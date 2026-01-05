class Plant:
    def __init__(self, name, height, a_ge):
        self.name = name
        self.height = height
        self.a_ge = a_ge
    def age(self):
        self.a_ge += 1
    def grow(self):
        self.height += 1
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.a_ge} days old"

plant1 = Plant("Rose", 25, 30)
day = 1
print(f"=== Day {day} ===")
print(plant1.get_info())
day = 7
i = 0
while i < day - 1:
    plant1.age()
    plant1.grow()
    i += 1
print(f"=== Day {day} ===")
print(plant1.get_info())
print(f"Growth this week: +{i}cm")