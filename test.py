import pandas 
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._init_height = 0.0
        self._height = 0.0
        self._age_of_plant = 0
        self.stats = Plant.Stats(self)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age_of_plant} days old")
        self.stats.increment_show()

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"\n{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return False
        self._height = round(height, 1)
        # print(f"\nHeight updated: {height}cm")
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected\n")
            return False
        self._age_of_plant = age
        # print(f"Age updated: {age} days")
        return True

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_of_plant

    def grow(self, length: float) -> None:
        self._height = round(self._height + length, 1)
        self.stats.increment_grow()

    def age(self, days: int = 1) -> None:
        self._age_of_plant += days
        self.stats.increment_age()

    @staticmethod
    def older_than_a_year(age: int) -> bool:
        if age > 365:
            return True
        return False

    @classmethod
    def anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self, plant: 'Plant') -> None:
            self.__grow_count = 0
            self.__age_count = 0
            self.__show_count = 0
            self.plant = plant

        def increment_grow(self) -> None:
            self.__grow_count += 1

        def increment_age(self) -> None:
            self.__age_count += 1

        def increment_show(self) -> None:
            self.__show_count += 1

        def display(self) -> None:
            print(f"[statistics of {self.plant.get_name()}]")
            print(f"Stats: {self.__grow_count} grow, {self.__age_count} age,"
                  f" {self.__show_count} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        super().set_height(height)
        super().set_age(age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        # print(f"[asking the {self._name} to bloom]")
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        super().set_height(height)
        super().set_age(age)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 trunk_diameter: float
                 ) -> None:
        super().__init__(name, height, age)
        super().set_height(height)
        super().set_age(age)
        self.trunk_diameter = trunk_diameter
        self.__shade_count = 0

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )
        self.__shade_count += 1

    def get_shade_count(self) -> int:
        return self.__shade_count

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 harvest_season: str,
                 nutritional_value: int = 0
                 ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self, length: float = 2.1) -> None:
        super().grow(length)
        self.nutritional_value += 1

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += days - 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def print_stats(plant: Plant) -> None:
    plant.stats.display()
    if plant.__class__ is Tree:
        print(f" {plant.get_shade_count()} shades")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_a_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print_stats(rose)
    print(f"[asking the {rose.get_name()} to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    print_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print_stats(oak)
    oak.produce_shade()
    print_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print(f"[make {sunflower.get_name()} grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print_stats(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    print_stats(unknown)


if __name__ == "__main__":
    main()
