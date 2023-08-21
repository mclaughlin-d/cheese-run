# cheese-run
A simple python game where you play as a mouse collecting cheese.

## Basic Gameplay
There is one level that increases in difficulty the longer it is played. To move from the start screen to the gameplay, press the space bar. The key to jump (the only action performed during gameplay) is also the space bar. Once gameplay ends (when the mouse collides with an obstacle), the score can be entered by typing a name in the text box entry and hitting the 'enter' key. To move back to the start screen, press the right arrow key. To quit the application, either press the 'esc' key or the red x in the top right corner of the window. 

## Installation/Execution Instructions
### Running in VS Code
If you have VS Code and you download the repository, all you need to do is run the game.py file in the cheese-run directory.

### Using the setup.py file
You can use the setup.py file to build the project package and execute it with the 'cheese-run-cli' command. In summary, you activate a virtual python environment with venv, navigate to the cheese-run directory on your machine, and type 'pip install .', which will build the project. Then you can execute the command. If you are missing the playsound module, you will need to import it with 'pip install playsound'. 

## Libraries/Imports
The only non-standard library import used in this project was the playsound module, which can be installed by running
'pip install playsound' on your machine.
