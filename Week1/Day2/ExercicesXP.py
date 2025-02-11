
# #1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Dictionaries = dict(zip(keys, values))

# print(Dictionaries)

# #2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# total_cost = 0

# for member, age in family.items():
#     if age < 3:
#         cost = 0
#     elif 3 <= age <= 12:
#         cost = 10
#     else:
#         cost = 15

#     print(f"{member.capitalize()} has to pay ${cost}.")
#     total_cost += cost

# print(f"The total cost for the family is: ${total_cost}")

# family = {}
# total_cost = 0
# num_members = int(input("How many family members are there? "))

# for i in range(num_members):
#     name = input("Enter the family member's name: ")
#     age = int(input(f"Enter {name}'s age: "))
#     family[name] = age

# for member, age in family.items():
#     if age < 3:
#         cost = 0
#     elif 3 <= age <= 12:
#         cost = 10
#     else:
#         cost = 15

#     print(f"{member.capitalize()} has to pay ${cost}.")
#     total_cost += cost

# print(f"The total cost for the family is: ${total_cost}")

#3
# 1.
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

# 2.
brand["number_stores"] = 2
print(brand)

# 3.
clients = ", ".join(brand["type_of_clothes"])
print(f"Zara's clients are {clients}.")

# 4.
brand["country_creation"] = "Spain"

# 5. Check if the key international_competitors is in the dictionary. If it is, add Desigual.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 6. Delete the information about the date of creation
del brand["creation_date"]

# 7. Print the last international competitor
print(f"The last international competitor is: {brand['international_competitors'][-1]}.")

# 8. Print the major clothes colors in the US
print(f"The major clothes colors in the US are: {', '.join(brand['major_color']['US'])}.")

# 9. Print the amount of key-value pairs (length of the dictionary)
print(f"The number of key-value pairs in the brand dictionary is: {len(brand)}.")

# 10. Print the keys of the dictionary
print(f"The keys in the brand dictionary are: {list(brand.keys())}.")

# 11. Create another dictionary called more_on_zara
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# 12. Update the brand dictionary with more_on_zara
brand.update(more_on_zara)

# 13. Print the value of the key number_stores
print(f"The updated number of stores is: {brand['number_stores']}.")

# #4
# def describe_city(city, country="France"):
#     """Prints a simple sentence stating the city and its country."""
#     print(f"{city} is in {country}.")

# # Calling the function with different arguments

# # Using the default country (USA)
# describe_city("New York","USA")

# # Specifying the country explicitly
# describe_city("Reykjavik", "Iceland")
# describe_city("Tokyo", "Japan")
# describe_city("Paris")

# #5
# import random

# def guess_number(user_number):
#     """Compares the user's number with a randomly generated number between 1 and 100."""
    
#     if not 1 <= user_number <= 100:
#         print("Please enter a number between 1 and 100.")
#         return

#     random_number = random.randint(1, 100)

#     if user_number == random_number:
#         print(f"Congratulations! You guessed it right. The number was {random_number}. 🎉")
#     else:
#         print(f"Sorry, you guessed {user_number}, but the correct number was {random_number}. Try again!")

# # Example calls:
# guess_number(25)  # Replace 25 with any number you'd like to test

# #6
# def make_shirt(size, message):
#     """Prints a summary of the shirt size and the message to be printed on it."""
#     print(f"The size of the shirt is {size} and the text is '{message}'.")

# # Calling the function
# make_shirt("Medium", "Code is life!")

# def make_shirt(size="Large", message="I love Python"):
#     """Prints a summary of the shirt size and the message, with default values."""
#     print(f"The size of the shirt is {size} and the text is '{message}'.")

# # 1. Make a large shirt with the default message
# make_shirt()

# # 2. Make a medium shirt with the default message
# make_shirt(size="Medium")

# # 3. Make a shirt of any size with a different message
# make_shirt(size="Small", message="Keep Calm and Code On!")

# # Using keyword arguments to call the function
# make_shirt(message="Eat, Sleep, Code, Repeat!", size="Extra Large")

# #7
# import random

# def get_random_temp(season=None):
#     """Returns a random temperature based on the season."""
#     if season == "winter":
#         temp = random.uniform(-10, 16)
#     elif season == "spring":
#         temp = random.uniform(5, 22)
#     elif season == "summer":
#         temp = random.uniform(20, 40)
#     elif season == "autumn" or season == "fall":
#         temp = random.uniform(10, 25)
#     else:
#         # Default range if no season provided
#         temp = random.uniform(-10, 40)
    
#     return round(temp, 2)  # Return a floating-point number rounded to 2 decimal places


# def determine_season(month):
#     """Determines the season based on the month number."""
#     if month in [12, 1, 2]:
#         return "winter"
#     elif month in [3, 4, 5]:
#         return "spring"
#     elif month in [6, 7, 8]:
#         return "summer"
#     elif month in [9, 10, 11]:
#         return "autumn"
#     else:
#         return None


# def main():
#     """Main function to display the temperature and provide advice."""
    
#     # Bonus: Ask for the month instead of season
#     try:
#         month = int(input("Please enter the number of the month (1 = January, 12 = December): "))
#         if month < 1 or month > 12:
#             print("Invalid month. Please enter a number between 1 and 12.")
#             return
#     except ValueError:
#         print("Invalid input. Please enter a number.")
#         return

#     # Determine the season based on the month
#     season = determine_season(month)
#     print(f"The detected season is {season.capitalize()}.")

#     # Get the temperature for the given season
#     temp = get_random_temp(season)

#     # Display the temperature
#     print(f"The temperature right now is {temp} degrees Celsius.")

#     # Provide friendly advice based on the temperature
#     if temp < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today!")
#     elif 0 <= temp <= 16:
#         print("Quite chilly! Don’t forget your coat.")
#     elif 17 <= temp <= 23:
#         print("It's a pleasant day, enjoy the weather!")
#     elif 24 <= temp <= 32:
#         print("It's warm outside, stay hydrated!")
#     elif 33 <= temp <= 40:
#         print("It's really hot! Make sure to wear sunscreen and stay cool.")
#     else:
#         print("Unusual temperature detected! Stay prepared.")

# # Run the program
# main()

# #8
# def start_quiz():
#     data = [
#         {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
#         {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
#         {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
#         {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
#         {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
#         {"question": "What species is Chewbacca?", "answer": "Wookiee"}
#     ]
    
#     correct_answers = 0
#     wrong_answers = []

#     print("🌟 Welcome to the Star Wars Quiz! 🌟\n")
    
#     # Loop through each question
#     for item in data:
#         user_answer = input(item["question"] + " ").strip()

#         if user_answer.lower() == item["answer"].lower():
#             print("✅ Correct!\n")
#             correct_answers += 1
#         else:
#             print(f"❌ Incorrect! The correct answer was '{item['answer']}'.\n")
#             wrong_answers.append({
#                 "question": item["question"],
#                 "your_answer": user_answer,
#                 "correct_answer": item["answer"]
#             })

#     # Display the results
#     display_results(correct_answers, len(data) - correct_answers, wrong_answers)

#     # If more than 3 wrong answers, ask to replay
#     if len(wrong_answers) > 3:
#         play_again = input("\nYou had more than 3 wrong answers. Would you like to try again? (yes/no): ").strip().lower()
#         if play_again == 'yes':
#             start_quiz()
#         else:
#             print("Thanks for playing! May the Force be with you. ✨")
#     else:
#         print("Great job! Thanks for playing! 🚀")


# def display_results(correct, incorrect, wrong_answers):
#     print("🎉 Quiz Results 🎉")
#     print(f"Correct Answers: {correct}")
#     print(f"Incorrect Answers: {incorrect}\n")

#     if wrong_answers:
#         print("Here are the questions you got wrong:\n")
#         for item in wrong_answers:
#             print(f"❓ {item['question']}")
#             print(f"   Your answer: {item['your_answer']}")
#             print(f"   Correct answer: {item['correct_answer']}\n")


# # Start the quiz
# start_quiz()


def testdedef(a,b):
    return a, b
c= testdedef(1, 3)[0]
print(c)
