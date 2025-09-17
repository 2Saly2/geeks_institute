class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:", self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        groups = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            groups.setdefault(first_letter, []).append(animal)
        return groups

    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


rabat_zoo = Zoo("New York Zoo")
rabat_zoo.add_animal("Giraffe")
rabat_zoo.add_animal("Elephant")
rabat_zoo.add_animal("Bear")
rabat_zoo.add_animal("Ape")
rabat_zoo.add_animal("Emu")
rabat_zoo.get_animals()
rabat_zoo.sell_animal("Bear")
rabat_zoo.get_animals()
rabat_zoo.get_groups()
