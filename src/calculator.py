class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def sqrt(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of negative number")
        guess = x / 2.0
        for _ in range(20):  # 20 iteraciones para aproximación
            guess = (guess + x / guess) / 2.0
        return guess
