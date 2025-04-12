from .shell_interface import full_simu


def main():
    """
    Main entry point for the loan ranger application.

    This function provides a simple command-line interface for the loan calculator.
    """
    print("======================================")
    print("    Loan Calculator and Simulator    ")
    print("======================================")
    print("\nThis program calculates loan details including monthly payments,")
    print("interest costs, and effective rates (TAEG/TAEA).\n")

    while True:
        # Run the simulation in interactive mode
        full_simu()

        # Ask if user wants to calculate another loan
        again = input("\nCalculate another loan? (y/n): ").lower().strip()
        if again != "y":
            break

    print("\nThank you for using the Loan Ranger!")


if __name__ == "__main__":
    main()
