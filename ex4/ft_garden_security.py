class SecurePlant:
    def __init__(self,  name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def set_height(self):
        if height > 0:
            self.height = height
            return f"Height updated: {height}cm [OK]"
        else:
            return f"\nInvalid operation attempted: height {height}cm [REJECTED]\
                    \nSecutity: Negative height rejected"

plant = SecurePlant("Rose", 25, 30)