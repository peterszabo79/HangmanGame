![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome peterszabo79,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

# Hangman Game
## 1. Purpose of the project

### Hangman is a Python terminal game, wich runs in the Code Institute mock terminal on Heroku.

Users guess the right word by entering the right letters.
Words are choosen from rd.com - hardest spelling words in english.They only have six lives, so if they guess six times wrong, they are executed!
for the live site click
![respon](assets/images/respon.jpeg)

---

# Features 
## Existing Features
- Header:
  - This header tells the user what is the name of the game.
  ![respon](assets/images/doors.jpeg)

- The Game Options:
   - 13 questions each with 3 answers, only one of them is the right one.
  ![respon](assets/images/question.jpeg)

 - The Game Results:  
   - Shows how many right answer from the 13 questions.
   - No answer = wrong answer
   - 5 minutes timer, but can finish the quiz after it's run out.

     ![1](assets/images/1.jpeg) 
     ![2](assets/images/13.jpeg)
     ![3](assets/images/timer.jpeg)

- The Footer:
   - a link to the doors website opens in a new tab

## Features Left to Implement
- When there is time, I would like to expand this game, with a timer that can finish the game if 5 minutes it's gone, random questions etc.

## Design
- Color Scheme:
  - Used color are:
     - Black
     - Grey
     - Lightgrey
     - Whitesmoke

- Typography:
  - The fonts used are taken from google fonts named 'Roboto' and 'Rubik' with a fall-back of sans-serif.


---

# Testing
- I tested playing this game in different browsers: Chrome, Safari, Firefox, Opera.
- I confirmed that the game is counting the right answers always correctly.
- I confirmed that the colours and fonts chosen are easy to read and accessible by running it through lighthouse in dev tools.
- I confirmed that the timer shows a message when 5 minutes are gone.

![1](assets/images/time%20out.jpeg)



---

# Validator Testing
- HTML
  - No errors were returned when passing through the official W3C validator.

- CSS
  - No errors were returned when passing through the official (Jigsaw) validator.

- JS:
  - No errors were returned when passing through the JSHint validator, but I have warnings.

- Accessibility
  - I confirmed that the colours and fonts chosen are easy to read and accessible by running it through Lighthouse in Devtools.


### Desktop 

![](assets/images/dtop.jpeg)

### Mobile 

![](assets/images/mobil.jpeg)

---

# Deployment
- The site was deployed to GitHub Pages. The steps to deploy are the follows:
  - In the Github repository, navigate to the Settings tab.
  - Scroll down to Pages and click on it.
  - Select Main Branch and click Save.
  - The page provides a link to the completed website.

The live link can be found here - [The Doors Quiz](https://peterszabo79.github.io/project-no2/index.html)


---

# Git & GitHub
I used GitPod as a local repository and IDE and GitHub as a remote repository. The process was:
  1. First i created a new repository on GitHub.
  2. I have then opened that repository on GitPod and started coding.
  3. In GitPod i have created all the pages and and folders.
  4. I was then saving my work and pushing it to GitHub repository to keep it safe.

Process for saving, commiting and pushing it to remote repository goes as follows (done in terminal):


 - `git add .` for adding work to git


 - `git commit -m "+ commit message"` to commit the work on the stage


 - `git push` to update work to GitHub

---

# Issues
 - I got warnings when I was passing through the code the JSHint validator.On stackoverflow.com found ` /*jshint esversion: 6 */ ` fixed most of them. but still have three warnings.

# Credits
<details>
<li>The "How to Make a Simple JavaScript Quiz" from sitepoint.com Walkthrough Project helped me from the beginning through to the finish of my project
</li>
<li>Wikipedia - correct answers can be found on wikipedia.</li>
<li>My cohort channel helped in fixing typing errors.</li>
<li>Google Fonts was used to choose my fonts, Roboto and Rubik.</li>
<li>Gitpod “Tips and Tricks” used during writing my project.</li>
<li>W3School was used while writing my project.</li>
<li>developer.mozilla.org was used while writing my project.</li>
<li>Grammarly was used to correct my text.</li>
<li>web.dev was used to test and improve UX.</li>
<li>Chrome Devtools was used for fixing my code all the way through my project.</li>
<li>My first project - Peter's Garage helped me for writing my README. </li>
<li>The Code Institute “rock-paper-scissor” Walkthrough Project helped me for writing my README.</li>
<li>Timer from "yo.fun"</li>
</details>