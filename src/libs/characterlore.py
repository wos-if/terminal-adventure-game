import time
import os

def clearScreen(t):
    """
    Function to clear the screen after a given amount of time. 
    Args
        t: int 
    Returns
        None
    """
    time.sleep(t) 
    _ = os.system('clear')

# Dictionary with backstories for each characted. Inspired from Apex Legends Lore. 
loreStrings = {
    "CRYPTO" : """Crypto specializes in secrets. A brilliant hacker and encryption expert, he uses aerial drones to spy on his opponents in the Apex Arena without being seen. He also has a secret of his own: his name is Tae Joon Park, and he joined the Apex Games to find the people who framed him for murder.""",
    "WRAITH" : """Wraith is a whirlwind fighter, able to execute deadly attacks and manipulate spacetime by opening rifts in the fabric of reality — but those abilities came at a price. Years ago, she woke up in an IMC detention facility with no memory of who she was. Senior Science Pilot Renee Blasey, who volunteered as guinea pig for her own experiments... whose partner betrayed her and locked her away… no longer existed. All that was left was a timid girl, frightened by a cacophony of voices in her head, until another version of herself appeared and taught her to listen to the voices. Following her lead, Wraith found the strength to break free from her prison and escape into a different reality - this reality.""",
    "BLOODHOUND" : """Bloodhound is known across the Outlands as one of the greatest game hunters the Frontier has ever seen. The child of two engineers stationed at the New Dawn industrial plant on Talos, Bloodhound was taken in by their uncle Artur after a meltdown destroyed the facility and killed both their parents. Artur taught them the Old Ways, a belief system that focuses on the glory of nature and rejects modern technology. Yet Bloodhound was constantly drawn to technological marvels, and ultimately used both new and old methods to take down a Goliath that preyed on the people of their village, forever changing their life's path."""
}
def retLore(character):
    """ 
    """
    return loreStrings[character.upper()]

def chooseChar(): 
    
    charChoices = ["WRAITH", "CRYPTO", "BLOODHOUND"]
    
    print(f'You, Player, have the choice to choose between three characters. Press any key to continue.')
    input() 

    print(f'\nCRYPTO:\n{loreStrings["CRYPTO"]}\n\nPress any key to continue.')
    input() 

    print(f'\nWRAITH:\n{loreStrings["WRAITH"]}\n\nPress any key to continue.')
    input() 

    print(f'\nBLOODHOUND:\n{loreStrings["BLOODHOUND"]}\n\nPress any key to continue.')
    input() 
    
    userChoice = input("\nWhich character would you like to choose? Enter their name: ").upper() 

    while userChoice not in charChoices: 
        print("That is not a valid character.")
        userChoice = input("Enter a valid character choice: ").upper() 
    
    return userChoice 