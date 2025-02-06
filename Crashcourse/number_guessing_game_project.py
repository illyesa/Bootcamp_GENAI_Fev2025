import random


def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attempts = 7
    print(f"Game start you have {max_attempts} to guess the number between 1 and 100")
    for i in range(max_attempts):
        try:
            a=int(input(f"Guess number {i+1} :"))
            if a < random_number:
                print("Too low!")
            elif a > random_number:
                print("Too high!")
            elif a == random_number :
                print(f"GG you find {random_number} in {i+1} guess")
                break
            else :
                print("error")
        except ValueError:
            print("you lose a try because you don't input a number")

    else:
        print(f"FF you lose, you have reached the max attempts : {max_attempts} the good number was {random_number}")

number_guessing_game()    
        

