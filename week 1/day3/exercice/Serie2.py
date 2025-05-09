 #exercice1
import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def definition(self):
        print("A circle is a shape consisting of all points in a plane that are at a given distance from a given point, the center.")

 
c = Circle(5)
print(f"Perimeter: {c.perimeter():.2f}")
print(f"Area: {c.area():.2f}")
c.definition()
#exercice2
import random

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reversed_list(self):
        return self.letters[::-1]

    def sorted_list(self):
        return sorted(self.letters)

    def generate_random_numbers(self):
        return [random.randint(1, 100) for _ in range(len(self.letters))]

# Example usage
my_list = MyList(['b', 'a', 'd', 'c'])
print("Original list:", my_list.letters)
print("Reversed list:", my_list.reversed_list())
print("Sorted list:", my_list.sorted_list())
print("Random numbers list:", my_list.generate_random_numbers())
#exercice3
class MenuManager:
    def __init__(self):
        self.menu = [
            {
                "name": "Soup",
                "price": 10,
                "spice": "B",
                "gluten": False
            },
            {
                "name": "Hamburger",
                "price": 15,
                "spice": "A",
                "gluten": True
            },
            {
                "name": "Salad",
                "price": 18,
                "spice": "A",
                "gluten": False
            },
            {
                "name": "French Fries",
                "price": 5,
                "spice": "C",
                "gluten": False
            },
            {
                "name": "Beef bourguignon",
                "price": 25,
                "spice": "B",
                "gluten": True
            }
        ]

    def add_item(self, name, price, spice, gluten):
        dish = {
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        }
        self.menu.append(dish)
        print(f"{name} added to menu.")

    def update_item(self, name, new_price=None, new_spice=None, new_gluten=None):
        for dish in self.menu:
            if dish["name"] == name:
                if new_price is not None:
                    dish["price"] = new_price
                if new_spice is not None:
                    dish["spice"] = new_spice
                if new_gluten is not None:
                    dish["gluten"] = new_gluten
                print(f"{name} has been updated.")
                return
        print(f"{name} not found in menu.")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(f"{name} removed from menu.")
                return
        print(f"{name} not found in menu.")

    def display_menu(self):
        print("\n--- Current Menu ---")
        for dish in self.menu:
            print(f"{dish['name']} | Price: ${dish['price']} | Spice: {dish['spice']} | Gluten: {dish['gluten']}")
        print("--------------------")

# Example usage
if __name__ == "__main__":
    manager = MenuManager()

    manager.display_menu()

    manager.add_item("Spaghetti", 20, "B", True)
    manager.update_item("Soup", new_price=12)
    manager.remove_item("French Fries")

    manager.display_menu()