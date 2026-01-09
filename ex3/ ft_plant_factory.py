class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


plant_list = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 15, 120),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120)
]
print("=== Plant Factory Output ===")
# for plant in plant_list:
#     print(plant.get_info())
i = 0
while i < 5:
    print(plant_list[i].get_info())
    i = i + 1
print(f"\nTotal plants created: {i}")
