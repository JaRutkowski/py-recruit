class CalculatorView:
    def display_result(self, result):
        print(f"Result: {result}")

    def display_history(self, history):
        for operation in history:
            print(f"{operation[0]} {operation[1]} {operation[2]} = {operation[3]}")
