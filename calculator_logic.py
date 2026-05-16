# Import the math module to use mathematical functions like sin, cos, log, sqrt
import math
from tkinter import StringVar

# This class contains all the calculator operations
class Calculator:

    # This runs when we create a new Calculator object
    def __init__(self):
        #Store angle mode
        self.angle_mode = StringVar(value = "deg")
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

            expr = expr.replace("π", "math.pi")
            expr = expr.replace("e", "math.e")

            #change angle mode
            if self.angle_mode.get() == "deg":
                #degrees
                sine = lambda x: math.sin(math.radians(x))
                cosine = lambda x: math.cos(math.radians(x))
                tangent = lambda x: math.tan(math.radians(x))

                inverse_s = lambda x: math.degrees(math.asin(x))
                inverse_c = lambda x: math.degrees(math.acos(x))
                inverse_t = lambda x: math.degrees(math.atan(x))
            else:
                # Radians setup
                sine = lambda x: math.sin(x)
                cosine = lambda x: math.cos(x)
                tangent = lambda x: math.tan(x)

                inverse_s = lambda x: math.asin(x)
                inverse_c = lambda x: math.acos(x)
                inverse_t = lambda x: math.atan(x)

            # inverse trigonometry function
            expr = expr.replace("arcsin(", "inverse_s(")
            expr = expr.replace("arccos(", "inverse_c(")
            expr = expr.replace("arctan(", "inverse_t(")

            # trigonometry functions
            expr = expr.replace("sin(", "sine(")
            expr = expr.replace("cos(", "cosine(")
            expr = expr.replace("tan(", "tangent(")

            #log functions
            expr = expr.replace("log(", "math.log10(")
            expr = expr.replace("ln(", "math.log(")

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

    # Calculate the square of a number (number multiplied by itself)
    def square(self, value):
        try:
            return round(float(value) ** 2,10)
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