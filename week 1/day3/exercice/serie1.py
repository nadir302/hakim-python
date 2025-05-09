#exercice1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

 
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 5)
cat3 = Cat("Shadow", 7)

 
def find_oldest_cat(cat1, cat2, cat3):
    cats = [cat1, cat2, cat3]
    oldest = max(cats, key=lambda cat: cat.age)
    return oldest

 
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
#exercice2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

 
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

 
for dog in [davids_dog, sarahs_dog]:
    print(f"\nDog Name: {dog.name}")
    print(f"Height: {dog.height} cm")
    dog.bark()
    dog.jump()

 
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
else:
    print(f"{sarahs_dog.name} is bigger.")  
#exercice3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

 
stairway_lyrics = [
    "There’s a lady who's sure",
    "All that glitters is gold",
    "And she’s buying a stairway to heaven"
]

stairway_song = Song(stairway_lyrics)
stairway_song.sing_me_a_song()  
#exercice4   
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
         
        self.animals.sort()
        grouped = {}
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in grouped:
                grouped[first_letter] = []
            grouped[first_letter].append(animal)
        return grouped

    def get_groups(self):
        groups = self.sort_animals()
        print("\nGrouped Animals:")
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")

 
my_zoo = Zoo("Wild Adventure")


my_zoo.add_animal("Baboon")
my_zoo.add_animal("Bear")
my_zoo.add_animal("Cat")
my_zoo.add_animal("Cougar")
my_zoo.add_animal("Giraffe")
my_zoo.add_animal("Lion")
my_zoo.add_animal("Zebra")

 
my_zoo.add_animal("Bear")

 
my_zoo.get_animals()

 
my_zoo.sell_animal("Giraffe")


my_zoo.get_animals()

 
my_zoo.get_groups()
 