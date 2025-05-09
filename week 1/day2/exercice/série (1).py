#exercice1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

 
result_dict = dict(zip(keys, values))

print(result_dict)
 # exerice2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{name.capitalize()} has to pay ${cost}")
    total_cost += cost

print("Total family cost:", "$" + str(total_cost))
family = {}
while True:
    name = input("Enter family member's name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    try:
        age = int(input(f"Enter {name}'s age: "))
        family[name] = age
    except ValueError:
        print("Please enter a valid age.")
#exercice4
 
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

 
brand["number_stores"] = 2

 
clothes_clients = ", ".join(brand["type_of_clothes"])
print(f"Zara's clients are: {clothes_clients}.")

 
brand["country_creation"] = "Spain"
 
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

 
del brand["creation_date"]
 
print("Last international competitor:", brand["international_competitors"][-1])

 
print("Major clothes colors in the US:", brand["major_color"]["US"])
 
print("Number of key-value pairs:", len(brand))

 
print("Keys in the dictionary:", list(brand.keys()))

 
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

 
brand.update(more_on_zara)

 
print("Updated number of stores:", brand["number_stores"])
#exercice 5
import random

def compare_number(user_num):
    rand_num = random.randint(1, 100)
    if user_num == rand_num:
        print("Success! You guessed it right!")
    else:
        print(f"Oops! You guessed {user_num}, but the correct number was {rand_num}.")
        import random

def compare_number(user_num):
    rand_num = random.randint(1, 100)
    if user_num == rand_num:
        print("Success! You guessed it right!")
    else:
        print(f"Oops! You guessed {user_num}, but the correct number was {rand_num}.")

#exercice6

        def make_shirt(size="large", text="I love Python"):
         print(f"The size of the shirt is {size} and the text is '{text}'.")

 
make_shirt()

 
make_shirt("medium")

 
make_shirt("small", "Python Rocks!")

 
make_shirt(text="Hello World", size="XL")



#EXERCICE8
data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

def run_quiz(questions):
    correct = 0
    wrong_answers = []

    for q in questions:
        user_answer = input(q["question"] + " ").strip()
        if user_answer.lower() == q["answer"].lower():
            correct += 1
        else:
            wrong_answers.append({
                "question": q["question"],
                "user_answer": user_answer,
                "correct_answer": q["answer"]
            })

    return correct, wrong_answers

def show_results(correct, wrong):
    print(f"\nYou got {correct} correct answers.")
    print(f"You got {len(wrong)} wrong answers.")
    
    if wrong:
        print("\nHere are the questions you answered incorrectly:")
        for entry in wrong:
            print(f"Question: {entry['question']}")
            print(f"Your answer: {entry['user_answer']}")
            print(f"Correct answer: {entry['correct_answer']}\n")

    if len(wrong) > 3:
        print("You had more than 3 wrong answers. Would you like to play again?")

 
correct, wrong = run_quiz(data)
show_results(correct, wrong)

 