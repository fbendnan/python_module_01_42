#!/usr/bin/env python3
class Plant:
    '''
    Docstring for Plant class
    '''
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def add_age(self):
        self.age += 1

    def grow(self, cm=1):
        self.height += cm

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


plant1 = Plant("Rose", 25, 30)
day = 1
cm = 1
while day <= 7:
    print(f"=== Day {day} ===")
    print(plant1.get_info())
    plant1.add_age()
    plant1.grow(cm)
    day += 1
print(f"Growth this week: +{cm * (day - 2)}cm")
