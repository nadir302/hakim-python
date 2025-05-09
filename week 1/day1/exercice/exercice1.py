## exercice1
print("hello word")

print("hello word")

print("hello word")

print("hello word")



## exercice2 
8*(3^99)


## exer3

 
my_name = "hakim"

 
user_name = input("What's your name? ").strip().capitalize()

 
if user_name == my_name:
    print(f"Whoa! We have the same name, {user_name}! 🎉 Are you me from an alternate universe?")
else:
    print(f"Hi {user_name}! Cute name, but I still prefer '{my_name}' 😏")










    #Exercice4
    
height = int(input("What is your height in centimeters? "))

 
if height > 145:
    print("You are tall enough to ride!  ")
else:
    print("Sorry, you need to grow some more to ride.  ")










# Exercices 5
my_fav_numbers = {7, 14, 21, 42}

 
my_fav_numbers.add(8)

my_fav_numbers.add(100)

 
my_fav_numbers.pop()
 
friend_fav_numbers = {3, 7, 10, 42}

   
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
 
print("Our favorite numbers:", our_fav_numbers)













#eexercice7

 
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

 
basket.remove("Banana")
 
basket.remove("Blueberries")

 
basket.append("Kiwi")

 
basket.insert(0, "Apples")

 
apple_count = basket.count("Apples")

print(f"There are {apple_count} apples in the basket.")
 
basket.clear()

 
print("Basket:", basket)


