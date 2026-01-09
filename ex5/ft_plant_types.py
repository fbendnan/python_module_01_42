class SecurePlant:
    def __init__(self,  name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)
    def set_height(self, height):
        if height < 0:
            print(f"\nInvalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
    def set_age(self, age):
        if age < 0:
            print(f"\nInvalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
    def get_height(self):
        return self.__height
    def get_age(self):
        return self.__age

class Flower(SecurePlant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return f"{self.name} is blooming beautifully!"

    def get_info(self):
        return f"{self.name} (Flower): {self.get_height()}cm, {self.get_age()} days, {self.color} color"

class Tree(SecurePlant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        return f"{self.name}  provides 78 square meters of shade"
    
    def get_info(self):
        return f"{self.name}(Tree): {self.get_height()}cm, {self.get_age()} days, {self.trunk_diameter} diameter"
        
class Vegetable(SecurePlant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutritional_value(self):
        return f"{self.name} is rich in {self.nutritional_value}"

    def get_info(self):
        return f"{self.name} (Vegetable): {self.get_height()}cm, {self.get_age()} days, {self.harvest_season} harvest"

def main():
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
