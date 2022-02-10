"""
Wasif Kamran
ICS3U
This file contains the main driver code for the project. 
"""

import os
import sys
import time 

import libs.greetings as greetings 
import libs.characterlore as lore 
import libs.games as games
import libs.locations as locations 
import libs.economy as econ 

attributes = {
    "character": '', 
    "inflationRates": [], 
    "gamesPlayed": [] 
}

visited = []

def clearScreen(t):
    time.sleep(t) 
    _ = os.system('clear')

def main(): 

    greetings.introduction()
 
    if greetings.accept():
        clearScreen(2) 
    else:
        print("Well then, I suppose you still have some sanity in you...")
        sys.exit() 

    attributes["character"] = lore.chooseChar() 

    clearScreen(1) 

    balance = econ.initBalance() 
    
    clearScreen(1)

    locations.launchsite(attributes, visited) 
    

main() 
