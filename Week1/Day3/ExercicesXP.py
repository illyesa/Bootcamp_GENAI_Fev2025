
# #1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# cat1 = Cat("C1", 4)
# cat2 = Cat("C2", 2)
# cat3 = Cat("C3", 7)
# cats=[cat1, cat2, cat3]

# def find_oldest_cat(cats):
#     oldest_cat = cats[0]

#     for cat in cats:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat

#     return oldest_cat
# print(f"The oldest cat is {find_oldest_cat(cats).name}, and is {find_oldest_cat(cats).age} years old")

# #2
# class Dog:
#     def __init__(self, dog_name, dog_height):
#         self.name = dog_name
#         self.height = dog_height
#     def bark(self):
#         print(f"{self.name} goes woof!")
#     def jump(self):
#         x=self.height *2
#         print(f"{self.name} jumps {x} cm high!")

# # dog1 = Dog("D1", 25)
# # dog1.bark()
# # dog1.jump()

# davids_dog = Dog("Rex", 50)
# print(davids_dog.name, davids_dog.height), davids_dog.bark(), davids_dog.jump()

# sarahs_dog = Dog("Teacup", 20)
# print(sarahs_dog.name, sarahs_dog.height), sarahs_dog.bark(), sarahs_dog.jump()

# if davids_dog.height > sarahs_dog.height:
#     print(f"{davids_dog.name} is the bigger dog")
# elif davids_dog.height < sarahs_dog.height:
#     print(f"{sarahs_dog.name} is the bigger dog")
# else:
#     print(f"{davids_dog.name} and {sarahs_dog.name} have the same height")


# #3
# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(f"{line}")
# stairway = Song(["There's a lady who's sure","all that glitters is gold","and she's buying a stairway to haven"])
# stairway.sing_me_a_song()

#4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else :
            print("Already here")
    def get_animals(self):
        print(self.animals)
    def sell_animals(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"Can't sold {animal_sold} because not in the zoo")
    def sort_animals(self):
        self.animals.sort()
        grouped_animals = {}
        for animal in self.animals :
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)
        for key in grouped_animals:
            if len(grouped_animals[key]) == 1:
                grouped_animals[key] = grouped_animals[key][0]
        
        self.grouped_animals = grouped_animals

    def get_groups(self):
        if hasattr(self, 'grouped_animals'):
            print("Animal Groups:")
            for letter, animals in self.grouped_animals.items():
                print(f"{letter}: {animals}")
        else:
            print("Animals haven't been sorted yet. Use the sort_animals() method first.")


# zoo1 = Zoo("Z1")
# zoo1.add_animal("Lion")
# zoo1.add_animal("dog")
# zoo1.sell_animals("Lion")
# zoo1.add_animal("Cat")
# zoo1.add_animal("Cat2")
# zoo1.get_animals()
# zoo1.sort_animals()
# zoo1.get_animals()
# zoo1.get_groups()

# Create the zoo object
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Add animals
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")

# Display current animals
ramat_gan_safari.get_animals()

# Sell an animal
ramat_gan_safari.sell_animals("Ape")

# Display animals after selling
ramat_gan_safari.get_animals()

# Sort and group animals
ramat_gan_safari.sort_animals()

# Display grouped animals
ramat_gan_safari.get_groups()



