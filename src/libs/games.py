"""
Wasif Kamran
ICS3U 
This file contains the various minigames used throughout the larger game. 
"""

# Import needed libraries
import random
import math
import os
import time

def clearScreen(t):
    """
    Function to clear terminal after t seconds. 
    Args
        t: int
    Returns
        None
    """
    # Delay by t seconds
    time.sleep(t) 
    # Clear terminal
    _ = os.system('clear')

def rockpaperscissors(name):
    """
    This function contains the code for the rock paper scissors game. 
    Args
        name: string
    Returns
        0 if game is won and 1 is game is lost
    """

    # The next couple of lines print out the story line for the game
    # The inputs are to prevent the program from being too overwhelming for the user in terms of text
    print(f"""Welcome {name} to place. You've managed to stumble upon place and awaken the Titan Overlord. He wishes to speak to you.\n""")

    input("Press any key to continue\n")

    print(f"""TITAN OVERLORD: Well, well, what do we have here... A prospective young hero trying to escape The Syndicate, I see. Why don't you try my hand at a couple of games of rock paper scissors?\n""")

    input("Press any key to continue\n")

    print(f"""YOU: Say, I don't know. I've been trying to escape for quite a while and I don't think I have time for you.\n""")

    input("Press any key to continue\n")

    print(f"""TITAN OVERLORD: If you are able to beat me in a tournament of 3, I will give you $50,000. Otherwise, I take $25,000 How does that sound?\n""")

    input("Press any key to continue\n")

    print(f"""YOU: Hmm, I must admit, that does sound pretty enticing... Sure, I'll play three rounds with you.\n""")

    input("Press any key to continue\n")

    # Clear the terminal
    _ = os.system('clear')

    # Print statement for aesthetic purposes 
    print("--\n") 

    # List of options for user and computer randomizer
    options = ["rock", "paper", "scissors"]

    # Initialize win counter to 0
    winCounter = 0

    # Run the code 3 times as there are three rounds
    for i in range(1, 4): 
        # Print out which round number it is
        print(f'This is round {i}.')

        # Get input for their choice
        userAction = input("Enter rock, paper, or scissors: ")
        # Keep asking for input until it is a valid input 
        while userAction not in options: 
            userAction = input("That is not valid. Enter rock, paper, or scissors: ")
        
        # Randomly choose an option for the overlord (computer) 
        overlordAction = random.choice(options) 

        # If they are the same, tell the user it was a tie
        if userAction == overlordAction: 
            print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. You tied!\n')
        # If the user chose rock, decide whether they won or lost based on computer choice
        # If they won, increment the win counter
        elif userAction == "rock":
            if overlordAction == "scissors":
                print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. You won!\n')
                winCounter += 1 
            else:
                print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. The overlord won!\n')
        # If the user chose paper, decide whether they won or lost based on computer choice
        # If they won, increment the win counter
        elif userAction == "paper":
            if overlordAction == "rock":
                print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. You won!\n')
                winCounter += 1
            else:
                print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. The overlord won!\n')
        # If the user chose scissors, decide whether they won or lost based on computer choice
        # If they won, increment the win counter
        elif userAction == "scissors":
            if overlordAction == "paper":
                print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. You won!\n')
                winCounter += 1
            else:
                print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. The overlord won!\n') 

    # If the final win counter is greater than 2, then the user won the total tournament and we output the win statement and return 0
    # Otherwise, we tell them that they lost and return 1
    if winCounter >= 2:
        print(f'TITAN OVERLORD: I suppose I have been defeated. Take your money and your leave now before I eradicate you.')
        return 0 
    else:
        print(f'As expected, I managed to win. Get on your way now, fool, for I cannot be challenged.')
        return 1 

def guessing(name, bound): 
	"""
    Function for the guessing game
    Args
        name: string
        bound: int
    Returns
        0 if game won, 1 if game lost
    """
    # Let the number of guesses intialize to be ceiling of log base 2 of the upper bound (derived from binary search)
	numGuesses = int(math.log(bound, 2)) + 1
    # Initialize guess counter to track the number of guesses the user has used
	guessCounter = 0

    # Let the target value be a random integer between 1 and the bound, which is what the user is trying to guess
	target = random.randint(1, bound)

    # Print description of the game
	print(f'Welcome, {name}. As you may have realized, the Syndicate takes great pride in their games of chance. Here, you will have to guess a number between 1 and an upper bound which will be chosen at random. The higher the bound, the more money you will get as a reward.\n') 

    # Give the user information as to the upper bound and the number of guesses they have 
	print(f'You have to guess between 1 and {bound}. You have {numGuesses} guesses. \n') 

    # Take input for the  guess
	userGuess = input("Enter a guess: ")

    # Run loop until the user guesses the target or number of guesses runs out
	while userGuess != str(target): 
        # Error checking to see if the guess is numeric
        # If it isn't, ask for input again
		if not userGuess.isnumeric(): 
			userGuess = input("The guess must be a valid number. Enter a guess: ")
        # Error checking to see if the guess is in the range
        # If it isn't, ask for the input again
		elif int(userGuess) < 1 or int(userGuess) > bound: 
			userGuess = input("The guess must be between 1 and the bound. Enter a guess: ")
        # If the error checking is passed, run the following code
		else:
            # If the guess is less than target, tell the user their guess was too low
            # Increase the guess counter and ask for another input
            # Do the same for when the guess is too high
			if int(userGuess) < target: 
				print("\nYour guess was too low.")
				guessCounter += 1
				userGuess = input("Enter a guess: ") 
			elif int(userGuess) > target:
				print("\nYour guess was too high.")
				guessCounter += 1
				userGuess = input("Enter a guess: ")
			
            # If the number of guesses has been exceeded, tell the user they have lost the game and return 1
			if guessCounter >= numGuesses:
				print("\nYou've run out of guesses. You win no money. You can try again if you revisit this location.")
				return 1

    # Define the amount of money the user wins 
    # Upper bound is multiplied by 1000 for a linear relationship between the difficulty and the reward. 
	winBounty = bound * 1000

    # Tell the user how much money they won
	print(f"\nYou won!. You obtained ${winBounty}.")
    # Return 0 since the program only comes here if they won
	return 0 

def dice(name, location, target): 
    """
    Function for the dice game
    Args
        name: string
        location: string
        target: int
    """
    # Initialize the numbers on the dice
    die = [1,2,3,4,5,6]

    # Print the introduction of the game and how it works
    print(f"Good work ending up at {location}.\nHere, The Syndicate demands that you play an interesting game of dice with them. \nThe rules are as follows:\nYou will roll a die, as will the appointed member of the Syndicate. Whoever gets the higher number gets a point, and if the two numbers sum to a target value, the points is doubled to 2.\nThis will occur over 3 rounds.\n")

    # Give information as to the target value for obtaining double points
    print(f"The target value has been decided to be {target}.\n")

    # Print statement for aesthetic purposes
    print("--")

    # Initialize the points for the user and the computer
    userPoints = 0
    syndicatePoints = 0 

    # Run code thrice as there are three rounds
    for i in range(1,4):
        # Tell use which round it is
        print(f'This is round {i}.\n')

        # For interactivity, allow the user to press any key to begin the round
        input("Press any key to roll.")     

        # Let the two rolls be randomly chosen from the die values list
        userRoll = random.choice(die)  
        syndicateRoll = random.choice(die) 

        # If the user's roll is greater than the computer's roll, check if they sum to target 
        # If they do, tell the user that they won the round and that they got 2 points
        # Otherwise, they got 1 point
        # Increment the points counter accordingly 
        if userRoll > syndicateRoll: 
            if userRoll + syndicateRoll == target: 
                print(f'You rolled {userRoll}. They rolled {syndicateRoll}. You got 2 points!\n')
                userPoints += 2
            else:
                print(f'You rolled {userRoll}. They rolled {syndicateRoll}. You got 1 point!\n')
                userPoints += 1
        # If the user's roll is less than the computer's roll, check if they sum to target 
        # If they do, tell the user that the computer won the round and that they got 2 points
        # Otherwise, they got 1 point
        # Increment the points counter accordingly         
        elif userRoll < syndicateRoll: 
            if userRoll + syndicateRoll == target: 
                print(f'You rolled {userRoll}. They rolled {syndicateRoll}. They got 2 points!\n')
                syndicatePoints += 2
            else:
                print(f'You rolled {userRoll}. They rolled {syndicateRoll}. They got 1 point!\n')
                syndicatePoints += 1
        # The last case is that they are both equal and if they sum to target, both get 2 points otherwise both get 1 point
        else:
            if userRoll + syndicateRoll == target: 
                print(f'You rolled {userRoll}. They rolled {syndicateRoll}. You both got 2 points!\n')
                userPoints += 2
                syndicatePoints += 2
            else:
                print(f'You rolled {userRoll}. They rolled {syndicateRoll}. You both got 1 point!\n')
                userPoints += 1
                syndicatePoints += 1

    # If after three round the user has more points than the computer, tell them that they won and return 0 
    if userPoints > syndicatePoints: 
        print(f'You won the game! You have won $5000')
        return 0
    # If after three rounds the user has three less points than the computer, tell them that they lost and return 1
    elif userPoints < syndicatePoints:
        print(f'You lost the game! You have only gotten $500 for participating.') 
        return 1
    # If after three rounds they tied, tell them that they tied and return 2
    else:
        print(f'A close game, and you tied! You have won $2500') 
        return 2

def envelopeParadox(name):
    """
    Function for the envelope paradox simulation game
    Args
        name: string
    Returns
        0 if they keep the envelope, and either 5000 or 20000 if they choose the other envelope
    """
    # Print introduction to the game
    print(f"You are faced with an interesting dillemma. You've been presented with an envelope of $10,000. You can either choose this envelope or choose the other envelope which has an equal chance of containing either $5,000 or $20,000.\n") 

    # Get use input for their choice
    choice = input("If you woeuld like to keep this envelope, enter 'k'. If you want to choose the other one, enter 's': ")

    # List of possible user input choices that are valid
    choices = ["k", "s"]   
    # List of choices for the randomizer to pick if they choose the other envelope (sChoices for switch choices) 
    sChoices = ["5, 000", "20, 000"]

    # Keep asking for input until user input is a valid choice
    while choice not in choices: 
        choice = input("That is not valid. If you would like to keep this envelope, enter 'k'. If you want to choose the other one, enter 's': ") 

    # If they choose to keep it, tell them that they got 10000 dollars and return 0 
    if choice == "k": 
        print(f"\nYou have gained $10, 000")
        return 0 
    # Otherwise, pick a random value from sChoices and return accordingly
    else:
        finalValue = random.choice(sChoices)
        print(f"\nYou have gained ${finalValue}.")
        if finalValue == "5, 000":
            return 5000 
        else:
            return 20000

def memory(name, length): 
    """
    Function for the memory game
    Args
        name: string
        length: int 
    Returns
        If they win the game, return 0 and if they lose, return 1
    """
    # Choices for each character in the memory string
    choices = ["x","o"] 
    
    # Initialize the string to be guessed 
    memoryStr = ""

    # Generate the memory string character by character randomly from the choices list
    for i in range(length):
        memoryStr += random.choice(choices)
        memoryStr += " " 

    # Print introduction to the game
    print(f"In order to pass through the game, you must pass the memory game. You will be given a string of a random length between 5 and 10, with a liner relationship with the money you earn from winning.\n\nThe string will be shown for 4 seconds before the terminal is cleared and you must input the sequence you believe is correct. The correct positions will be capitalized and the wrong ones will be left lowercase.\n")

    # Print statement for aesthetics
    print("--")

    # Give the user information as to the string to be guessed
    print(f"The string is {memoryStr}")

    # Give them 4 seconds to remember the string 
    time.sleep(4) 

    # Clear terminal
    _ = os.system('clear')

    # Run the game 4 times since they get 4 tries 
    for i in range(4):
        # Get user input for guess
        guess = input(f"Enter your guess (length {length}) with spaces between letters: ") 
        # While the length of the guess is not equal to the memory string length - 1 (accounting for whitespace)
        while len(guess) != len(memoryStr) - 1:
            guess = input(f"That is invalid. Enter your guess (length {length}) with spaces between letters: ") 
        
        # Iniitalize the resultant string
        printStr = ""

        # If the guess plus whitespace at the end is the same as the memory string, tell the user they won and return 0 
        if guess + " " == memoryStr:
            print("Good job! You have excellent memory and can proceed")
            return 0 

        # If they hadn't won, then generate the resultant string by using the rules outlined in the introduction 
        for j in range(0, len(guess)):
            if guess[j] == memoryStr[j]:
                printStr += guess[j].upper() 
                printStr += " "
            else: 
                printStr += guess[j].lower()
                printStr += " "

        # Give the user the resultant string
        print(f'\nYour result: {printStr}.') 

    # If we come out of the for loop without winning, they ran out of guesses and we return 1
    print(f'\nYou ran out of guesses.')
    return 1

def wordguess(name, word):
    """
    Function for the wordguess game 
    Args
        name: string
        word: string
    Returns
        Return 0 if they win, and 1 if they lose
    """

    # Print introduction to the game
    print(f"For some odd reason, the Syndicate values your linguistic abilities. With inspiration from the well known pop game Wordle, you will be given 6 attempts to guess a 5 letter word. Letters in the correct place will be capitalized and letters in the wrong place but in the word will have a * next to them. Letters not in the word at all will be left lowercase. Note that the letters in the word will not be repeated.\n") 

    # Print statement for aesthetic purposes
    print("--\n")

    # Give them 6 tries to guess the word
    for i in range(1, 7): 
        # Output the guess number
        print(f"Guess {i}")

        # Get input for the guess
        guess = input("Enter your 5 letter guess with spaced between letters: ").upper().strip() 

        # Error checking to see if the length of the guess is 9 and that all the characters are letters or spaces
        while (not all(x.isalpha() or x.isspace() for x in guess)) or (len(guess) != 9):
            guess = input("Invalid. Enter your 5 letter guess with spaced between letters: ").upper().strip() 
        
        # Initilize the resultant string
        printStr = ""

        # Generate the resultant string based on rules outlined in the introduction
        # Iterate over the characters in guess
        for j in range (0, len(guess)): 
            # If the current iteration character is not a space, proceed 
            if guess[j].isalpha():
                # If letter is in the right place, add it to the resultant string
                if guess[j] == word[j]:
                    printStr += guess[j]
                    printStr += " " 
                # If the letter is in the word but not in the right place, add it with a star to the resultant string
                elif guess[j] in word[j:len(guess)+1]: 
                    printStr += guess[j]
                    printStr += "*"
                    printStr += " "
                # If the letter is not in the word at all, lowercase the word and add it to the resultant string
                else:
                    printStr += guess[j].lower() 
                    printStr += " " 
        
        # Output the resultant string to the player
        print(f"Results: {printStr}\n") 

        # If the resultant string with whitespace removed is the same as word, they won the game and return 0 
        if printStr.strip() == word:
            print("Congratulations! You were able to guess the word correctly!")
            return 0 

    # If they make it out the for loop, they have used up all their guesses and we return 1
    print("You've run out of guesses and have not won the reward. You can always try again by revisiting the location.")
    return 1

def cf(name, chance): 
    """
    Function for the coinflip game
    Args
        name: string
        chance: int
    Returns
        0 if the gamble is won and 1 if the gamble is lost
    """
    # Output introduction to the game
    print(f"As you may have noticed, the Syndicate enjoys asserting their power and letting their contestents feel completely powerless of their fate. In this game (can we really call it a game?) a coin will be flipped on your behalf. If you get 2 heads, you win the game and win the reward. Otherwise, you win nothing.")

    # List of 0s and 1s to flip an uneven coin (not a 5050 chance) 
    # Add a 0 and 1 to initialize
    options = [0,1]

    # Given the randomized chance, we add 0s which represents heads to the list
    for i in range(chance):
        options.append(0) 

    # Then we add the complement probability to the list as well with 1s representing tails
    for i in range(100-chance):
        options.append(1) 

    # Our initial coin flip result is chosen randomly from the list
    result = random.choice(options) 

    # If the result is heads, continue. 
    # Otherwise, the game has already ended
    if result == 0:
        # The second result is chosen randomly from the list
        bresult = random.choice(options)
        # If the second result is also heads, let them know they won the gamble and return 0
        if bresult == 0:
            print(f"Congratulations, you won the gamble!")
            return 0 
        # If they get tails on the second result, return 1 as they lost the game
        else:
            print(f"You lost the coin toss, but the game can be attempted again by revisiting the location.")
            return 1
    else:
        print(f"You lost the coin toss, but the game can be attempted again by revisiting the location.")
        return 1

def russianroulette(name):
    """
    Function for the russian roulette game.
    Args
        name: string
    Returns
        Return 0 if the game is won and 1 if the game is lost
    """
    # List of characters that will be in the roulette
    charList = ["GIBRALTAR", "ASH", "BLOODHOUND", "LIFELINE", "PATHFINDER", "LOBA", "REVNANT"]
    # Add the user's character to the list
    charList.append(name.upper())
    # Let a variable be the number of characters
    nums = len(charList)
    # Output introduction for the game
    print("You've reached the final location. Here, you have no choice but to participate in the Russian Roulette. Either you win the entire game, or lose.\n")

    # While the number of characters left is not 1
    while nums != 1:
        # The new eliminated character is chosen at random
        newElim = random.choice(charList) 
        # Remove the elimination from the character list
        charList.remove(newElim) 
        # Reduce the number of characters by 1
        nums -= 1 
        # If the new elimination is the player's name, they have lost game so we return 1
        # Otherwise we continue the game and output the name of the character who got eliminated
        if newElim != name.upper(): 
            print(f"\n{newElim} has been eliminated.") 
            input("Press any key to continue") 
        else:
            print("\nYou have been eliminated")
            return 1
    # Return 0 if they win the game    
    return 0
        
