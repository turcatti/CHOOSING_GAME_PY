import random

def choosedGame():

    print("*"*37)
    print("Welcome to the Guess the Number")
    print("*"*37)

    secretNumber = random.randrange(1,101)
    attemptNumber = 0
    round = 1

    print("What level of difficulty?")
    print("(1) Easy (2) Medium (3) Hard")
    level = int(input("Choose the leve of difficulty: "))

    if level == 1:
        attemptNumber = 10
    elif level == 2:
        attemptNumber = 5
    elif level == 3:
        attemptNumber = 3

    for round in range(1, attemptNumber + 1):
        print(f"Attempt {round} of {attemptNumber}")

        guessNumber = int(input("Choose a number between 1 and 100: "))

        if guessNumber < 1 or guessNumber > 100:
            print("Invalid number. Choose a number between 1 and 100.")
            continue

        rightGuess = guessNumber == secretNumber
        bigger = guessNumber > secretNumber
        lower = guessNumber < secretNumber

        if rightGuess:
            print("You nailed it!")
            break
        else:
            if bigger:
                print("You missed! The number is smaller")
                if round == attemptNumber:
                    print("O número secreto era {}.".format(secretNumber))
            elif lower:
                print("You missed! The number is bigger")
                if round == attemptNumber:
                    print("The secret number was {}.".format(secretNumber))

if __name__ == "__main__":
    choosedGame()