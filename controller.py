from model import CalculatorModel
from view import CalculatorView

class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView()

    def run(self):
        operation = ''
        while operation != 'quit':
            operation = input("Enter operation (quit, +, -, *, /): ")
            if operation == 'quit':
                break
            elif operation == 'history':
                self.view.display_history(self.model.get_history())
            else:
                var1 = float(input("Enter first number: "))
                var2 = float(input("Enter second number: "))
                if operation == '+':
                    result = self.model.add(var1, var2)
                elif operation == '-':
                    result = self.model.subtract(var1, var2)
                elif operation == '*':
                    result = self.model.multiply(var1, var2)
                elif operation == '/':
                    if var2 != 0:
                        result = self.model.divide(var1, var2)
                    else:
                        print("Cannot divide by zero!")
                        continue
                else:
                    print("Invalid operation!")
                    continue
                self.view.display_result(result)
