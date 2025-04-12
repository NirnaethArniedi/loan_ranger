# Loan ranger

Rapide module pour calculer différents paramètres
d'un emprunt immobilier.

## Dépendances

- `python>3.10`
- `numpy`
- `scipy`

(For more details see `pyproject.toml` file or the Dev stuff below)

## Utilisation

### Short version

Aller dans le répertoire ou le repo a été cloné.
Executer le module.

```shell
cd loan_ranger
python -m loan_ranger
```

Et c'est tout.

### Long version

Importer le module dans une une console python.
Appeler la fonction "full_simu".
Et voilà.

```python
import loan_ranger

loan_ranger.full_simu()
```

## Structure

All code lives in `loan_ranger` folder.

- `common_objects`: Rapide structure pour stocker input et résultat (plus propre que de balader des tuples à rallonge)
- `core_functions`: Sexy stuff, là ou sont les calculs "compliqué
- `shell_interface`: Fonctions pour faire l'interface user: prompting, printing, regrouper le tout, etc

## Development stuff

- Project managed with uv, run `uv sync` to install project and dependencies
- Use ruff as a formatter, included in dev dependencies (`uv sync --all-extras` to install dev dependencies)
- First version developped in a single file, docstrings and refactoring courtesy of Claude.ai
<!-- loan_ranger documentation master file, created by
sphinx-quickstart on Sat Apr 12 18:29:26 2025.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->

# loan_ranger documentation

Add your content using `reStructuredText` syntax. See the
[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)
documentation for details.

# Contents:

* [loan_ranger package](loan_ranger.md)
  * [`LoanInputs`](loan_ranger.md#loan_ranger.LoanInputs)
    * [`LoanInputs.initial_capital`](loan_ranger.md#loan_ranger.LoanInputs.initial_capital)
    * [`LoanInputs.annual_rate`](loan_ranger.md#loan_ranger.LoanInputs.annual_rate)
    * [`LoanInputs.month_number`](loan_ranger.md#loan_ranger.LoanInputs.month_number)
    * [`LoanInputs.initial_cost`](loan_ranger.md#loan_ranger.LoanInputs.initial_cost)
    * [`LoanInputs.insurance_cost`](loan_ranger.md#loan_ranger.LoanInputs.insurance_cost)
    * [`LoanInputs.annual_rate`](loan_ranger.md#id0)
    * [`LoanInputs.initial_capital`](loan_ranger.md#id1)
    * [`LoanInputs.initial_cost`](loan_ranger.md#id2)
    * [`LoanInputs.insurance_cost`](loan_ranger.md#id3)
    * [`LoanInputs.month_number`](loan_ranger.md#id4)
  * [`LoanResult`](loan_ranger.md#loan_ranger.LoanResult)
    * [`LoanResult.monthly_installment_no_insurance`](loan_ranger.md#loan_ranger.LoanResult.monthly_installment_no_insurance)
    * [`LoanResult.full_installments`](loan_ranger.md#loan_ranger.LoanResult.full_installments)
    * [`LoanResult.total_interests`](loan_ranger.md#loan_ranger.LoanResult.total_interests)
    * [`LoanResult.total_cost_no_insurance`](loan_ranger.md#loan_ranger.LoanResult.total_cost_no_insurance)
    * [`LoanResult.total_cost`](loan_ranger.md#loan_ranger.LoanResult.total_cost)
    * [`LoanResult.full_taeg`](loan_ranger.md#loan_ranger.LoanResult.full_taeg)
    * [`LoanResult.taea`](loan_ranger.md#loan_ranger.LoanResult.taea)
    * [`LoanResult.full_installments`](loan_ranger.md#id5)
    * [`LoanResult.full_taeg`](loan_ranger.md#id6)
    * [`LoanResult.monthly_installment_no_insurance`](loan_ranger.md#id7)
    * [`LoanResult.taea`](loan_ranger.md#id8)
    * [`LoanResult.total_cost`](loan_ranger.md#id9)
    * [`LoanResult.total_cost_no_insurance`](loan_ranger.md#id10)
    * [`LoanResult.total_interests`](loan_ranger.md#id11)
  * [`compute_all_quantities()`](loan_ranger.md#loan_ranger.compute_all_quantities)
  * [`full_simu()`](loan_ranger.md#loan_ranger.full_simu)
  * [Submodules](loan_ranger.md#submodules)
  * [loan_ranger.common_objects module](loan_ranger.md#module-loan_ranger.common_objects)
    * [`LoanInputs`](loan_ranger.md#loan_ranger.common_objects.LoanInputs)
      * [`LoanInputs.initial_capital`](loan_ranger.md#loan_ranger.common_objects.LoanInputs.initial_capital)
      * [`LoanInputs.annual_rate`](loan_ranger.md#loan_ranger.common_objects.LoanInputs.annual_rate)
      * [`LoanInputs.month_number`](loan_ranger.md#loan_ranger.common_objects.LoanInputs.month_number)
      * [`LoanInputs.initial_cost`](loan_ranger.md#loan_ranger.common_objects.LoanInputs.initial_cost)
      * [`LoanInputs.insurance_cost`](loan_ranger.md#loan_ranger.common_objects.LoanInputs.insurance_cost)
      * [`LoanInputs.annual_rate`](loan_ranger.md#id12)
      * [`LoanInputs.initial_capital`](loan_ranger.md#id13)
      * [`LoanInputs.initial_cost`](loan_ranger.md#id14)
      * [`LoanInputs.insurance_cost`](loan_ranger.md#id15)
      * [`LoanInputs.month_number`](loan_ranger.md#id16)
    * [`LoanResult`](loan_ranger.md#loan_ranger.common_objects.LoanResult)
      * [`LoanResult.monthly_installment_no_insurance`](loan_ranger.md#loan_ranger.common_objects.LoanResult.monthly_installment_no_insurance)
      * [`LoanResult.full_installments`](loan_ranger.md#loan_ranger.common_objects.LoanResult.full_installments)
      * [`LoanResult.total_interests`](loan_ranger.md#loan_ranger.common_objects.LoanResult.total_interests)
      * [`LoanResult.total_cost_no_insurance`](loan_ranger.md#loan_ranger.common_objects.LoanResult.total_cost_no_insurance)
      * [`LoanResult.total_cost`](loan_ranger.md#loan_ranger.common_objects.LoanResult.total_cost)
      * [`LoanResult.full_taeg`](loan_ranger.md#loan_ranger.common_objects.LoanResult.full_taeg)
      * [`LoanResult.taea`](loan_ranger.md#loan_ranger.common_objects.LoanResult.taea)
      * [`LoanResult.full_installments`](loan_ranger.md#id17)
      * [`LoanResult.full_taeg`](loan_ranger.md#id18)
      * [`LoanResult.monthly_installment_no_insurance`](loan_ranger.md#id19)
      * [`LoanResult.taea`](loan_ranger.md#id20)
      * [`LoanResult.total_cost`](loan_ranger.md#id21)
      * [`LoanResult.total_cost_no_insurance`](loan_ranger.md#id22)
      * [`LoanResult.total_interests`](loan_ranger.md#id23)
  * [loan_ranger.core_functions module](loan_ranger.md#module-loan_ranger.core_functions)
    * [`compute_all_quantities()`](loan_ranger.md#loan_ranger.core_functions.compute_all_quantities)
    * [`compute_interest_cost()`](loan_ranger.md#loan_ranger.core_functions.compute_interest_cost)
    * [`compute_taeg()`](loan_ranger.md#loan_ranger.core_functions.compute_taeg)
  * [loan_ranger.shell_interface module](loan_ranger.md#module-loan_ranger.shell_interface)
    * [`full_simu()`](loan_ranger.md#loan_ranger.shell_interface.full_simu)
    * [`pretty_print_results()`](loan_ranger.md#loan_ranger.shell_interface.pretty_print_results)
    * [`prompt_for_loan_inputs()`](loan_ranger.md#loan_ranger.shell_interface.prompt_for_loan_inputs)
# loan_ranger package

### *class* loan_ranger.LoanInputs(initial_capital: float, annual_rate: float, month_number: int, initial_cost: float = 0.0, insurance_cost: float = 0.0)

Bases: `NamedTuple`

Container for loan input parameters.

#### initial_capital

Principal amount of the loan

* **Type:**
  float

#### annual_rate

Annual interest rate (as a decimal, e.g., 0.05 for 5%)

* **Type:**
  float

#### month_number

Total number of monthly payments

* **Type:**
  int

#### initial_cost

Upfront fees paid at loan origination

* **Type:**
  float

#### insurance_cost

Total cost of insurance over the life of the loan

* **Type:**
  float

#### annual_rate *: `float`*

Alias for field number 1

#### initial_capital *: `float`*

Alias for field number 0

#### initial_cost *: `float`*

Alias for field number 3

#### insurance_cost *: `float`*

Alias for field number 4

#### month_number *: `int`*

Alias for field number 2

### *class* loan_ranger.LoanResult(monthly_installment_no_insurance: float, full_installments: float, total_interests: float, total_cost_no_insurance: float, total_cost: float, full_taeg: float, taea: float)

Bases: `NamedTuple`

Container for all results of a loan calculation.

#### monthly_installment_no_insurance

Monthly payment amount excluding insurance costs

* **Type:**
  float

#### full_installments

Average monthly payment including all costs (principal, interest, insurance)

* **Type:**
  float

#### total_interests

Total interest paid over the life of the loan

* **Type:**
  float

#### total_cost_no_insurance

Total cost of the loan excluding insurance (interest + initial costs)

* **Type:**
  float

#### total_cost

Total cost of the loan including all expenses (interest + initial costs + insurance)

* **Type:**
  float

#### full_taeg

Taux Annuel Effectif Global (Annual Percentage Rate) including all costs

* **Type:**
  float

#### taea

Taux Annuel Effectif d’Assurance (Effective Annual Insurance Rate)

* **Type:**
  float

#### full_installments *: `float`*

Alias for field number 1

#### full_taeg *: `float`*

Alias for field number 5

#### monthly_installment_no_insurance *: `float`*

Alias for field number 0

#### taea *: `float`*

Alias for field number 6

#### total_cost *: `float`*

Alias for field number 4

#### total_cost_no_insurance *: `float`*

Alias for field number 3

#### total_interests *: `float`*

Alias for field number 2

### loan_ranger.compute_all_quantities(loan_inputs)

Compute all quantities related to a loan.

* **Return type:**
  [`LoanResult`](#loan_ranger.common_objects.LoanResult)
* **Parameters:**
  **loan_inputs** ([*LoanInputs*](#loan_ranger.LoanInputs)) – A named tuple containing all input parameters for the loan calculation
* **Returns:**
  A named tuple containing all computed loan metrics:
  - monthly_installment_no_insurance: Monthly payment excluding insurance
  - full_installments: Monthly payment including all costs
  - total_interests: Total interest paid
  - total_cost_no_insurance: Total cost excluding insurance
  - total_cost: Total cost including all expenses
  - full_taeg: Effective annual rate (APR)
  - taea: Effective annual insurance rate
* **Return type:**
  [LoanResult](#loan_ranger.LoanResult)

### Notes

The TAEA (Taux Annuel Effectif d’Assurance) is calculated as the
difference between the full TAEG and the TAEG without insurance costs.
This provides a measure of the effective cost of the insurance component.

### loan_ranger.full_simu(initial_capital=None, annual_rate=None, month_number=None, initial_cost=None, insurance_cost=None)

Run a full loan simulation and print the results.

* **Return type:**
  `None`
* **Parameters:**
  * **initial_capital** (*float* *,* *optional*) – Principal amount of the loan. If None, will prompt for input.
  * **annual_rate** (*float* *,* *optional*) – Annual interest rate (as a decimal, e.g., 0.05 for 5%). If None, will prompt for input.
  * **month_number** (*int* *,* *optional*) – Total number of monthly payments. If None, will prompt for input.
  * **initial_cost** (*float* *,* *optional*) – Upfront fees paid at loan origination. If None, will prompt for input.
  * **insurance_cost** (*float* *,* *optional*) – Total cost of insurance over the life of the loan. If None, will prompt for input.
* **Returns:**
  This function prints results to stdout but doesn’t return a value
* **Return type:**
  None

### Notes

If any parameter is None, the function will enter interactive mode and
prompt the user for all required values.

### Examples

```pycon
>>> full_simu(200000, 0.02, 240, 1000, 8000)  # Direct parameters
Capital emprunté:                   200000.00 €
Taux annuel:                            2.00%
Durée d'emprunt:                         240 mois (20.0 années)
Frais initiaux:                        1000.00 €
...
```

```pycon
>>> full_simu()  # Interactive mode
===== Loan Calculator - Parameter Input =====
Enter loan amount (€): 200000
Enter annual interest rate (%): 2
...
```

## Submodules

## loan_ranger.common_objects module

### *class* loan_ranger.common_objects.LoanInputs(initial_capital: float, annual_rate: float, month_number: int, initial_cost: float = 0.0, insurance_cost: float = 0.0)

Bases: `NamedTuple`

Container for loan input parameters.

#### initial_capital

Principal amount of the loan

* **Type:**
  float

#### annual_rate

Annual interest rate (as a decimal, e.g., 0.05 for 5%)

* **Type:**
  float

#### month_number

Total number of monthly payments

* **Type:**
  int

#### initial_cost

Upfront fees paid at loan origination

* **Type:**
  float

#### insurance_cost

Total cost of insurance over the life of the loan

* **Type:**
  float

#### annual_rate *: `float`*

Alias for field number 1

#### initial_capital *: `float`*

Alias for field number 0

#### initial_cost *: `float`*

Alias for field number 3

#### insurance_cost *: `float`*

Alias for field number 4

#### month_number *: `int`*

Alias for field number 2

### *class* loan_ranger.common_objects.LoanResult(monthly_installment_no_insurance: float, full_installments: float, total_interests: float, total_cost_no_insurance: float, total_cost: float, full_taeg: float, taea: float)

Bases: `NamedTuple`

Container for all results of a loan calculation.

#### monthly_installment_no_insurance

Monthly payment amount excluding insurance costs

* **Type:**
  float

#### full_installments

Average monthly payment including all costs (principal, interest, insurance)

* **Type:**
  float

#### total_interests

Total interest paid over the life of the loan

* **Type:**
  float

#### total_cost_no_insurance

Total cost of the loan excluding insurance (interest + initial costs)

* **Type:**
  float

#### total_cost

Total cost of the loan including all expenses (interest + initial costs + insurance)

* **Type:**
  float

#### full_taeg

Taux Annuel Effectif Global (Annual Percentage Rate) including all costs

* **Type:**
  float

#### taea

Taux Annuel Effectif d’Assurance (Effective Annual Insurance Rate)

* **Type:**
  float

#### full_installments *: `float`*

Alias for field number 1

#### full_taeg *: `float`*

Alias for field number 5

#### monthly_installment_no_insurance *: `float`*

Alias for field number 0

#### taea *: `float`*

Alias for field number 6

#### total_cost *: `float`*

Alias for field number 4

#### total_cost_no_insurance *: `float`*

Alias for field number 3

#### total_interests *: `float`*

Alias for field number 2

## loan_ranger.core_functions module

### loan_ranger.core_functions.compute_all_quantities(loan_inputs)

Compute all quantities related to a loan.

* **Return type:**
  [`LoanResult`](#loan_ranger.common_objects.LoanResult)
* **Parameters:**
  **loan_inputs** ([*LoanInputs*](#loan_ranger.LoanInputs)) – A named tuple containing all input parameters for the loan calculation
* **Returns:**
  A named tuple containing all computed loan metrics:
  - monthly_installment_no_insurance: Monthly payment excluding insurance
  - full_installments: Monthly payment including all costs
  - total_interests: Total interest paid
  - total_cost_no_insurance: Total cost excluding insurance
  - total_cost: Total cost including all expenses
  - full_taeg: Effective annual rate (APR)
  - taea: Effective annual insurance rate
* **Return type:**
  [LoanResult](#loan_ranger.LoanResult)

### Notes

The TAEA (Taux Annuel Effectif d’Assurance) is calculated as the
difference between the full TAEG and the TAEG without insurance costs.
This provides a measure of the effective cost of the insurance component.

### loan_ranger.core_functions.compute_interest_cost(annual_rate, month_number, initial_capital)

Compute the monthly installment and total interest cost for a loan.

* **Return type:**
  `tuple`[`float`, `float`]
* **Parameters:**
  * **annual_rate** (*float*) – Annual interest rate (as a decimal, e.g., 0.05 for 5%)
  * **month_number** (*int*) – Total number of monthly payments
  * **initial_capital** (*float*) – Principal amount of the loan
* **Returns:**
  * **monthly_installment** (*float*) – The fixed monthly payment amount
  * **total_cost** (*float*) – The total interest paid over the life of the loan

### Examples

```pycon
>>> monthly_payment, total_interest = compute_interest_cost(0.05, 360, 200000)
>>> print(f"Monthly payment: {monthly_payment:.2f}")
Monthly payment: 1073.64
>>> print(f"Total interest: {total_interest:.2f}")
Total interest: 186510.40
```

### loan_ranger.core_functions.compute_taeg(month_number, total_cost, initial_cost, initial_capital)

Calculate the TAEG (Taux Annuel Effectif Global) for a loan.

* **Return type:**
  `tuple`[`float`, `float`]
* **Parameters:**
  * **month_number** (*int*) – Total number of monthly payments
  * **total_cost** (*float*) – Total cost of the loan including all expenses
  * **initial_cost** (*float*) – Upfront fees paid at loan origination
  * **initial_capital** (*float*) – Principal amount of the loan
* **Returns:**
  * **taeg** (*float*) – The effective annual percentage rate (TAEG)
  * **full_installments** (*float*) – The average monthly payment including all costs

### Notes

This function uses numerical optimization to find the effective rate that
satisfies the NPV equation for the loan. The optimization uses a root-finding
algorithm with analytical derivatives for efficiency.

The starting point for optimization (x0=0.99) is chosen to be near 1 to
ensure proper convergence of the algorithm for typical loan rates.

* **Raises:**
  **RuntimeError** – If the optimization algorithm fails to converge

## loan_ranger.shell_interface module

### loan_ranger.shell_interface.full_simu(initial_capital=None, annual_rate=None, month_number=None, initial_cost=None, insurance_cost=None)

Run a full loan simulation and print the results.

* **Return type:**
  `None`
* **Parameters:**
  * **initial_capital** (*float* *,* *optional*) – Principal amount of the loan. If None, will prompt for input.
  * **annual_rate** (*float* *,* *optional*) – Annual interest rate (as a decimal, e.g., 0.05 for 5%). If None, will prompt for input.
  * **month_number** (*int* *,* *optional*) – Total number of monthly payments. If None, will prompt for input.
  * **initial_cost** (*float* *,* *optional*) – Upfront fees paid at loan origination. If None, will prompt for input.
  * **insurance_cost** (*float* *,* *optional*) – Total cost of insurance over the life of the loan. If None, will prompt for input.
* **Returns:**
  This function prints results to stdout but doesn’t return a value
* **Return type:**
  None

### Notes

If any parameter is None, the function will enter interactive mode and
prompt the user for all required values.

### Examples

```pycon
>>> full_simu(200000, 0.02, 240, 1000, 8000)  # Direct parameters
Capital emprunté:                   200000.00 €
Taux annuel:                            2.00%
Durée d'emprunt:                         240 mois (20.0 années)
Frais initiaux:                        1000.00 €
...
```

```pycon
>>> full_simu()  # Interactive mode
===== Loan Calculator - Parameter Input =====
Enter loan amount (€): 200000
Enter annual interest rate (%): 2
...
```

### loan_ranger.shell_interface.pretty_print_results(loan_inputs, loan_result)

Print a formatted summary of loan calculation results.

* **Return type:**
  `None`
* **Parameters:**
  * **loan_inputs** ([*LoanInputs*](#loan_ranger.LoanInputs)) – Input parameters used for calculation
  * **loan_result** ([*LoanResult*](#loan_ranger.LoanResult)) – Calculated results for the loan
* **Returns:**
  This function prints to stdout but doesn’t return a value
* **Return type:**
  None

### Notes

Output is formatted in French with appropriate currency symbols.
All monetary values are displayed with 2 decimal places.
Percentage values are formatted using Python’s percentage formatting.

### loan_ranger.shell_interface.prompt_for_loan_inputs()

Interactively prompt the user for loan parameters.

* **Return type:**
  [`LoanInputs`](#loan_ranger.common_objects.LoanInputs)
* **Returns:**
  A named tuple containing all input parameters for the loan calculation
* **Return type:**
  [LoanInputs](#loan_ranger.LoanInputs)

### Notes

This function handles input validation and provides help text
to guide users through entering the correct values.
