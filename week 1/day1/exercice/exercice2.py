#exercice1
month = int (input("entre your month(1-12):"))

if 3 <= month <=5:
    print("sprint")
elif 6 <=month <=8:
    print("summer") 
elif 9 <= month <= 11:
    print("autumn") 
else:
    print("winter")       

    #exercice2 
     
print("All numbers from 1 to 20:")
for i in range(1, 21):
    print(i)

 
print("\nNumbers at even indexes (values that are odd):")
for idx, num in enumerate(range(1, 21)):
    if idx % 2 == 0:
        print(num)
  # exercice3     
my_name = "Alice"  # Replace with your actual name

while True:
    user_input = input("What is your name? ")
    if user_input == my_name:
        print("Matched! Exiting loop.")
        break
 #exercice4
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter your name: ")

if user_name in names:
    index = names.index(user_name)
    print(f"The index of the first occurrence of '{user_name}' is: {index}")
else:
    print("Name not found in the list.") 
 #exercice5
num1 = float(input("Input the 1st number: "))
num2 = float(input("Input the 2nd number: "))
num3 = float(input("Input the 3rd number: "))

greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")
#exercice6
import random

games_won = 0
games_lost = 0

while True:
    try:
        user_guess = input("Guess a number from 1 to 9 (type 'q' to quit): ")
        if user_guess.lower() == 'q':
            break
        user_guess = int(user_guess)
        if user_guess < 1 or user_guess > 9:
            print("Invalid input. Please pick a number between 1 and 9.")
            continue

        random_num = random.randint(1, 9)

        if user_guess == random_num:
            print("Winner!")
            games_won += 1
        else:
            print(f"Better luck next time. The number was {random_num}.")
            games_lost += 1

    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")

 
print("\nGame Summary:")
print(f"Games won: {games_won}")
print(f"Games lost: {games_lost}")

 