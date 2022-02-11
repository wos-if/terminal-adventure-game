import random
import math
import os
import time

def rockpaperscissors(name):
    options = ["rock", "paper", "scissors"]

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
    _ = os.system('clear')

    print("--\n") 

    options = ["rock", "paper", "scissors"]

    winCounter = 0

    for i in range(1, 4): 
        print(f'This is round {i}.')

        userAction = input("Enter rock, paper, or scissors: ")
        while userAction not in options: 
            userAction = input("That is not valid. Enter rock, paper, or scissors: ")
        
        overlordAction = random.choice(options) 

        if userAction == overlordAction: 
            print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. You tied!\n')
        elif userAction == "rock":
            if overlordAction == "scissors":
                print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. You won!\n')
                winCounter += 1 
            else:
                print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. The overlord won!\n')
        elif userAction == "paper":
            if overlordAction == "rock":
                print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. You won!\n')
                winCounter += 1
            else:
                print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. The overlord won!\n')
        elif userAction == "scissors":
            if overlordAction == "paper":
                print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. You won!\n')
                winCounter += 1
            else:
                print(f'\nYou chose {userAction}. The overlord chose {overlordAction}. The overlord won!\n') 

    if winCounter >= 2:
        print(f'TITAN OVERLORD: I suppose I have been defeated. Take your money and your leave now before I eradicate you.')
        return 0 
    else:
        print(f'As expected, I managed to win. Get on your way now, fool, for I cannot be challenged.')
        return 1 


def guessing(name, bound): 
	
	numGuesses = int(math.log(bound, 2)) + 1
	guessCounter = 0

	target = random.randint(1, bound)

	print(f'Welcome, {name}. As you may have realized, the Syndicate takes great pride in their games of chance. Here, you will have to guess a number between 1 and an upper bound which will be chosen at random. The higher the bound, the more money you will get as a reward.\n') 

	print(f'You have to guess between 1 and {bound}. You have {numGuesses} guesses. \n') 

	userGuess = input("Enter a guess: ")

	while userGuess != str(target): 
		if not userGuess.isnumeric(): 
			userGuess = input("The guess must be a valid number. Enter a guess: ")
		elif int(userGuess) < 1 or int(userGuess) > bound: 
			userGuess = input("The guess must be between 1 and the bound. Enter a guess: ")
		else:
			if int(userGuess) < target: 
				print("\nYour guess was too low.")
				guessCounter += 1
				userGuess = input("Enter a guess: ") 
			elif int(userGuess) > target:
				print("\nYour guess was too high.")
				guessCounter += 1
				userGuess = input("Enter a guess: ")
			
			if guessCounter >= numGuesses:
				print("\nYou've run out of guesses. You win no money. You can try again if you revisit this location.")
				return 1

	winBounty = bound * 1000
	print(f"\nYou won!. You obtained ${winBounty}.")
	return 0 

def dice(name, location, target): 

    die = [1,2,3,4,5,6]
    print(f"Good work ending up at {location}.\nHere, The Syndicate demands that you play an interesting game of dice with them. \nThe rules are as follows:\nYou will roll a die, as will the appointed member of the Syndicate. Whoever gets the higher number gets a point, and if the two numbers sum to a target value, the points is doubled to 2.\nThis will occur over 3 rounds.\n")

    print(f"The target value has been decided to be {target}.\n")

    print("--")

    userPoints = 0
    syndicatePoints = 0 

    for i in range(1,4):
        print(f'This is round {i}.\n')

        input("Press enter to roll.")     

        userRoll = random.choice(die)  
        syndicateRoll = random.choice(die) 

        if userRoll > syndicateRoll: 
            if userRoll + syndicateRoll == target: 
                print(f'You rolled {userRoll}. They rolled {syndicateRoll}. You got 2 points!\n')
                userPoints += 2
            else:
                print(f'You rolled {userRoll}. They rolled {syndicateRoll}. You got 1 point!\n')
                userPoints += 1
        elif userRoll < syndicateRoll: 
            if userRoll + syndicateRoll == target: 
                print(f'You rolled {userRoll}. They rolled {syndicateRoll}. They got 2 points!\n')
                syndicatePoints += 2
            else:
                print(f'You rolled {userRoll}. They rolled {syndicateRoll}. They got 1 point!\n')
                syndicatePoints += 1
        else:
            if userRoll + syndicateRoll == target: 
                print(f'You rolled {userRoll}. They rolled {syndicateRoll}. You both got 2 points!\n')
                userPoints += 2
                syndicatePoints += 2
            else:
                print(f'You rolled {userRoll}. They rolled {syndicateRoll}. You both got 1 point!\n')
                userPoints += 1
                syndicatePoints += 1

    if userPoints > syndicatePoints: 
        print(f'You won the game! You have won $5000')
        return 0
    elif userPoints < syndicatePoints:
        print(f'You lost the game! You have only gotten $500 for participating.') 
        return 1
    else:
        print(f'A close game, and you tied! You have won $2500') 
        return 2

def envelopeParadox(name):
    print(f"You are faced with an interesting dillemma. You've been presented with an envelope of $10,000. You can either choose this envelope or choose the other envelope which has an equal chance of containing either $5,000 or $20,000.\n") 

    choice = input("If you woeuld like to keep this envelope, enter 'k'. If you want to choose the other one, enter 's': ")

    choices = ["k", "s"]
    sChoices = ["5, 000", "20, 000"]

    while choice not in choices: 
        choice = input("That is not valid. If you would like to keep this envelope, enter 'k'. If you want to choose the other one, enter 's': ") 

    if choice == "k": 
        print(f"\nYou have gained $10, 000")
        return 0 
    else:
        finalValue = random.choice(sChoices)
        print(f"\nYou have gained ${finalValue}.")
        if finalValue == "5, 000":
            return 5000 
        else:
            return 20000

def memory(name, length): 
    choices = ["x","o"] 
    
    memoryStr = ""

    for i in range(length):
        memoryStr += random.choice(choices)
        memoryStr += " " 

    print(f"In order to pass through the game, you must pass the memory game. You will be given a string of a random length between 5 and 10, with a liner relationship with the money you earn from winning.\n\nThe string will be shown for 4 seconds before the terminal is cleared and you must input the sequence you believe is correct. The correct positions will be capitalized and the wrong ones will be left lowercase.\n")

    print("--")
    print(f"The string is {memoryStr}")

    time.sleep(4) 
    _ = os.system('clear')

    for i in range(4):
        guess = input(f"Enter your guess (length {length}) with spaces between letters: ") 
        while len(guess) != len(memoryStr) - 1:
            guess = input(f"That is invalid. Enter your guess (length {length}) with spaces between letters: ") 
        
        printStr = ""

        if guess + " " == memoryStr:
            print("Good job! You have excellent memory and can proceed")
            return 0 

        for j in range(0, len(guess)):
            if guess[j] == memoryStr[j]:
                printStr += guess[j].upper() 
                printStr += " "
            else: 
                printStr += guess[j].lower()
                printStr += " "

        print(f'\nYour result: {printStr}.') 

    print(f'\nYou ran out of guesses.')
    return 1

def wordguess(name, word):

    #choices = ['PAUSE', 'HUMOR', 'FRAME', 'ELDER', 'SKILL', 'ALOFT', 'PLEAT', 'SHARD', 'MOIST', ]

    print(f"For some odd reason, the Syndicate values your linguistic abilities. With inspiration from the well known pop game Wordle, you will be given 6 attempts to guess a 5 letter word. Letters in the correct place will be capitalized and letters in the wrong place but in the word will have a * next to them. Letters not in the word at all will be left lowercase. Note that the letters in the word will not be repeated.\n") 

    print("--\n")

    for i in range(1, 7): 
        
        print(f"Guess {i}")
        guess = input("Enter your 5 letter guess with spaced between letters: ").upper().strip() 

        while (not all(x.isalpha() or x.isspace() for x in guess)) or (len(guess) != 9):
            guess = input("Invalid. Enter your 5 letter guess with spaced between letters: ").upper().strip() 
        
        printStr = ""

        for j in range (0, len(guess)): 
            if guess[j].isalpha():
                if guess[j] == word[j]:
                    printStr += guess[j]
                    printStr += " " 
                elif guess[j] in word[j:len(guess)+1]: 
                    printStr += guess[j]
                    printStr += "*"
                    printStr += " "
                else:
                    printStr += guess[j].lower() 
                    printStr += " " 
        
        print(f"Results: {printStr}\n") 

        if printStr.strip() == word:
            print("Congratulations! You were able to guess the word correctly!")
            return 0 

    print("You've run out of guesses and have not won the reward. You can always try again by revisiting the location.")
    return 1

# For creative purposes, the function will output the wrong value sometimes. 
# This is a feature, not a bug.

def cf(name, chance): 

    print(f"As you may have noticed, the Syndicate enjoys asserting their power and letting their contestents feel completely powerless of their fate. In this game (can we really call it a game?) a coin will be flipped on your behalf. If you get 2 heads, you win the game and win the reward. Otherwise, you win nothing.")

    options = [0,1]

    for i in range(chance):
        options.append(0) 

    for i in range(100-chance):
        options.append(1) 

    print(options)
    result = random.choice(options) 

    if result == 0:
        bresult = random.choice(options) 
        if bresult == 0:
            print(f"Congratulations, you won the gamble!")
            return 0 
        else:
            print(f"You lost the coin toss, but the game can be attempted again by revisitiing the location.")
            return 1
    else:
        print(f"You lost the coin toss, but the game can be attempted again by revisitiing the location.")
        return 1

def russianroulette(name):
    charList = ["GIBRALTAR", "ASH", "BLOODHOUND", "LIFELINE", "PATHFINDER", "LOBA", "REVNANT"]
    charList.append(name.upper())
    nums = len(charList)
    print("You've reached the final location. Here, you have no choice but to participate in the Russian Roulette. Either you win the entire game, or lose.\n")

    while nums != 1:
        newElim = random.choice(charList) 
        charList.remove(newElim) 
        nums -= 1 
        if newElim != name.upper(): 
            print(f"\n{newElim} has been eliminated.") 
            input("Press any key to continue") 
        else:
            print("You have been eliminated, and the game is over. You lost.")
            return 1
        
    return 0
        
