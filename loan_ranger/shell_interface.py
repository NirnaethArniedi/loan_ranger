from .common_objects import LoanInputs, LoanResult
from .core_functions import compute_all_quantities


def _format_currency(value: float, width: int = 10) -> str:
    """
    Format a monetary value with consistent width.

    Parameters
    ----------
    value : float
        The value to format
    width : int, optional
        The width for right-alignment, by default 10

    Returns
    -------
    str
        Formatted string with 2 decimal places and right-aligned
    """
    return f"{value:>{width}.2f} €"


def _format_percentage(value: float, width: int = 10) -> str:
    """
    Format a percentage value with consistent width.

    Parameters
    ----------
    value : float
        The value to format as a percentage
    width : int, optional
        The width for right-alignment, by default 10

    Returns
    -------
    str
        Formatted string as percentage
    """
    return f"{value:>{width}.2%}"


def _format_duration(month_number: int, width: int = 10) -> str:
    """
    Format a duration in months with years conversion.

    Parameters
    ----------
    month_number : int
        Number of months
    width : int, optional
        The width for right-alignment, by default 10

    Returns
    -------
    str
        Formatted string showing months and years
    """
    years = month_number / 12
    return f"{month_number:>{width}} mois ({years:.1f} années)"


def _print_loan_result_line(label: str, value: str) -> None:
    """
    Print a formatted line for loan results.

    Parameters
    ----------
    label : str
        Label for the result
    value : str
        Formatted value string
    """
    label_width = 34
    print(f"{label:<{label_width}} {value}")


def pretty_print_results(loan_inputs: LoanInputs, loan_result: LoanResult) -> None:
    """
    Print a formatted summary of loan calculation results.

    Parameters
    ----------
    loan_inputs : LoanInputs
        Input parameters used for calculation
    loan_result : LoanResult
        Calculated results for the loan

    Returns
    -------
    None
        This function prints to stdout but doesn't return a value

    Notes
    -----
    Output is formatted in French with appropriate currency symbols.
    All monetary values are displayed with 2 decimal places.
    Percentage values are formatted using Python's percentage formatting.
    """
    # Unpack input parameters
    initial_capital = loan_inputs.initial_capital
    annual_rate = loan_inputs.annual_rate
    month_number = loan_inputs.month_number
    initial_cost = loan_inputs.initial_cost
    insurance_cost = loan_inputs.insurance_cost

    # Unpack result values
    monthly_installment_no_insurance = loan_result.monthly_installment_no_insurance
    full_installments = loan_result.full_installments
    total_interests = loan_result.total_interests
    total_cost_no_insurance = loan_result.total_cost_no_insurance
    total_cost = loan_result.total_cost
    full_taeg = loan_result.full_taeg
    taea = loan_result.taea

    # Print formatted results
    _print_loan_result_line("Capital emprunté:", _format_currency(initial_capital))
    _print_loan_result_line("Taux annuel:", _format_percentage(annual_rate))
    _print_loan_result_line("Durée d'emprunt:", _format_duration(month_number))
    _print_loan_result_line("Frais initiaux:", _format_currency(initial_cost))
    _print_loan_result_line("Coût total assurance:", _format_currency(insurance_cost))
    _print_loan_result_line("Mensualités hors assurance:", f"{_format_currency(monthly_installment_no_insurance)}/mois")
    _print_loan_result_line("Mensualités moyennes tout compris:", f"{_format_currency(full_installments)}/mois")
    _print_loan_result_line("Intérêt totaux:", _format_currency(total_interests))
    _print_loan_result_line("Coût total hors assurance:", _format_currency(total_cost_no_insurance))
    _print_loan_result_line("Coût total:", _format_currency(total_cost))
    _print_loan_result_line("TAEG (recalculé):", _format_percentage(full_taeg))
    _print_loan_result_line("TAEA (recalculé):", _format_percentage(taea))


def _get_float_input(prompt: str, min_value: float = None, default: float = None) -> float:
    """
    Get a validated float input from the user.

    Parameters
    ----------
    prompt : str
        The prompt to display to the user
    min_value : float, optional
        The minimum allowed value, by default None
    default : float, optional
        Default value if user enters empty string, by default None

    Returns
    -------
    float
        The validated float input
    """
    while True:
        try:
            # Handle default value if provided
            default_display = f" [default={default}]" if default is not None else ""
            input_str = input(f"{prompt}{default_display}: ")

            # Use default if input is empty
            if input_str == "" and default is not None:
                return default

            # Convert input to float, handling potential comma decimal separator
            value = float(input_str.replace(",", ".").strip())

            # Validate minimum value if provided
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue

            return value
        except ValueError:
            print("Please enter a valid number.")


def _get_int_input(prompt: str, min_value: int = None) -> int:
    """
    Get a validated integer input from the user.

    Parameters
    ----------
    prompt : str
        The prompt to display to the user
    min_value : int, optional
        The minimum allowed value, by default None

    Returns
    -------
    int
        The validated integer input
    """
    while True:
        try:
            value = int(input(f"{prompt}: "))

            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue

            return value
        except ValueError:
            print("Please enter a valid integer.")


def _get_option_input(prompt: str, options: list[str]) -> str:
    """
    Get a user selection from a list of options.

    Parameters
    ----------
    prompt : str
        The prompt to display to the user
    options : list[str]
        Valid option choices

    Returns
    -------
    str
        The selected option
    """
    while True:
        selection = input(prompt)
        if selection in options:
            return selection
        print(f"Please enter one of: {', '.join(options)}")


def _get_loan_duration() -> int:
    """
    Get loan duration from user, supporting both months and years input.

    Returns
    -------
    int
        Duration in months
    """
    duration_type = _get_option_input("Enter duration in: [1] Months or [2] Years: ", ["1", "2"])

    if duration_type == "1":
        # Get duration in months
        return _get_int_input("Enter loan duration (months)", min_value=1)
    else:
        # Get duration in years and convert to months
        years = _get_float_input("Enter loan duration (years)", min_value=0.1)
        month_number = int(years * 12)
        print(f"Converted to {month_number} months.")
        return month_number


def prompt_for_loan_inputs() -> LoanInputs:
    """
    Interactively prompt the user for loan parameters.

    Returns
    -------
    LoanInputs
        A named tuple containing all input parameters for the loan calculation

    Notes
    -----
    This function handles input validation and provides help text
    to guide users through entering the correct values.
    """
    print("\n===== Loan Calculator - Parameter Input =====\n")

    # Get basic loan parameters with validation
    initial_capital = _get_float_input("Enter loan amount (€)", min_value=0.01)
    annual_rate = _get_float_input("Enter annual interest rate (%)", min_value=0) / 100
    month_number = _get_loan_duration()

    # Get optional parameters with defaults
    initial_cost = _get_float_input("Enter upfront fees/costs (€)", min_value=0, default=0)
    insurance_cost = _get_float_input("Enter total insurance cost over loan period (€)", min_value=0, default=0)

    # Create and return LoanInputs
    return LoanInputs(
        initial_capital=initial_capital,
        annual_rate=annual_rate,
        month_number=month_number,
        initial_cost=initial_cost,
        insurance_cost=insurance_cost,
    )


def full_simu(
    initial_capital: float = None,
    annual_rate: float = None,
    month_number: int = None,
    initial_cost: float = None,
    insurance_cost: float = None,
) -> None:
    """
    Run a full loan simulation and print the results.

    Parameters
    ----------
    initial_capital : float, optional
        Principal amount of the loan. If None, will prompt for input.
    annual_rate : float, optional
        Annual interest rate (as a decimal, e.g., 0.05 for 5%). If None, will prompt for input.
    month_number : int, optional
        Total number of monthly payments. If None, will prompt for input.
    initial_cost : float, optional
        Upfront fees paid at loan origination. If None, will prompt for input.
    insurance_cost : float, optional
        Total cost of insurance over the life of the loan. If None, will prompt for input.

    Returns
    -------
    None
        This function prints results to stdout but doesn't return a value

    Notes
    -----
    If any parameter is None, the function will enter interactive mode and
    prompt the user for all required values.

    Examples
    --------
    >>> full_simu(200000, 0.02, 240, 1000, 8000)  # Direct parameters
    Capital emprunté:                   200000.00 €
    Taux annuel:                            2.00%
    Durée d'emprunt:                         240 mois (20.0 années)
    Frais initiaux:                        1000.00 €
    ...

    >>> full_simu()  # Interactive mode
    ===== Loan Calculator - Parameter Input =====
    Enter loan amount (€): 200000
    Enter annual interest rate (%): 2
    ...
    """
    # Check if we need interactive mode
    if any(param is None for param in [initial_capital, annual_rate, month_number, initial_cost, insurance_cost]):
        # Interactive mode - prompt for all parameters
        loan_inputs = prompt_for_loan_inputs()
    else:
        # Direct parameter mode
        loan_inputs = LoanInputs(
            initial_capital=initial_capital,
            annual_rate=annual_rate,
            month_number=month_number,
            initial_cost=initial_cost,
            insurance_cost=insurance_cost,
        )

    # Compute all results
    loan_result = compute_all_quantities(loan_inputs)

    # Print results
    print("\n===== Loan Calculation Results =====\n")
    pretty_print_results(loan_inputs, loan_result)
