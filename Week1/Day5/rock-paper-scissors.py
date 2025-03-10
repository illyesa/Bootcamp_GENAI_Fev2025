
from game import Game
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
