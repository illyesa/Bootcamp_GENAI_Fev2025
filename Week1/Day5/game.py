
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
