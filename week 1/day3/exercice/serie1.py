#exercice1
class Cat: 
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 5)
cat3 = Cat("Shadow", 4)

# Step 2: Function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest

# Step 3: Print the oldest cat’s details
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
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# Step 3: Print details and call methods
print(f"{davids_dog.name}, Height: {davids_dog.height}")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name}, Height: {sarahs_dog.height}")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
else:
    print(f"{sarahs_dog.name} is bigger.")
 #exercice3
     