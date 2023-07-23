class CalculatorModel:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append((a, '+', b, result))
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append((a, '-', b, result))
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append((a, '*', b, result))
        return result

    def divide(self, a, b):
        result = a / b
        self.history.append((a, '/', b, result))
        return result

    def get_history(self):
        return self.history
