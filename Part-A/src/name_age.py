"""Ask for a user's name and age to estimate 
their birth year.

Input:
    User's name as a string entered through the console.
    User's age as an integer entered through the console.
    Current year as an integer obtained from the system.

Process:
    Subtract the user's age from the current year.

Output:
    Display a personalized message as a string in the console.
Typical usage example:
    What is your name? Pat
    How old are you? 31
    Hello Pat! You were born in 1995.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"Hello {name}! You were born in {birth_year}.")

# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Replace with an APA-style reference for a source you used, or delete.
# TODO: Replace with another APA-style reference, or delete this TODO line.
