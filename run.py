# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
#source from inventwithpython.com
HANGMAN_PICS = ['''
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

# Add words to the game 
words = 'chthonic phlegm pterodactyl muscle dilate indict mnemonic liquefy asthma apropos receipt knead nauseous honest'.split()

# welcome the user
name = input("What is Your name?")
print ("Hello", name.capitalize(), "let's start playing Hangman!")#name will start with uppercase letter always

# This function returns a random word from the passed list of strings
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    """
    this function defines a  displayBoard. it has three parameters:
    missedLetters A string of the letters the player has guessed that are not in the secret word
    correctLetters A string of the letters the player has guessed that are in the secret word
    secretWord A string of the secret word that the player is trying to guess
    
    """  
    print(HANGMAN_PICS[len(missedLetters)]) # call hangman pics after user choice
    print() 
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter,end=' ')
    print()
