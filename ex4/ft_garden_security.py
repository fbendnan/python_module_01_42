class SecurePlant:
    '''
    a secure plant class with setter a to validated height, age
    and getter to get theire value
    '''
    def __init__(self,  name: str, height: int, age: int):
        self.name = name
        self._height = 25
        self._age = 30
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int):
        '''
        setter for set and validate height
        '''
        if height < 0:
            print(f"\nInvalid operation attempted: \
                height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int):
        '''
        setter for set and validate age
        '''
        if age < 0:
            print(f"\nInvalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age}days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


print("=== Garden Security System ===")
plant = SecurePlant("Rose", 5, 30)
print(f"\nCurrent plant: {plant.name} \
    ({plant.get_height()}cm, {plant.get_age()} days)")
