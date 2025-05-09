# exercice1
birthdays = {
    "Alice": "1990/05/12",
    "Bob": "1985/09/23",
    "Charlie": "2001/07/14",
    "Diana": "1998/03/30",
    "Ethan": "2005/11/05"
}

 
print("Welcome! You can look up the birthdays of the people in the list!")

 
name = input("Enter a person's name: ").strip()

 
birthday = birthdays.get(name, "not found")
if birthday != "not found":
    print(f"{name}'s birthday is on {birthday}.")
else:
    print("Sorry, we don't have the birthday information for that person.")
#  exercice2
birthdays = {
    "Alice": "1990/05/12",
    "Bob": "1985/09/23",
    "Charlie": "2001/07/14",
    "Diana": "1998/03/30",
    "Ethan": "2005/11/05"
}

 
print("You can look up the following names:")
for name in birthdays:
    print("-", name)

 
name = input("Enter a person's name: ").strip()

 
birthday = birthdays.get(name)
if birthday:
    print(f"{name}'s birthday is on {birthday}.")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")  
#exercice3
def calculate_sum(X):
     
    X_str = str(X)
    total = int(X_str) + int(X_str * 2) + int(X_str * 3) + int(X_str * 4)
    return total

 
print(calculate_sum(3))       
 #exercice4
import random

 
def throw_dice():
    return random.randint(1, 6)

 
def throw_until_doubles():
    count = 0
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        count += 1
        if die1 == die2:
            return count

 
def main():
    total_throws = 0
    results = []

    for _ in range(100):
        throws_needed = throw_until_doubles()
        total_throws += throws_needed
        results.append(throws_needed)

    average = round(total_throws / 100, 2)

    print(f"\nTotal throws to get 100 doubles: {total_throws}")
    print(f"Average throws per double: {average}")

 
main()
