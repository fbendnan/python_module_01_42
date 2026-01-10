#!/usr/bin/env python3
class SecurePlant:
    '''
    base class (parent class) representing a plant with
    a validated attributes (height, age)
    '''
    def __init__(self,  name: str, height: int, age: int):
        """
        Initialize a SecurePlant object.
        """
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int):
        '''
        Set the plant's height after validation.
        '''
        if height < 0:
            print(f"\nInvalid operation attempted:"
                  f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height

    def set_age(self, age: int):
        '''
        Set the plant's age after validation.
        '''
        if age < 0:
            print(f"\nInvalid operation attempted:"
                  f"age {age}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age

    def get_height(self) -> int:
        '''
        Get the plant's height.
        '''
        return self.__height

    def get_age(self) -> int:
        '''
        Get the plant's age.
        '''
        return self.__age


class Flower(SecurePlant):
    '''
        Represents a flower plant with a specific color.
    '''
    def __init__(self, name: str, height: int, age: int, color: str):
        '''
        Initialize a Flower object.
        '''
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        '''
        Simulate the flower blooming.
        '''
        return f"{self.name} is blooming beautifully!"

    def get_info(self) -> str:
        '''
        Get detailed information about the flower.
        '''
        return (f"{self.name} (Flower): {self.get_height()}cm,"
                f" {self.get_age()} days, {self.color} color")


class Tree(SecurePlant):
    '''
    Represents a tree with a trunk diameter.
    '''
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        '''
        Initialize a Tree object.
        '''
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        '''
        Simulate shade production by the tree.
        '''
        return f"{self.name}  provides 78 square meters of shade"

    def get_info(self) -> str:
        '''
        Get detailed information about the tree.
        '''
        return (f"{self.name}(Tree): {self.get_height()}cm, {self.get_age()}"
                f"days, {self.trunk_diameter} diameter")


class Vegetable(SecurePlant):
    '''
    Represents a vegetable plant with harvest season and nutritional value.
    '''
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        '''
        Initialize a Vegetable object.
        '''
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutritional_value(self) -> str:
        '''
        Get the nutritional value of the vegetable.
        '''
        return f"{self.name} is rich in {self.nutritional_value}"

    def get_info(self) -> str:
        '''
        Get detailed information about the vegetable.
        '''
        return (f"{self.name} (Vegetable): {self.get_height()}cm, "
                f"{self.get_age()} days, {self.harvest_season} harvest")


def main():
    '''
    Main function that creates plant objects and displays their information.
    '''
    Rose = Flower("Rose", 25, 30, "red")
    Daisy = Flower("Daisy", 20, 38, "yellow")

    Oak = Tree("Oak", 500, 1825, 50)
    Oval = Tree("Oval", 600, 1445, 60)

    Tomato = Vegetable("Tomato", 80, 90, "summer", " vitamin C")
    Carrot = Vegetable("Carrot", 80, 90, "fall", " vitamin A")

    print("=== Garden Plant Types ===")
    print()
    print(Rose.get_info())
    print(Rose.bloom())
    print(Daisy.get_info())
    print(Daisy.bloom())
    print()
    print(Oak.get_info())
    print(Oak.produce_shade())
    print(Oval.get_info())
    print(Oval.produce_shade())
    print()
    print(Tomato.get_info())
    print(Tomato.get_nutritional_value())
    print(Carrot.get_info())
    print(Carrot.get_nutritional_value())


main()
