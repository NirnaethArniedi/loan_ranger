from collections.abc import Callable

import numpy as np
import scipy.optimize as optimize

from .common_objects import LoanInputs, LoanResult


def _convert_prop_rate(origin_rate: float, periods: int) -> float:
    """
    Convert an annual rate to a rate per period.

    Parameters
    ----------
    origin_rate : float
        The original annual interest rate (as a decimal, e.g., 0.05 for 5%)
    periods : int
        Number of periods per year (e.g., 12 for monthly periods)

    Returns
    -------
    float
        Interest rate per period

    Notes
    -----
    Uses simple division for rate conversion. For compound interest,
    a different formula would be required: (1 + origin_rate)**(1/periods) - 1
    """
    prop_rate = origin_rate / periods
    return prop_rate


def _calculate_compound_factor(period_rate: float, period_number: int) -> float:
    """
    Calculate the compound factor for the loan formula.

    Parameters
    ----------
    period_rate : float
        Interest rate per period (as a decimal)
    period_number : int
        Total number of payment periods

    Returns
    -------
    float
        The compound factor (1 + r)^n
    """
    return (1 + period_rate) ** period_number


def _installment_per_period(period_rate: float, period_number: int, initial_capital: float) -> float:
    """
    Calculate the installment per period using the standard amortization formula.

    Parameters
    ----------
    period_rate : float
        Interest rate per period (as a decimal)
    period_number : int
        Total number of payment periods
    initial_capital : float
        Principal amount of the loan

    Returns
    -------
    float
        Payment amount per period

    Notes
    -----
    Uses the standard formula for calculating equal payments on an amortizing loan:
    PMT = P * r * (1 + r)^n / ((1 + r)^n - 1)
    where P = principal, r = interest rate per period, n = number of periods

    This formula assumes the interest rate is not zero. For zero interest rates,
    a simple division of principal by number of periods should be used instead.
    """
    # Handle the edge case of zero interest rate
    if period_rate == 0:
        return initial_capital / period_number

    # Calculate the compound factor (1 + r)^n
    compound_factor = _calculate_compound_factor(period_rate, period_number)

    # Calculate the denominator ((1 + r)^n - 1)
    denominator = compound_factor - 1

    # Calculate the numerator (P * r * (1 + r)^n)
    numerator = initial_capital * period_rate * compound_factor

    # Calculate the installment
    installment = numerator / denominator

    return installment


def compute_interest_cost(annual_rate: float, month_number: int, initial_capital: float) -> tuple[float, float]:
    """
    Compute the monthly installment and total interest cost for a loan.

    Parameters
    ----------
    annual_rate : float
        Annual interest rate (as a decimal, e.g., 0.05 for 5%)
    month_number : int
        Total number of monthly payments
    initial_capital : float
        Principal amount of the loan

    Returns
    -------
    monthly_installment : float
        The fixed monthly payment amount
    total_cost : float
        The total interest paid over the life of the loan

    Examples
    --------
    >>> monthly_payment, total_interest = compute_interest_cost(0.05, 360, 200000)
    >>> print(f"Monthly payment: {monthly_payment:.2f}")
    Monthly payment: 1073.64
    >>> print(f"Total interest: {total_interest:.2f}")
    Total interest: 186510.40
    """
    monthly_rate = _convert_prop_rate(annual_rate, 12)
    monthly_installment = _installment_per_period(monthly_rate, month_number, initial_capital)
    total_reimbursed = monthly_installment * month_number
    total_cost = total_reimbursed - initial_capital
    return monthly_installment, total_cost


def _create_taeg_objective_function(
    month_number: int, full_installments: float, initial_cost: float, initial_capital: float
) -> Callable[[float], tuple[float, float]]:
    """
    Create the objective function for TAEG calculation.

    Parameters
    ----------
    month_number : int
        Total number of monthly payments
    full_installments : float
        The average monthly payment including all costs
    initial_cost : float
        Upfront fees paid at loan origination
    initial_capital : float
        Principal amount of the loan

    Returns
    -------
    Callable[[float], tuple[float, float]]
        A function that takes a rate and returns (function_value, derivative_value)
    """

    def objective_function(rate: float) -> tuple[float, float]:
        """
        Objective function for root-finding algorithm with its derivative.

        Parameters
        ----------
        rate : float
            The discount rate to evaluate

        Returns
        -------
        tuple[float, float]
            (function_value, derivative_value)
        """
        # Create arrays for efficient calculation
        pow_array = np.arange(1, month_number + 1)
        deriv_pow = np.arange(0, month_number)

        # Calculate rate raised to different powers
        rate_array = np.power(rate, pow_array)

        # Calculate sum of installments discounted at the given rate
        sum_installs = np.sum(full_installments * rate_array)

        # Calculate function value (should be zero at the correct rate)
        value = initial_cost - initial_capital + sum_installs

        # Calculate derivative for more efficient optimization
        derivative = full_installments * np.sum(pow_array * np.power(rate, deriv_pow))

        return value, derivative

    return objective_function


def _calculate_average_installment(total_reimbursed: float, initial_cost: float, month_number: int) -> float:
    """
    Calculate the average monthly installment.

    Parameters
    ----------
    total_reimbursed : float
        Total amount to be paid back
    initial_cost : float
        Upfront fees paid at loan origination
    month_number : int
        Total number of monthly payments

    Returns
    -------
    float
        The average monthly payment
    """
    reimbursed_by_installments = total_reimbursed - initial_cost
    return reimbursed_by_installments / month_number


def _convert_monthly_to_annual_rate(monthly_rate: float) -> float:
    """
    Convert a monthly rate to an annual rate.

    Parameters
    ----------
    monthly_rate : float
        Rate per month

    Returns
    -------
    float
        Equivalent annual rate
    """
    return (1 / monthly_rate) ** 12 - 1


def compute_taeg(
    month_number: int, total_cost: float, initial_cost: float, initial_capital: float
) -> tuple[float, float]:
    """
    Calculate the TAEG (Taux Annuel Effectif Global) for a loan.

    Parameters
    ----------
    month_number : int
        Total number of monthly payments
    total_cost : float
        Total cost of the loan including all expenses
    initial_cost : float
        Upfront fees paid at loan origination
    initial_capital : float
        Principal amount of the loan

    Returns
    -------
    taeg : float
        The effective annual percentage rate (TAEG)
    full_installments : float
        The average monthly payment including all costs

    Notes
    -----
    This function uses numerical optimization to find the effective rate that
    satisfies the NPV equation for the loan. The optimization uses a root-finding
    algorithm with analytical derivatives for efficiency.

    The starting point for optimization (x0=0.99) is chosen to be near 1 to
    ensure proper convergence of the algorithm for typical loan rates.

    Raises
    ------
    RuntimeError
        If the optimization algorithm fails to converge
    """
    # Calculate total amount to be repaid
    total_reimbursed = total_cost + initial_capital

    # Calculate average monthly installment
    full_installments = _calculate_average_installment(total_reimbursed, initial_cost, month_number)

    # Create the objective function for optimization
    taeg_objective = _create_taeg_objective_function(month_number, full_installments, initial_cost, initial_capital)

    # Find the rate that makes the objective function zero
    taeg_optim = optimize.root_scalar(
        taeg_objective,
        x0=0.99,  # Starting near 1 for convergence
        xtol=1e-7,
        fprime=True,
    )

    # Convert the monthly rate to an annual rate
    taeg = _convert_monthly_to_annual_rate(taeg_optim.root)

    return float(taeg), full_installments


def compute_all_quantities(loan_inputs: LoanInputs) -> LoanResult:
    """
    Compute all quantities related to a loan.

    Parameters
    ----------
    loan_inputs : LoanInputs
        A named tuple containing all input parameters for the loan calculation

    Returns
    -------
    LoanResult
        A named tuple containing all computed loan metrics:
        - monthly_installment_no_insurance: Monthly payment excluding insurance
        - full_installments: Monthly payment including all costs
        - total_interests: Total interest paid
        - total_cost_no_insurance: Total cost excluding insurance
        - total_cost: Total cost including all expenses
        - full_taeg: Effective annual rate (APR)
        - taea: Effective annual insurance rate

    Notes
    -----
    The TAEA (Taux Annuel Effectif d'Assurance) is calculated as the
    difference between the full TAEG and the TAEG without insurance costs.
    This provides a measure of the effective cost of the insurance component.
    """
    # Unpack input parameters
    initial_capital = loan_inputs.initial_capital
    annual_rate = loan_inputs.annual_rate
    month_number = loan_inputs.month_number
    initial_cost = loan_inputs.initial_cost
    insurance_cost = loan_inputs.insurance_cost

    # Calculate monthly installment and total interest
    monthly_installment_no_insurance, total_interests = compute_interest_cost(
        annual_rate, month_number, initial_capital
    )

    # Calculate total costs
    total_cost_no_insurance = total_interests + initial_cost
    total_cost = total_cost_no_insurance + insurance_cost

    # Calculate TAEG with and without insurance
    full_taeg, full_installments = compute_taeg(month_number, total_cost, initial_cost, initial_capital)
    taeg_no_insurance, _ = compute_taeg(month_number, total_cost_no_insurance, initial_cost, initial_capital)

    # Calculate insurance effective rate
    taea = full_taeg - taeg_no_insurance

    # Return all results
    return LoanResult(
        monthly_installment_no_insurance,
        full_installments,
        total_interests,
        total_cost_no_insurance,
        total_cost,
        full_taeg,
        taea,
    )
