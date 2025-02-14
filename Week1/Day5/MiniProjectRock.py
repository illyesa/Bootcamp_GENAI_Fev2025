
# game.py
import random

class Game:
    def get_user_item(self):
        choices = {"r": "rock", "p": "paper", "s": "scissors", "rock": "rock", "paper": "paper", "scissors": "scissors"}
        user_input = ""
        while user_input not in choices:
            user_input = input("Select (r)ock, (p)aper, or (s)cissors: ").lower()
            if user_input not in choices:
                print("Wrong chose")
        return choices[user_input]

    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "scissors" and computer_item == "paper") or \
             (user_item == "paper" and computer_item == "rock"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You chose {user_item}. The computer chose {computer_item}. Result: {result}")
        return result


# rock-paper-scissors.py
# from game import Game
def get_user_menu_choice():
    choices = {"Menu": " ", "g": "Play a new game", "r": "Show scores", "x": "Quit"}
    for key, value in choices.items():
        print(f"{key}. {value}")
    choice = ""
    while choice not in choices:
        choice = input("Choose an option: ").lower()
        if choice not in choices:
                print("Wrong chose")
    return choice


def print_results(results):
    print("\nGame Results:")
    print(f"You won {results['win']} times \nYou Lost {results['loss']} times \nYou drew {results['draw']} times")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "g":
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == "r":
            print_results(results)
        elif choice == "x":
            print_results(results)
            print("\nThank you for playing!")
            break


if __name__ == "__main__":
    main()
