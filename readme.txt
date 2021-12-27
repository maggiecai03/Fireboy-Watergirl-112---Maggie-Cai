#Project Description 
Project Name: Fireboy Watergirl 112 
Based on the original game "Fireboy & Watergirl," "Fireboy Watergirl 112" is a
collaborative game featureing two players. To pass a level of the game, 
both players, starting at the bottom of the game screen, have to work together 
through obstacles to reach the top where the exits are located.


#How to run the project 
Run this file: TP_main.py


#Needed installations
This project requires python3, pygame, and cmu_112_graphics (tkinter)

For windows installation of pygame, enter this prompt into the Command Prompt:
                py -m pip install -U pygame --user

#Shortcut commands
- 'g': Moves both fireboy and watergirl to the center of the screen.
       Helpful for testing the purple platforms.
- 'h': Moves both fireboy and watergirl to the top of the screen
       Helpful for reaching the exits/passing the level 
- 'z': Automatically wins the game and shows the game win screen
- 'x': Automatically loses the game and shows the game over screen
- 'm': Restarts entire game. Goes back to the opening screen.
- 'p': Resets the characters and diamonds for a specific level


Additional Notes: 
This project uses the A* algorithm to generate the best path for an AI player.
When running the AI modes, it may take some time to boot up