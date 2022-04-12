import random
import time
# source from inventwithpython.com
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
words = 'chthonic phlegm pterodactyl muscle dilate indict mnemonic\
     liquefy asthma apropos receipt knead nauseous honest'.split()

# welcome the user
name = input("What is Your name?")
print ("Hello", name.capitalize(), "let's start playing Hangman!")
time.sleep(1)

print("The objective of the game is ,\
to guess the secret word chosen by the computer.")
time.sleep(2)

print("You can guess only one letter at a time.Please use only lowercase letters!\
Don't forget to press 'enter key' after each guess.")
time.sleep(3)

print("You have 6 lifes.It's mean, You can miss 6 times.")
time.sleep(2)


# This function returns a random word from the passed list of strings
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):

    """
    this function defines a  displayBoard. it has three parameters:
    missedLetters:A string of the letters the player has guessed
    that are not in the secret word
    correctLetters:A string of the letters the player has guessed
    that are in the secret word
    secretWord:A string of the secret word that the player is trying to guess

    """
    # call hangman pics after user choice
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secretWord)
    # replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    # show the secret word with spaces in between each letter
    for letter in blanks:
        print(letter, end=' ')
    print()


# show the letter what user entered
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LOWERCASE-LETTER.')
        else:
            return guess

"""
playAgain function:must return true if user wants to play again,
otherwise false

"""


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if user win
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes', name.capitalize(),
                  'the secret word is "' + secretWord + '"! Yay! you won!!!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if user guessed too many times and lost
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!Sorry ', name.capitalize(),
                  ' better luck next time.After ' + str(len(missedLetters)) +
                  ' missed guesses and ' + str(len(correctLetters)) +
                  ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
    # Ask user if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
