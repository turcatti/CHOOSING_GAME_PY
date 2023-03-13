def choosedGame():

    print("*"*37)
    print("Welcome to the Hangman Game!")
    print("*"*37)

    secretWord = "banana"

    hanged = False
    rightGuess = False

    # while not hanged and not right guessed, continue the loop
    while not rightGuess and not hanged:
        guessLetter = input("Choose your letter: ")
        guessLetter = guessLetter.strip()

        # if the guessed letter is included in the secret word, it'll print the letter
        # index + 1 will run for each word position and print it's position
        index = 0
        for letter in secretWord:
            if guessLetter.upper() == letter.upper():
                print(f"The letter {guessLetter} is in the {index} position.")
            index = index + 1

if __name__ == "__main__":
    choosedGame()