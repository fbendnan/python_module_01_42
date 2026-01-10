class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def add_age(self):
        self.age += 1

    def grow(self):
        self.height += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


plant1 = Plant("Rose", 25, 30)
day = 1
print(f"=== Day {day} ===")
print(plant1.get_info())
day = 7
i = 0
while i < day - 1:
    plant1.add_age()
    plant1.grow()
    i += 1
print(f"=== Day {day} ===")
print(plant1.get_info())
print(f"Growth this week: +{i}cm")
