# Direct Implementation of Coffee Billing System using the decoraotr pattern.
from abc import ABC, abstractmethod
# Abstract base Component Interface
class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass

# Concrete Component
class BasicCoffee(Coffee):
    def get_cost(self):
        return 50  # cost of regular coffee

    def get_ingredients(self):
        return "Basic Coffee"

# Abstract Base Decorator
class CoffeeDecorator(Coffee,ABC):
    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost()

    def get_ingredients(self):
        return self.coffee.get_ingredients()

# Concrete Decorator Milk, Decorate the Basic Coffee with extra milk.This object is a Coffee and has a object of Coffee.
class Milk(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return super().get_cost() + 10

    def get_ingredients(self):
        return super().get_ingredients() + ", Milk"
    
# Concrete Decorator Sugar, Decorate the Basic Coffee with extra Sugar.
class Sugar(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return super().get_cost() + 5

    def get_ingredients(self):
        return super().get_ingredients() + ", Sugar"



def main():
    coffee = BasicCoffee()

    coffee = Milk(coffee)

    coffee = Sugar(coffee)

    print(f"Ingredients: {coffee.get_ingredients}")
    print(f"Cost: {coffee.get_cost}")


if __name__ == "__main__":
    main()
