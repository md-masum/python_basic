# ErrorHandling.py

# Define a custom error type by subclassing Exception
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Function to demonstrate error handling
def divide_numbers(a, b):
    """
    Function to divide two numbers with error handling.
    Raises a CustomError if division by zero is attempted.
    """
    try:
        # Attempt to divide the numbers
        result = a / b
    except ZeroDivisionError:
        # Handle division by zero error
        raise CustomError("Division by zero is not allowed.")
    except TypeError:
        # Handle invalid input types
        raise CustomError("Both inputs must be numbers.")
    else:
        # If no exceptions occur, return the result
        return result
    finally:
        # This block always executes, regardless of exceptions
        print("Execution of divide_numbers is complete.")

# Example usage

# Check if the script is being run directly
if __name__ == "__main__":
    try:
        # Test with valid inputs
        print(divide_numbers(10, 2))  # Output: 5.0

        # Test with division by zero
        print(divide_numbers(10, 0))
    except CustomError as e:
        # Handle custom errors
        print(f"CustomError occurred: {e}")

    try:
        # Test with invalid input types
        print(divide_numbers(10, "a"))
    except CustomError as e:
        # Handle custom errors
        print(f"CustomError occurred: {e}")
    except Exception as e:
        # Handle any other unknown errors
        print(f"An unknown error occurred: {e}")