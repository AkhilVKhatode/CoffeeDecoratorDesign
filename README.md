# Coffee Shop Decorator Pattern

This project demonstrates the use of the **Decorator Design Pattern** to enhance the functionality of a basic coffee shop ordering system. The system allows the user to select a base coffee type (like Espresso or Cappuccino) and customize it with additional ingredients such as Milk, Sugar, and Vanilla using decorators.

## Features

- **Base Coffee Types**: The system supports multiple coffee types such as Espresso and Cappuccino.
- **Dynamic Customization**: You can dynamically add ingredients to your coffee using decorators. Each ingredient (e.g., Milk, Sugar, Vanilla) enhances the coffee's description and cost.
- **Decorator Pattern**: The pattern allows the system to extend functionality without modifying the original coffee classes.

## Code Explanation

- **`Coffee` Interface**: The `Coffee` class defines the basic methods `get_description()` and `get_cost()`, which must be implemented by all coffee types.
- **Concrete Coffee Classes**: `Espresso` and `Cappuccino` are two concrete implementations of the `Coffee` interface.
- **`CoffeeDecorator` Class**: This is an abstract class that implements the `Coffee` interface and wraps a `Coffee` object, delegating method calls to the wrapped coffee.
- **Concrete Decorators**: `MilkDecorator`, `SugarDecorator`, and `VanillaDecorator` extend `CoffeeDecorator` to add specific ingredients to the coffee and modify its cost and description.
- **Main Program**: The `main()` function demonstrates how to create a coffee order, add decorators, and print the description and total cost.

## Example Usage

The following example demonstrates how to use the decorators:

```python
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
```

Output Example:
```yaml
Order: Espresso, Milk, Sugar
Total Cost: $ 2.75

Order: Cappuccino, Vanilla
Total Cost: $ 3.75
```
