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