import math


class Calculator:

    def __init__(self):
        self.expression = ""
        self.result = 0
        self.error = False

    def add_to_expression(self, value):
        self.expression += str(value)

    def clear(self):
        self.expression = ""
        self.result = 0
        self.error = False

    def backspace(self):
        if self.expression:
            self.expression = self.expression[:-1]

    def evaluate(self):
        try:
            expr = self.expression
            expr = expr.replace("×", "*")
            expr = expr.replace("÷", "/")
            expr = expr.replace("^", "**")
            self.result = eval(expr)
            self.expression = str(self.result)
            self.error = False
            return str(self.result)
        except ZeroDivisionError:
            self.error = True
            self.expression = ""
            return "Error: Division by zero"
        except Exception:
            self.error = True
            self.expression = ""
            return "Error: Invalid input"

    def sine(self, degrees):
        try:
            return round(math.sin(math.radians(float(degrees))), 10)
        except Exception:
            return "Error"

    def cosine(self, degrees):
        try:
            return round(math.cos(math.radians(float(degrees))), 10)
        except Exception:
            return "Error"

    def tangent(self, degrees):
        try:
            if float(degrees) % 180 == 90:
                return "Error: Undefined"
            return round(math.tan(math.radians(float(degrees))), 10)
        except Exception:
            return "Error"

    def arcsin(self, value):
        try:
            value = float(value)
            if value < -1 or value > 1:
                return "Error: Out of range"
            return round(math.degrees(math.asin(value)), 10)
        except Exception:
            return "Error"

    def arccos(self, value):
        try:
            value = float(value)
            if value < -1 or value > 1:
                return "Error: Out of range"
            return round(math.degrees(math.acos(value)), 10)
        except Exception:
            return "Error"

    def arctan(self, value):
        try:
            return round(math.degrees(math.atan(float(value))), 10)
        except Exception:
            return "Error"

    def square(self, value):
        try:
            return float(value) ** 2
        except Exception:
            return "Error"

    def square_root(self, value):
        try:
            value = float(value)
            if value < 0:
                return "Error: Negative number"
            return round(math.sqrt(value), 10)
        except Exception:
            return "Error"

    def power(self, base, exponent):
        try:
            return float(base) ** float(exponent)
        except Exception:
            return "Error"

    def logarithm(self, value):
        try:
            value = float(value)
            if value <= 0:
                return "Error: Must be positive"
            return round(math.log10(value), 10)
        except Exception:
            return "Error"

    def natural_log(self, value):
        try:
            value = float(value)
            if value <= 0:
                return "Error: Must be positive"
            return round(math.log(value), 10)
        except Exception:
            return "Error"

    def get_pi(self):
        return math.pi

    def get_e(self):
        return math.e
