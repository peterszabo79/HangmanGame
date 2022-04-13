# Hangman Game
## 1. Purpose of the project

Hangman is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Users guess the right word by entering the right letters.
Words are chosen from rd.com - hardest spelling words in English. They only have six lives, so they are executed if they guess six times wrong!
![Am I Responsive](/images/imresponsive.jpeg)
for the live site click
[here](https://project3hangman.herokuapp.com/)

---

## 2. How to play
 The user can play this game by entering letters into the terminal. They must guess the letters correctly with no more than six wrong guesses. The word will appear as "----", but if the user guesses the right letter, then the letter will appear instead of "-". When the user enters a letter they have already guessed before, or puts an invalid character, they get a warning and must guess again. The user must guess all the letters in the word to win.
## 3. features
 ### existing features
 - Name input screen 
   - the user must input his name
 ![name input](/images/name.jpeg)

 - Welcome screen
   - Welcome the user and explain the game rules
![welcome screen](/images/welcome.jpeg)

 - The winning screen
   - congratulate the user
   - ask for a new game
  ![win](/images/win.jpeg)

 - The lost screen  
   - tell user, had too many wrong guesses
   - show the correct word 
   - ask for a new game
   ![lost](/images/lost.jpeg)
 
 - The wrong input screen
   - ask user to use only lowercase letters
   - tell user if already select a letter
  ![wrongcaracter](/images/wrong.jpeg)

### Features Left to Implement
- Wish to add levels -easy-medium-hard to the words, let the user make a choice

## 4. Technology
These are the Technology I used for this project.
- Python
- Gitpod
- Github
- Heroku
- Grammarly
- Google


---

# Testing
I have tested this project by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems.
![pep8](/images/pep8.jpeg)
- Given invalid inputs.
- Same input twice.
- Given uppercase letter.
- Tested in my local terminal and the Code Institute Heroku terminal.

# Bugs
- When I passed my code on the PEP8 online checker, run into multiple warnings.
They are fixed now.
  - E501 - line too long
  - W291 - trailing whitespace
  - W293 - blank line contains whitespace
  - E302 - expected 2 blank  lines, found 1



# Deployment
This game was deployed to GitHub pages :

### Gitpod

1. In gitpod workspaces
2. I choose the right workspace/repo
3. Now I can write my code and readme
4. To save my code I Type in the terminal: git add.
5. I type git commit -m "comment"
6. I type git push to push it to GitHub

### Heroku

1. Fork or clone this repository.
2. requirements.txt can be left empty as this project does not use any external libraries.
3. Create a new app in Heroku.
4. Select "New" and "Create new app".
5. Name the new app and click "Create new app".
6. In "Settings" select "BuildPack" and select Python and Node.js.
7. Whilst still in "Settings", click "Reveal Config Vars" and input the folloing. KEY: PORT, VALUE: 8000. Nothing else is needed here as this project does not have any sensitive files.
8. Click on "Deploy" and select your deploy method and repository.
9. Click "Connect" on selected repository.
10. choose "Deploy Branch" in the manual deploy section.
11. you can choose "Enable Automatic Deploys" if you want.
10. Heroku will now deploy the site.

# Credits
<details>
<li>my mentor Spencer Barriball
</li>
<li>inwentinpython.com site helped me from the beginning through to the finish of my project</li>
<li>My cohort channel helped in fixing typing errors, and give me support on my hard days.</li>
<li>stackoverflow.com helped me from the beginning through to the finish of my project</li>
<li>My second project - The Doors Quiz helped me for writing my README. </li>
<li>Slack  #peer-code-review helped me writing my README.</li>
<li>rd.com - for my secret words</li>
</details>