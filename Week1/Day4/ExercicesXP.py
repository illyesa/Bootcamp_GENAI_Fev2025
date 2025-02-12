
##1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# beng = Bengal("beng", 3)
# chart = Chartreux("chart", 2)
# siame = Siamese("siame", 5)
# all_cats =[beng, chart, siame]
# sara_pets = Pets(all_cats)
# sara_pets.walk()

##2
# class Dog():
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         print(f"{self.name} is barking")
#     def run_speed(self):
#         return self.weight/self.age*10
#     def fight(self, other_dog):
#         if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
#             print(f"{self.name} win")
#         else:
#             print(f"{other_dog.name} win")

# d1 = Dog("d1", 3, 12)
# d2 = Dog("d2", 7, 18)
# d3 = Dog("d3", 3, 15)
# d1.fight(d3)
# d2.fight(d3)
# d2.fight(d1)

# #3
# #from ExercicesXP import Dog #import in the same file because we can submit only one file
# import random
# class PetDog(Dog):
#     def __init__(self, trained):
#         trained = False
#         self.trained = trained
#     def train(self):
#         self.trained = True
#         self.bark()
#     def play(self, *args):
#         b= []
#         for a in args:
#             b.append(a.name)
#         print(f"{self.name}, {b} all play together.")
#     def do_a_trick(self):
#         r = random.random(1, 4)
#         if self.trained == True:
#             if r == 1 :
#                 print(f"{self.name} does a barrel roll")
#             elif r == 2:
#                 print(f"{self.name} stands on his back legs")
#             elif r == 3:
#                 print(f"{self.name} shakes your hand")
#             else:
#                 print(f"{self.name} plays dead")
#         else:
#             print("not trained")

#4
class Family():
    def __init__(self, last_name, members):
        self.members = members
        self.last_name = last_name
    def born(self, **kwargs):
        self.members.append(kwargs)
        print("Congratulation")
    def is_18(self, name):
        for i in range(len(self.members)):
            if self.members[i]["name"]==name:
        #if self.members["name"] == name:
                return self.members[i]["age"] >= 18
            else:
                return False
        else:
            print(f"{name} is not in this family")
    def family_presentation(self):
        print(f"Family name: {self.last_name}")
        for member in self.members:
            #member.append("is_child", self.is_18(member["age"]))
            print(member)

family = Family("Smith", [
    {"name": "Michael", "age": 35, "gender": "Male", "is_child": False},
    {"name": "Sarah", "age": 32, "gender": "Female", "is_child": False}
])
family.family_presentation()
family.born(name='John', age=0, gender='Male', is_child=True)
print(family.members[0]["name"])
print(family.is_18("Michael"))
family.family_presentation()


