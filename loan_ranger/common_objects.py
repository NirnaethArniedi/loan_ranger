from typing import NamedTuple


class LoanResult(NamedTuple):
    """
    Container for all results of a loan calculation.

    Attributes
    ----------
    monthly_installment_no_insurance : float
        Monthly payment amount excluding insurance costs
    full_installments : float
        Average monthly payment including all costs (principal, interest, insurance)
    total_interests : float
        Total interest paid over the life of the loan
    total_cost_no_insurance : float
        Total cost of the loan excluding insurance (interest + initial costs)
    total_cost : float
        Total cost of the loan including all expenses (interest + initial costs + insurance)
    full_taeg : float
        Taux Annuel Effectif Global (Annual Percentage Rate) including all costs
    taea : float
        Taux Annuel Effectif d'Assurance (Effective Annual Insurance Rate)
    """

    monthly_installment_no_insurance: float
    full_installments: float
    total_interests: float
    total_cost_no_insurance: float
    total_cost: float
    full_taeg: float
    taea: float


class LoanInputs(NamedTuple):
    """
    Container for loan input parameters.

    Attributes
    ----------
    initial_capital : float
        Principal amount of the loan
    annual_rate : float
        Annual interest rate (as a decimal, e.g., 0.05 for 5%)
    month_number : int
        Total number of monthly payments
    initial_cost : float
        Upfront fees paid at loan origination
    insurance_cost : float
        Total cost of insurance over the life of the loan
    """

    initial_capital: float
    annual_rate: float
    month_number: int
    initial_cost: float = 0.0
    insurance_cost: float = 0.0
