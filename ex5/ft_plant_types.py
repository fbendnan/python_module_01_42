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

class Tree(SecurePlant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        return f"{self.name}  provides 78 square meters of shade"

class Vegetable(SecurePlant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

Rose = Flower("Rose", 25, 30, "red")
Daisy = Flower("Daisy", 20, 38, "yellow")

Oak = Tree("Oak", 500, 1825, 50)
Oval = Tree("Oval", 600, 1445, 60)

Tomato = Vegetable("Tomato", 80, 90, "summer", " vitamin C")
Carrot = Vegetable("Carrot", 80, 90, "fall", " vitamin A")

print("=== Garden Plant Types ===")
print(f"\n{Rose.name} (Flower): {Rose.get_height()}cm, {Rose.get_age()} days, {Rose.color} color")
print(f"{Rose.bloom()}")
print(f"\n{Daisy.name} (Flower): {Daisy.get_height()}cm, {Daisy.get_age()} days, {Daisy.color} color")
print(f"{Daisy.bloom()}")

print(f"\n{Oak.name}(Tree): {Oak.get_height()}cm, {Oak.get_age()} days, {Oak.trunk_diameter} diameter")
print(Oak.produce_shade())
print(f"\n{Oval.name}(Tree): {Oval.get_height()}cm, {Oval.get_age()} days, {Oval.trunk_diameter} diameter")
print(Oval.produce_shade())

print(f"\n{Tomato.name} (Vegetable): {Tomato.get_height()}cm, {Tomato.get_age()} days, {Tomato.harvest_season} harvest")
print(f"{Tomato.name} is rich in {Tomato.nutritional_value}")
print(f"\n{Carrot.name} (Vegetable): {Carrot.get_height()}cm, {Carrot.get_age()} days, {Carrot.harvest_season} harvest")
print(f"{Carrot.name} is rich in {Carrot.nutritional_value}")