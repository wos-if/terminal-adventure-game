"""
Wasif Kamran
ICS3U
This is the main driver file for the entire project. Here we import the seperate files and initialize attributes and the visited list and call the starting location function. The game works as follows: the user's objective is to maximize their money by winning games and winning the russian roulette at the end location. Each location has smaller mini games that they can win to get more money. The game quits only when they go to the last location and either win or lose the roulette game. 
"""

# Import needed libraries
import os
import sys
import time

# Import files (and their functions) with alises for ease of typing and readability. 
import libs.greetings as greetings 
import libs.characterlore as lore 
import libs.games as games
import libs.locations as locations 
import libs.economy as econ 

# Initialize player attributes such as character, past inflation rates, and the names of games played.
playerAttributes = {
    "character": '', 
    "inflationRates": [], 
    "gamesPlayed": [] 
}

# Initialize the visited list in order to produce different ouputs when the user is revisiting a location. 
visitedList = []

def clearScreen(t):
    """
    This function contains the code to clear the screen after t seconds. 
    Args
        t: int
    Returns
        None 
    """
    # Delay program for t second
    time.sleep(t) 
    # Clear screen
    _ = os.system('clear')

def main(): 
    """
    Main driver function for the entire project. 
    Args
        None
    Returns 
        None
    """
    # Call introduction function from the greetings file
    greetings.introduction()
    
    # Call the accept function from greetings file to see if they want to start the game or not
    # If they choose to continue the game, clear screen after two seconds and proceed. 
    # Otherwise, print a goodbye message and exit the program. 
    if greetings.accept():
        clearScreen(2) 
    else:
        print("Well then, I suppose you still have some sanity in you...")
        sys.exit() 

    # Call the function from lore file to choose a character and place it inside of the attributes dictionary 
    playerAttributes["character"] = lore.chooseChar() 

    # Clear screen after one second
    clearScreen(1) 

    # Initialize the balance and write it to the .txt file based on user choice
    balance = econ.initBalance() 
    
    # Clear screen after one second
    clearScreen(1)

    # Call the starting location function, which then has calls to other locations. 
    locations.launchsite(playerAttributes, visitedList) 

# Driver code 
main()