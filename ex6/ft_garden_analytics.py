class GardenManager:
    """
    Manages one garden (one owner), while also tracking all gardens globally.
    Demonstrates:
    - instance methods (add_plant, help_plants_grow, garden_report)
    - nested helper class (GardenStats)
    - staticmethods for statistics
    - cllassmethods
    """
    _all_gardens = []

    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.plants = []
        self.total_growth = 0
        GardenManager._all_gardens.append(self)

    def add_plant(self, plant, shoud_print: bool) -> None:
        self.plants.append(plant)
        if shoud_print:
            print(f"Added {plant.name} to {self.owner_name}'s garden")

    def help_plants_grow(self, shoud_print: bool, cm=1) -> None:
        """
        Makes all plants grow and prints the growth lines.
        Also tracks total growth for analytics (without re-growing later).
        """
        if shoud_print:
            print(f"\n{self.owner_name} is helping all plants grow...")
        total = 0
        for plant in self.plants:
            grew = plant.grow(cm)
            total += grew
            if shoud_print:
                print(f"{plant.name} grew {grew}cm")
        self.total_growth += total

    def garden_report(self):
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())

    @classmethod
    def create_garden_network(cls):
        """
        Works on the manager type itself.
        Returns a mapping owner_name -> GardenManager instance.
        """
        network = {}
        for garden in cls._all_gardens:
            network[garden.owner_name] = garden
        return network

    @classmethod
    def total_gardens_managed(cls):
        return len(cls._all_gardens)

    class GardenStats:
        """
        Nested helper class for statistics
        """
        @staticmethod
        def height_test(h: int):
            print(f"Height validation test: {h >= 2}")

        @staticmethod
        def plants_info(plants, total_growth: int):
            regular = 0
            flowering = 0
            prize = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            print(f"\nPlants added: {len(plants)}, Total growth: \
                {total_growth}cm")
            print(f"Plant types: {regular} regular, {flowering} flowering, \
                {prize} prize flowers\n")

        @staticmethod
        def garden_score(plants):
            """
            Scoring rule:
            - sum of all plant heights
            - +3 points for each FloweringPlant
            - +5 points per prize point for PrizeFlower
            """
            height_sum = 0
            flowering_count = 0
            prize_points_sum = 0

            for plant in plants:
                height_sum += plant.get_height()
                if isinstance(plant, FloweringPlant):
                    flowering_count += 1
                if isinstance(plant, PrizeFlower):
                    prize_points_sum += plant.prize_points

            return height_sum + (flowering_count * 3) + (prize_points_sum * 5)


class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.__height = 0
        self.set_height(height)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"\nInvalid operation attempted: height \
                {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height

    def get_height(self):
        return self.__height

    def grow(self, cm: int):
        self.__height += cm
        return cm

    def get_info(self):
        return f"- {self.name}: {self.__height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        return f"- {self.name}: {self.get_height()}cm, \
            {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize_points: int):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self):
        return (
            f"- {self.name}: {self.get_height()}cm, \
                {self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )


def main():
    print("=== Garden Management System Demo ===\n")
    alice = GardenManager("Alice")
    alice.add_plant(Plant("Oak Tree", 101), True)
    alice.add_plant(FloweringPlant("Rose", 26, "red"), True)
    alice.add_plant(PrizeFlower("Sunflower", 51, "yellow", 10), True)
    bob = GardenManager("Bob")
    bob.add_plant(Plant("Oak Tree", 101), False)
    bob.add_plant(FloweringPlant("Rose", 26, "red"), False)

    alice.help_plants_grow(True)

    alice.garden_report()
    alice.GardenStats.plants_info(alice.plants, alice.total_growth)

    alice.GardenStats.height_test(alice.total_growth)
    alice_score = alice.GardenStats.garden_score(alice.plants)
    bob_score = alice.GardenStats.garden_score(bob.plants)
    print(f"Garden scores - Alice: {alice_score}, Bob:{bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens_managed()}")


main()
