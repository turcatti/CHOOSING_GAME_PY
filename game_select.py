import guessnumber
import hangman

print("*"*37)
print("Choose your game")
print("*"*37)

print("(1) Hangman Game (2) Guess the Number")
choosedGame = int(input("What game do you choose? "))

if choosedGame == 1:
    print("You choosed the Hangman Game")
    hangman.choosedGame()
elif choosedGame == 2:
    print("You choosed the Guess the Number")
    guessnumber.choosedGame()