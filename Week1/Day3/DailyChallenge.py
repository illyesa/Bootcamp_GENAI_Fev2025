
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count=1):
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal:<10} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        plural_animals = [animal + 's' for animal in animal_types]
        if len(plural_animals) > 1:
            animal_list = ", ".join(plural_animals[:-1]) + " and " + plural_animals[-1]
        else:
            animal_list = plural_animals[0]
        return f"{self.name}'s farm has {animal_list}."
    