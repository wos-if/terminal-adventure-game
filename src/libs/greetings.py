"""
Wasif Kamran
ICS3U 
This file contains the various functions for outputting greetings and meta information. 
"""

def titleText():
    """
    This functions returns the ascii art string for the game title. 
    Args 
        None
    Returns
        string containing title in ascii art
    """
    return """ ▄▄▄       ██▓███  ▓█████ ▒██   ██▒    ███▄ ▄███▓▓██   ██▓▄▄▄█████▓ ██░ ██   ██████ 
▒████▄    ▓██░  ██▒▓█   ▀ ▒▒ █ █ ▒░   ▓██▒▀█▀ ██▒ ▒██  ██▒▓  ██▒ ▓▒▓██░ ██▒▒██    ▒ 
▒██  ▀█▄  ▓██░ ██▓▒▒███   ░░  █   ░   ▓██    ▓██░  ▒██ ██░▒ ▓██░ ▒░▒██▀▀██░░ ▓██▄   
░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄  ░ █ █ ▒    ▒██    ▒██   ░ ▐██▓░░ ▓██▓ ░ ░▓█ ░██   ▒   ██▒
 ▓█   ▓██▒▒██▒ ░  ░░▒████▒▒██▒ ▒██▒   ▒██▒   ░██▒  ░ ██▒▓░  ▒██▒ ░ ░▓█▒░██▓▒██████▒▒
 ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░▒▒ ░ ░▓ ░   ░ ▒░   ░  ░   ██▒▒▒   ▒ ░░    ▒ ░░▒░▒▒ ▒▓▒ ▒ ░
  ▒   ▒▒ ░░▒ ░      ░ ░  ░░░   ░▒ ░   ░  ░      ░ ▓██ ░▒░     ░     ▒ ░▒░ ░░ ░▒  ░ ░
  ░   ▒   ░░          ░    ░    ░     ░      ░    ▒ ▒ ░░    ░       ░  ░░ ░░  ░  ░  
      ░  ░            ░  ░ ░    ░            ░    ░ ░               ░  ░  ░      ░  
                                                  ░ ░                               """

def introduction(): 
    """
    This funtion prints out the string for introduction information.
    Args
        None
    Returns
        None
    """
    # Print out the title text by calling the function
    print(titleText())

    # Print out the introduction information for the game and information about how the money system works
    print(f"\n\nWelcome to the Apex Games...\nYou are here because you have been conscripted by The Syndicate. Your task in these games is to travel through the map and face the trials till the end location, where you will only be allowed to exit if you have enough liquid capital to do so. \n\nTHE ECONOMY SYSTEM: At almost every location, you will face a challenge and you must pay a fee to accept some of the challenges, but will be rewarded generously for succeeding. Furthermore, the Syndicate has decided to be nice and inflate your money by a certain amount every time you change your location!.\n\n")

def accept():
    """
    This function gets input from the user to see if they want to continue the game or not. 
    Args
        None
    Returns
        True if the user wants to play and False if they do not want to play. 
    """
    # Initialize the variable to a random string
    isAccept = "x"
    # While the input is not a valid option, keep asking for input again
    while isAccept != "Y" and isAccept != "N": 
        isAccept = input("Do you accept the games? (Y/N) ")
    
    # Program comes here after the user inputs a valid option
    # If they choose Y, return True since they want to play the game
    # Otherwise, return False
    if isAccept == "Y": 
        return True 
    else:
        return False 