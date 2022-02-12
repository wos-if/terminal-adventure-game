"""
Wasif Kamran
ICS3U
This file contains crucial functions for the economy system. A .txt file is used to store the balance in order to make it more easily accesible throughout the multiple files.
"""

# Import needed libraries
import random
import os

def initBalance(): 
    """
    This function intializes the balance at the beginning based off user input. 
    Args
        None
    Returns
        None
    """
    # Give description of what the user is about to choose
    print(f'You will be given three choices for your intial balance. While it may be tempting to choose the highest value keep in mind that your balance is randomly inflated every move.\n\nHere are your choices: $1000, $5000, $10000.\n')

    # Get input for which amount they want to initialize with
    balanceStr = input("What would you like your initial balance to be (enter the numerical option)? ") 

    # List of possible options
    options = ["1000", "5000", "10000"]

    # Keep asking for user input until they input a valid option from the list
    while balanceStr not in options: 
        balanceStr = input('That is not a valid option - enter a valid option: ') 

    # Open the file, erase it, and update it with the new initial balance 
    file = open("./src/libs/balance.txt", "r+") 
    file.truncate(0) 
    file.write(balanceStr) 
    file.close() 

def requestBalance(): 
    """
    This functions returns the current balance.
    Args
        None
    Returns
        Current balance of the user
    """
    # Open the file and return the contents after reading it 
    with open('./src/libs/balance.txt') as f:
        contents = f.read()
        return int(float(contents))

def updateBalance(amount):
    """
    This function updates the balance in the .txt file
    Args
        amount: int
    Returns
        None
    """
    # Read the current balance
    with open('./src/libs/balance.txt') as f:
        contents = f.read()
    
    # Open the file, erase it, and update the value of the balance
    file = open("./src/libs/balance.txt", "r+") 
    file.truncate(0) 
    file.write(str(int(float(contents))+amount))
    file.close() 

def generateRates(amount):
    """
    This function generates randomly the inflation rates used throughout the game.
    Args
        amount: int
    Returns
        List of randomly generated inflation rates
    """
    # Initialize empty list with rates
    rates = [] 

    # First add a very small inflation rate to guarantee the existence of a small inflation value. 
    rates.append(round(random.uniform(00.20, 00.99), 2))

    # Then add larger inflation rates to make the game more enjoyable
    for i in range(amount - 1):
        rates.append(round(random.uniform(00.20, 20.00), 2))
    
    # Return the list 
    return rates