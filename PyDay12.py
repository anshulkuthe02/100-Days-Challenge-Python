## Number Guessing Game
import random
##print(com_guess)
def guess_game():
    turns_e = 10; turns_h = 5
    if mode == 'e' or mode == 'E':
        while turns_e > 0:
            user_input = int(input("Enter your number: "))
            if user_input == com_guess:
                print("Congrats!! You've WON")
                break
            elif user_input < com_guess:
                print("Too low! Try Again")
                turns_e -= 1
                print(f"Lives left: {turns_e}")
            elif user_input > com_guess:
                print("Too high! Try Again")
                turns_e -= 1
                print(f"Lives left: {turns_e}")

            if turns_e == 0:
                print("Lives Over!! You LOST")

    elif mode == 'h' or mode == 'H':
        while turns_h > 0:
            user_input = int(input("Enter your number: "))
            if user_input == com_guess:
                print("Congrats!! You've WON")
                break
            elif user_input < com_guess:
                print("Too low! Try Again")
                turns_h -= 1
                print(f"Lives left: {turns_h}")
            elif user_input > com_guess:
                print("Too high! Try Again")
                turns_h -= 1
                print(f"Lives left: {turns_h}")

            if turns_h == 0:
                print("Lives Over!! You LOST")
                print(f"The number was {com_guess}")
    else:
        print("You've entered a wrong  keyword! Please try again")

print("Welcome to Number Guessing Game!")
mode = input("Press 'e' for EASY or 'h' for HARD: ")
com_guess = random.randint(0,100)
guess_game()