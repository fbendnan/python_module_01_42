# ft_garden_analytics.py

class GardenManager:
    """
    Manages one garden (one owner), while also tracking all gardens globally.
    Demonstrates:
    - instance methods (add_plant, help_plants_grow, garden_report, etc.)
    - nested helper class (GardenStats)
    - classmethod on the manager itself (create_garden_network)
    - staticmethods for utilities/statistics
    """

    _all_gardens = []

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        self._growth_log = 0  # track growth added through help_plants_grow
        GardenManager._all_gardens.append(self)

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def plants_nb(self):
        return len(self.plants)

    def help_plants_grow(self, cm=1):
        """
        Makes all plants grow and prints the growth lines.
        Also tracks total growth for analytics (without re-growing later).
        """
        print(f"{self.owner_name} is helping all plants grow...")
        total = 0
        for plant in self.plants:
            grew = plant.grow(cm)
            total += grew
            print(f"{plant.name} grew {grew}cm")
        self._growth_log += total

    def total_growth(self):
        """
        Returns the growth already applied (does NOT grow again).
        """
        return self._growth_log

    def garden_report(self):
        print(f"=== {self.owner_name}'s Garden Report ===")
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
        Nested helper class for statistics/analytics.
        """

        @staticmethod
        def garden_score(plants):
            """
            Scoring rule (chosen to match the expected output):
            - sum of all plant heights
            - +5 points for each FloweringPlant (including PrizeFlower)
            - +3 points per prize point for PrizeFlower
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

            return height_sum + (flowering_count * 5) + (prize_points_sum * 3)

        @staticmethod
        def height_test(h):
            return h >= 0

        @staticmethod
        def count_types(plants):
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
            return regular, flowering, prize


class Plant:
    def __init__(self, name, height, age):
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

    def grow(self, cm):
        self.__height += cm
        return cm

    def get_info(self):
        return f"- {self.name}: {self.__height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def get_info(self):
        return f"- {self.name}: {self.get_height()}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def get_info(self):
        return (
            f"- {self.name}: {self.get_height()}cm, {self.color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )


def main():
    print("=== Garden Management System Demo ===")

    # Alice garden
    alice = GardenManager("Alice")
    alice.add_plant(Plant("Oak Tree", 100, 10))
    alice.add_plant(FloweringPlant("Rose", 25, 30, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, 20, "yellow", 10))

    # Bob garden (chosen so score becomes 92 with the scoring rule)
    bob = GardenManager("Bob")
    bob.add_plant(Plant("Pine Tree", 80, 12))
    bob.add_plant(FloweringPlant("Tulip", 7, 15, "purple"))

    # Growth demo (only Alice grows in the example output)
    alice.help_plants_grow(1)

    # Alice report
    alice.garden_report()

    regular, flowering, prize = GardenManager.GardenStats.count_types(alice.plants)
    print(
        f"Plants added: {alice.plants_nb()}, Total growth: {alice.total_growth()}cm\n"
        f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers"
    )

    # Height validation test
    print(f"Height validation test: {GardenManager.GardenStats.height_test(alice.plants[0].get_height())}")

    # Garden network + scores
    network = GardenManager.create_garden_network()
    alice_score = GardenManager.GardenStats.garden_score(network["Alice"].plants)
    bob_score = GardenManager.GardenStats.garden_score(network["Bob"].plants)
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    print(f"Total gardens managed: {GardenManager.total_gardens_managed()}")


if __name__ == "__main__":
    main()
