def safe_divide(numerator, denominator):
    """
    Performs a safe division operation that handles division by zero
    and non-numeric input errors gracefully.
    """

    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Try performing the division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
import sys
from robust_division_calculator import safe_divide

def main():
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
