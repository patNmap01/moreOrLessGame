import random

def main():
    print("Welcome to the game!")
    print("You have 3 tries to guess the number")
    print("The number is between 1 and 10")
    print("Good luck!")

    number = random.randint(1,10)
    tries = 3

    while tries > 0:
        guess = int(input("Guess the number: "))
        if guess == number:
            print("You guessed it!")
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")
        tries -= 1
    else:
        print("You lost!")
        print("The number was", number)

main()