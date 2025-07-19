class Calculator:

    def __init__(self):
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }

    def show_operation_symbols(self):
        for symbol in self.operations:
            print(symbol)


    def add(self, n1, n2):
        return n1 + n2

    def subtract(self, n1, n2):
        return n1 - n2

    def multiply(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        if n2 == 0:
            raise ValueError("Cannot divide by zero!")
        return n1 / n2

