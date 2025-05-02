from abc import ABC, abstractmethod

# Base Coffee interface
class Coffee(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

# Concrete Coffee classes
class Espresso(Coffee):
    def get_description(self):
        return "Espresso"

    def get_cost(self):
        return 2.00

class Cappuccino(Coffee):
    def get_description(self):
        return "Cappuccino"

    def get_cost(self):
        return 3.00

# CoffeeDecorator base class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def get_description(self):
        return self._coffee.get_description()

    def get_cost(self):
        return self._coffee.get_cost()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def get_description(self):
        return self._coffee.get_description() + ", Milk"

    def get_cost(self):
        return self._coffee.get_cost() + 0.50

class SugarDecorator(CoffeeDecorator):
    def get_description(self):
        return self._coffee.get_description() + ", Sugar"

    def get_cost(self):
        return self._coffee.get_cost() + 0.25

class VanillaDecorator(CoffeeDecorator):
    def get_description(self):
        return self._coffee.get_description() + ", Vanilla"

    def get_cost(self):
        return self._coffee.get_cost() + 0.75

# Using the decorators
def main():
    coffee = Espresso()
    coffee = MilkDecorator(coffee)
    coffee = SugarDecorator(coffee)
    print("Order:", coffee.get_description())
    print("Total Cost: $", coffee.get_cost())

    another_coffee = Cappuccino()
    another_coffee = VanillaDecorator(another_coffee)
    print("\nOrder:", another_coffee.get_description())
    print("Total Cost: $", another_coffee.get_cost())

if __name__ == "__main__":
    main()
