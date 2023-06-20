# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


HANGMAN_PICTURES = ['''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\\  |
        |
       ===''', '''
    +---+
    O   |
   /|\\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\\  |
   / \\  |
       ===''']


# User enters their name to start the game
name = input("Welcome to Hangman game, please enter your name: ")
print("Hi", name, "" "lets begin the animal guessing game")
print("Rules are simple guess a letter each "
      "time to find out what animal name is hiding")
print("You will have 6 guesses in total, "
      "lets have some fun in gueesing animal words - Let's go :)")

words = "dog cat eagle lion lizard cow bear donkey tiger bull llama beaver" \
        "giraffe sheep deer horse rabbit monkey duck hippopotamus wolf camel" \
        "kangaroo wolf fox lion flamingo bat gorilla".split()


def getRandomWord(wordList):
    """
    Generates a random word from the past list of strings.
    """
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print()
    print(HANGMAN_PICTURES[len(missedLetters)])

    print()
    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')

    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    # Display the secret word with spaces between the letters:
    for letter in blanks:
        print(letter, end=' ')
    print()


def getGuessWord(alreadyGuessed):
    """
    Generates the letter the player have entered.
    Checks the player enters unique letter.
    """
    while True:
        print("Please choose your letter")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Only a single letter is allowed.")
        elif guess in alreadyGuessed:
            print("You have already chosen that letter. Choose different one.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please choose a letter from the alphabet")
        else:
            return guess


def repeatGame():
    """
    If the player chooses "yes" option returns True
    and the game starts again, returns false if "no"
    option picked
    """
    print("Would you like continue playing choose 'y' for yes or 'n' for no")
    return input().lower().startswith('y')


print(Fore.RED + '|_H_A_N_G_M_A_N_|')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsOver = False

# game
while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # Gives the player option to enter the letter:
    guess = getGuessWord(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check to see if the player has won:
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('You guessed it!')
            print('The secret word is "' + secretWord + '"! You win!')
            gameIsOver = True
    else:
        missedLetters = missedLetters + guess

        # Check if the player has guessed too many times and lost.

        if len(missedLetters) == len(HANGMAN_PICTURES)-1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of\
            guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses\
            and ' + str(len(correctLetters)) + ' correct guesses, the word\
            was "' + secretWord + '"')
            gameIsOver = True

    # If the game is over, ask the player to try again.
    if gameIsOver:
        if repeatGame():
            missedLetters = ''
            correctLetters = ''
            gameIsOver = False
            secretWord = getRandomWord(words)
        else:
            break
