# Strategy interface
class DiscountStrategy:
    def apply_discount(self, price):
        raise NotImplementedError

# Concrete strategies
class ChristmasDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9 # 10% off

class EasterDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.5 # 50% off

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price # no discount

# Context class
class Product:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy or NoDiscount()

    def get_price(self):
        return self.discount_strategy.apply_discount(self.price)

# Usage example
p1 = Product(100, ChristmasDiscount())
p2 = Product(100, EasterDiscount())
p3 = Product(100)

print(p1.get_price()) # prints 90.0
print(p2.get_price()) # prints 50.0
print(p3.get_price()) # prints 100
