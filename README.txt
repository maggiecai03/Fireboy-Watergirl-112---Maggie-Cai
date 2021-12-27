#Project Video Link
https://youtu.be/pUGPoZhaBho

#Project Description 
Project Name: Fireboy Watergirl 112 
Based on the original game "Fireboy & Watergirl," "Fireboy Watergirl 112" is a
collaborative game featureing two players. To pass a level of the game, 
both players, starting at the bottom of the game screen, have to work together 
through obstacles to reach the top where the exits are located.

#Project Components: 
Fireboy is red and Watergirl is blue.
Water, lava, and green goop liquids on the board can either cause death for the players or not.
Diamonds are scattered around the board for the characters to collect. The characters can only collect the diamonds that correspond to their own colors
A timer shows the total time it takes for the two players to reach the end of the game.
Blocks are available for the players to move around and help them navigate the board
Exits are placed at the top of the board where both players have to be on to pass the level
The purple platform blocks the path to the exit. The players must collaboratively use the purple buttons to help the other player pass the purple platform in order to reach the exit
Gravity exists for the players and the blocks. 

1. Easy Mode: This mode is a fixed board that allows newcomers to be accustomed to the game 
2. Random Mode: This mode randomly generates all the pieces on the board and can vary in difficulty. 
3. AI Mode: The mode creates an AI alien that both players need to beat. The AI's exit will be placed between the two players' exits. Using A* algorithm, the best path for the alien to reach its exit is calculated. AI mode will be used on the fixed board or a randomly generated board. 


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
