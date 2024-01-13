##**arithmetic_expression.py**

from abc import ABC, abstractmethod

class ArithmeticExpression(ABC):
    @abstractmethod
    def evaluate(self):
        pass


##**expression.py**

class Expression(ArithmeticExpression):
    def __init__(self, left_expression, right_expression, operation):
        self.left_expression = left_expression
        self.right_expression = right_expression
        self.operation = operation

    def evaluate(self):
        if self.operation == "ADD":
            value = self.left_expression.evaluate() + self.right_expression.evaluate()
        elif self.operation == "SUBTRACT":
            value = self.left_expression.evaluate() - self.right_expression.evaluate()
        elif self.operation == "DIVIDE":
            value = self.left_expression.evaluate() / self.right_expression.evaluate()
        elif self.operation == "MULTIPLY":
            value = self.left_expression.evaluate() * self.right_expression.evaluate()

        print(f"Expression value is: {value}")
        return value


##**number.py**

class Number(ArithmeticExpression):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        print(f"Number value is: {self.value}")
        return self.value



##**main.py**

from arithmetic_expression import ArithmeticExpression
from expression import Expression
from number import Number

def main():
    two = Number(2)
    one = Number(1)
    seven = Number(7)

    add_expression = Expression(one, seven, "ADD")
    parent_expression = Expression(two, add_expression, "MULTIPLY")

    print(parent_expression.evaluate())

if __name__ == "__main__":
    main()

