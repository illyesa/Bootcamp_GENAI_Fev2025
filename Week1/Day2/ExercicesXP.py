
#1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Dictionaries = dict(zip(keys, values))

print(Dictionaries)

#2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for member, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    print(f"{member.capitalize()} has to pay ${cost}.")
    total_cost += cost

print(f"The total cost for the family is: ${total_cost}")

family = {}
total_cost = 0
num_members = int(input("How many family members are there? "))

for i in range(num_members):
    name = input("Enter the family member's name: ")
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age

for member, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    print(f"{member.capitalize()} has to pay ${cost}.")
    total_cost += cost

print(f"The total cost for the family is: ${total_cost}")

#3
## 1.
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

## 2.
brand["number_stores"] = 2
print(brand)

## 3.
clients = ", ".join(brand["type_of_clothes"])
print(f"Zara's clients are : {clients}.")

## 4.
brand["country_creation"] = "Spain"

## 5.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

## 6.
del brand["creation_date"]

## 7.
print(f"The last international competitor is: {brand['international_competitors'][-1]}.")

## 8.
print(f"The major clothes colors in the US are: {', '.join(brand['major_color']['US'])}.")

## 9.
print(f"The number of key-value pairs in the brand dictionary is: {len(brand)}.")

## 10.
print(f"The keys in the brand dictionary are: {list(brand.keys())}.")

## 11.
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

## 12.
brand.update(more_on_zara)

## 13.
print(f"The updated number of stores is: {brand['number_stores']}.")


#4
def describe_city(city, country="France"):
    print(f"{city} is in {country}.")
describe_city("Madrid","Spain")
describe_city("Marseille", "France")
describe_city("Tokyo", "Japan")
describe_city("Paris")

#5
import random

def guess_number(user_number=int(input("Chose a number: "))):
    if not 1 <= user_number <= 100:
        print("Enter a number between 1 and 100.")
        return
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print(f"Congratulations! You guessed it right. The number was {random_number}.")
    else:
        print(f"Sorry, you guessed {user_number}, but the correct number was {random_number}. Try again!")
guess_number()

#6
def make_shirt(size, message):
    print(f"The size of the shirt is {size} and the text is '{message}'.")
make_shirt("Medium", "Code is life!")

def make_shirt(size="Large", message="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{message}'.")

make_shirt()
make_shirt(size="Medium")
make_shirt(size="Small", message="Message")
make_shirt(message="Message2", size="Medium")

#7
import random

def get_random_temp(season=None):
    if season == "summer":
        temp = random.uniform(20, 40)
    elif season == "autumn" or season == "fall":
        temp = random.uniform(10, 25)
    elif season == "spring":
        temp = random.uniform(5, 22)
    elif season == "winter":
        temp = random.uniform(-10, 16)
    else:
        temp = random.uniform(-10, 40)
    return round(temp, 2)

def determine_season(month):
    if month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    elif month in [1, 2, 12]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    else:
        return None

def main():
    try:
        month = int(input("Please enter the number of the month (1 = January, 12 = December): "))
        if month < 1 or month > 12:
            print("Invalid month. Please enter a number between 1 and 12.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    season = determine_season(month)
    print(f"The detected season is {season.capitalize()}.")
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today!")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 17 <= temp <= 23:
        print("That ok")
    elif 24 <= temp <= 32:
        print("It's warm")
    elif 33 <= temp <= 40:
        print("HOT")
    else:
        print("Hardcore mode actived (you don't know the weather)")

main()

#8
def start_quiz():
    data = [
        {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
        {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
        {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
        {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
        {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
        {"question": "What species is Chewbacca?", "answer": "Wookiee"}
    ]
    
    correct_answers = 0
    wrong_answers = []

    print("Star Wars Quiz!")
    for item in data:
        user_answer = input(item["question"]).strip()

        if user_answer.lower() == item["answer"].lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect! The correct answer was '{item['answer']}'.")
            wrong_answers.append({"question": item["question"], "your_answer": user_answer, "correct_answer": item["answer"]})

    display_results(correct_answers, len(data) - correct_answers, wrong_answers)

    if len(wrong_answers) > 3:
        play_again = input("More than 3 wrong answers. Would you like to try again? (yes/no): ").strip().lower()
        if play_again == "yes":
            start_quiz()
        elif play_again == "no" :
            print("Maybe next time")
        else:
            print("You don't chose yes or no, bye")
    else:
        print("GG")


def display_results(correct_answers, incorrect_answers, wrong_answers):
    print("Results")
    print(f"Correct Answers: {correct_answers}")
    print(f"Incorrect Answers: {incorrect_answers}")

    if wrong_answers:
        print("Here the questions you got wrong:")
        for item in wrong_answers:
            print(f"{item['question']}")
            print(f"Your answer: {item['your_answer']}")
            print(f"Correct answer: {item['correct_answer']}")

start_quiz()
