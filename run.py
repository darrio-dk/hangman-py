# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

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
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']


# User enters their name to start the game
#name = input("Please enter your name: ")
#print("Hi",name,"" "lets begin the game")

words = "dog cat eagle lion lizard cow bear donkey tiger bull llama beaver giraffe sheep deer horse rabbit monkey duck hippopotamus wolf camel kangaroo".split()

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
        print(letter, end =' ')
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
            print("You have already chosen that letter. Please choose different one.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please choose a letter from the alphabet")
        else:
            return guess
        

