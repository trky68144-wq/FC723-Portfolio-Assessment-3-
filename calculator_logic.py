# Import the math module to use mathematical functions like sin, cos, log, sqrt
import math
# This class contains all the calculator operations
class Calculator:

    # This runs when we create a new Calculator object
    def __init__(self):
        # Store the current expression the user is typing
        self.expression = ""
        # Store the last calculated result
        self.result = 0
        # Track whether an error has occurred
        self.error = False

    # Add a number or operator to the current expression
    def add_to_expression(self, value):
        # Convert the value to a string and add it to the expression
        self.expression += str(value)

    # Reset everything back to the starting state
    def clear(self):
        # Empty the expression
        self.expression = ""
        # Reset the result to zero
        self.result = 0
        # Clear any error
        self.error = False

    # Remove the last character from the expression
    def backspace(self):
        # Only remove if the expression is not already empty
        if self.expression:
            self.expression = self.expression[:-1]

    # Calculate the result of the current expression
    def evaluate(self):
        try:
            # Copy the expression so we can modify it safely
            expr = self.expression
            # Replace display symbols with Python operators
            expr = expr.replace("×", "*")
            expr = expr.replace("÷", "/")
            expr = expr.replace("^", "**")
            expr = expr.replace("x", "*")        
            # Calculate the result using eval
            self.result = eval(expr)
            # Store the result as the new expression
            self.expression = str(self.result)
            # No error occurred
            self.error = False
            # Return the result as a string to show on the display
            return str(self.result)
        except ZeroDivisionError:
            # Handle division by zero
            self.error = True
            self.expression = ""
            return "Error: Division by zero"
        except Exception:
            # Handle any other invalid expression
            self.error = True
            self.expression = ""
            return "Error: Invalid input"

    # Calculate the sine of an angle given in degrees
    def sine(self, degrees):
        try:
            # Convert degrees to radians first, then calculate sine
            return round(math.sin(math.radians(float(degrees))), 10)
        except Exception:
            return "Error"

    # Calculate the cosine of an angle given in degrees
    def cosine(self, degrees):
        try:
            # Convert degrees to radians first, then calculate cosine
            return round(math.cos(math.radians(float(degrees))), 10)
        except Exception:
            return "Error"

    # Calculate the tangent of an angle given in degrees
    def tangent(self, degrees):
        try:
            # Tangent is undefined at 90, 270, etc. so return an error
            if float(degrees) % 180 == 90:
                return "Error: Undefined"
            # Convert degrees to radians first, then calculate tangent
            return round(math.tan(math.radians(float(degrees))), 10)
        except Exception:
            return "Error"

    # Calculate the inverse sine (arcsin) and return the result in degrees
    def arcsin(self, value):
        try:
            value = float(value)
            # Arcsin only works for values between -1 and 1
            if value < -1 or value > 1:
                return "Error: Out of range"
            # Calculate arcsin and convert the result from radians to degrees
            return round(math.degrees(math.asin(value)), 10)
        except Exception:
            return "Error"

    # Calculate the inverse cosine (arccos) and return the result in degrees
    def arccos(self, value):
        try:
            value = float(value)
            # Arccos only works for values between -1 and 1
            if value < -1 or value > 1:
                return "Error: Out of range"
            # Calculate arccos and convert the result from radians to degrees
            return round(math.degrees(math.acos(value)), 10)
        except Exception:
            return "Error"

    # Calculate the inverse tangent (arctan) and return the result in degrees
    def arctan(self, value):
        try:
            # Calculate arctan and convert the result from radians to degrees
            return round(math.degrees(math.atan(float(value))), 10)
        except Exception:
            return "Error"

    # Calculate the square of a number (number multiplied by itself)
    def square(self, value):
        try:
            return float(value) ** 2
        except Exception:
            return "Error"

    # Calculate the square root of a number
    def square_root(self, value):
        try:
            value = float(value)
            # Square root of a negative number is not a real number
            if value < 0:
                return "Error: Negative number"
            return round(math.sqrt(value), 10)
        except Exception:
            return "Error"

    # Calculate base raised to the power of exponent
    def power(self, base, exponent):
        try:
            return float(base) ** float(exponent)
        except Exception:
            return "Error"

    # Calculate the logarithm base 10 of a number
    def logarithm(self, value):
        try:
            value = float(value)
            # Logarithm only works for positive numbers
            if value <= 0:
                return "Error: Must be positive"
            return round(math.log10(value), 10)
        except Exception:
            return "Error"

    # Calculate the natural logarithm (ln) of a number
    def natural_log(self, value):
        try:
            value = float(value)
            # Natural log only works for positive numbers
            if value <= 0:
                return "Error: Must be positive"
            # math.log() calculates the natural logarithm (ln)
            return round(math.log(value), 10)
        except Exception:
            return "Error"

    # Return the value of pi (3.14159...)
    def get_pi(self):
        return math.pi

    # Return the value of Euler's number e (2.71828...)
    def get_e(self):
        return math.e