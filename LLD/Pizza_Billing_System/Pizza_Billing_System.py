from abc import ABC, abstractmethod

#Abstract base Pizza Interface
class Pizza(ABC):
    @abstractmethod
    def get_cost():
        pass

    @abstractmethod
    def get_ingredients():
        pass

#concrete Pizza
class PlainPizza(Pizza):
    def get_cost(self):
        return 50
    
    def get_ingredients(self):
        return "Plain Pizza"

#Abstract base Decorator Interface
class PizzaDecorator(Pizza, ABC):

    def __init__(self, pizza) -> None:
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost()
    
    def get_ingredients(self):
        return self.pizza.get_ingredients()
    

#Concrete Decorator
class Cheese(PizzaDecorator):
    def __init__(self, pizza) -> None:
        super().__init__(pizza)

    def get_cost(self):
        return super().get_cost() + 20

    def get_ingredients(self):
        return super().get_ingredients() + ", Cheese"

class TomatoSauce(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_cost(self):
        return super().get_cost() + 15

    def get_ingredients(self):
        return super().get_ingredients() + ", Tomato Sauce"
    


#Client Code
    
def main():
    # Create a new plain pizza
    pizza = PlainPizza()

    # Add cheese to the pizza
    pizza = Cheese(pizza)

    # Add tomato sauce to the pizza
    pizza = TomatoSauce(pizza)

    # Now we have a pizza with cheese and tomato sauce
    print(f"Ingredients: {pizza.get_ingredients()}")
    print(f"Cost: {pizza.get_cost()}")

if __name__ == "__main__":
    main()
