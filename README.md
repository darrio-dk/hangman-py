# Hangman

This game Hangman is build using Python terminal, which runs in the code Institute mock terminal on Heroku.

This game is simply fun to give your free time and have a bit of fun in guessing words, suitable to play for teenagers and above. Firstly this game started on a piece of paper using pen.

![Alt text](<Screenshot (282).png>)

## How to play

In this game version in the begining the user enters their name, than word will be generated for guessing.

![Alt text](<Screenshot (288).png>)

Player can choose any letter he wants to make his first guess. If a letter is correct it will be displayed on the underscore symbol of the word.

![Alt text](<Screenshot (289).png>)

If the player chooses incorret letter when it will be displayed in missed guesess section.

User will have 6 guesses to pick the right word, if the player already knows what word is hiding behind, than the correct letters can be entered and no guesses "lives" will be lost.

However if the player uses all the guesses and collects all the "Hangman" pieces then the game is over, however if you are feeling lucky you can hit that y(yes) button to start the game again, or just take a break by pressing n(no) and come back later.

More in detail about Hangman game you can find here on Wikipedia - [Hangman game](https://en.wikipedia.org/wiki/Hangman_(game))

## Technologies used

### Languages

- Python

### Python Modules 

- colorama - add colour to the title of the game 
- random - selected random words

### Frameworks, Libraries & Programs

- Github - Repository to store saved project files
- Gitpod - Project workspace
- Heroku - Website for deployment

# Testing

I have manually tested this project by using PEP8 linter
- Passed all the codes through CI Python Linter 

![Alt text](<Screenshot (525) python.png>)

# Bugs

### Solved Bugs

- When running test with PEP8 were getting bugs like E221, E225, E501, W391, E272.

- All the bugs fixed by searcing what do the error code means on engine google.

# Remaining bugs 
- No bugs remaining

### Validator testing
- PEP8

# Deployment
- Login to Heroku
- Select 'Create New App'
- Pick a unique name for application
- On the settings tab select 'Add Buildpack'
- From Buidpack choose to add Python and Node.js
- Python selected first and Node.js second as needs to be in order
- Next go to Deploy page tab and chooose Github
- Connect your repository name
- Select to deploy manually or automatically
- A link to the deployed page can be seen once deployment is complete

# Credits
PEP8 bugs fixed using:
- [Python.org](https://discuss.python.org/)
- [W3Schools](https://www.w3schools.com/)

Extra knowledge picked from:

- [StackOverflow](https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python)
- [Rhino Developer](https://developer.rhino3d.com/guides/rhinopython/python-statements/) 

Inspiration research tutorials (youtube):

- [Link](https://www.youtube.com/watch?v=MtYw0RaZ4B0)
- [Link](https://www.youtube.com/watch?v=pFvSb7cb_Us)