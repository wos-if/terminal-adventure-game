"""
Wasif Kamran
ICS3U 
This file contains all the code for the locations and their activities. 
"""

# Import needed libraries
import os
import random
import time
import sys

# Import files for their functions
import libs.economy as econ
import libs.games as games 

# Assign a variable for the strings in order for consistency throughout the functions
HARVESTER = "HARVESTER"
SKYHOOK = "SKYHOOK"
COUNTDOWN = "COUNTDOWN"
LAVASIPHON = "LAVA SIPHON"
GEYSER = "GEYSER"
CLIMATIZER = "CLIMATIZER"
THERMALSTATION = "THERMAL STATION"
EPICENTER = "EPICENTER"
LAUNCHSITE = "LAUNCHSITE" 

# Make a dictionary for all the nodes and edges on the graph
connections = {
    LAUNCHSITE: [GEYSER, LAVASIPHON, EPICENTER, CLIMATIZER],
    GEYSER: [LAUNCHSITE, THERMALSTATION],
    THERMALSTATION: [GEYSER, EPICENTER],
    EPICENTER: [LAUNCHSITE, THERMALSTATION, CLIMATIZER],
    CLIMATIZER: [EPICENTER, LAUNCHSITE, SKYHOOK, COUNTDOWN, HARVESTER], 
    COUNTDOWN: [CLIMATIZER, HARVESTER],
    SKYHOOK: [LAVASIPHON, CLIMATIZER, HARVESTER],
    LAVASIPHON: [LAUNCHSITE, SKYHOOK],
    HARVESTER: [SKYHOOK, CLIMATIZER, COUNTDOWN]
}

# Descriptions of all the locations
descriptions = {
    HARVESTER: """Formally the "Planet Harvester", the Harvester is a huge multi-story structure on the center of the map with lots of entrances and exit points on multiple levels along with long corridors.""",
    SKYHOOK: """Skyhook is comprised of a large city with various skyscrapers around with the famous Space Elevator Tower in the center. There's also a train station where the train used to stop when at Skyhook.""",
    COUNTDOWN: """Once known as "Drill Site", Countdown is located southwest of Skyhook. It features multiple pits of lava, and an opening floor in the very center.""",
    LAVASIPHON: """Lava Siphon is a large area that contains three gondola stations, and a research facility that goes into the mountain range. The facility is expansive on the inside, with a couple of small rooms near the entrance, and a big room near the back.""",
    GEYSER: """The Geyser is a small facility to the east of the map with a large stunning geyser in the center.""",
    CLIMATIZER: """Climatizer consists a set of large research facilities in which several dangerous experiments are conducted - perhaps on people as well.""",
    LAUNCHSITE: """This is the original starting location. From here, your adventure begins (unless you are returning). This is what makes or breaks a person.""",
    EPICENTER: """The Epicenter is a large drill tower that was the source of the "Meltdown" accident that lead to the abandonment of the games for a short time period.""",
    THERMALSTATION: """Thermal Station is essentially divided into four zones: the central drill area, the small group of houses on its western edge, the larger village on its southern edge and the Thermal Station Train Station to its eastern edge."""
}

# Generate 5 inflation rates and store it in an array called inflationRates
inflationRates = econ.generateRates(5) 

def clearScreen(t):
    """
    Function to clear screen after t seconds
    Args
        t: int
    Returns
        None
    """
    # Add delay for t seconds
    time.sleep(t) 
    # Clear terminal
    _ = os.system('clear')

def grabConnections(place): 
    """
    Function to get connections and print them out in order
    Args
        place: string
    Returns
        None
    """
    # Iterate over the connections in the graph dictionary 
    for i in range(1, len(connections[place.upper()]) +1 ):
        # Output the location with the iteration number
        print(f'[{i}]. {connections[place.upper()][i-1]}') 

def getNextLocations(possibleLocations):
    """
    Function to get the user's choice for the next option
    Args
        possibleLocations: list
    Returns
        The next location the user chooses
    """
    # Ask for input for next location
    nextLoc = input(f'Enter the number allocated to the location you would like to visit: ') 
    # Keep asking for input as long as the input is not in the possible locations list
    while nextLoc not in possibleLocations: 
        nextLoc = input('That is not a possible location. Enter a valid location or 0 for request balance: ') 
    
    # Return the next location chosen by user
    return nextLoc

def playGame():
    """
    Function to ask user whether or not they want to play the game for a given location
    Args
        Nnone
    Returns
        The users choice as to whether or not they are playing (y/n)
    """
    # Ask for input for the choice 
    choice = input("Would you like to play the game for this location? (y/n): ") 
    # List of valid options the user can choose from
    choiceOptions = ['y', 'n']
    # Keep asking for input until they give a valid input
    while choice not in choiceOptions: 
        choice = input("Would you like to play the game for this location? (y/n): ") 
    
    # Return the user's choice
    return choice 

def launchsite(attributes, visited): 
    """
    Function for the launchsite location
    Args
        attributes: dictionary
        visited: list
    Returns
        None
    """
    # Check if launchsite is in visited. 
    # If it is, output the description with the welcome, otherwise, only welcome them back
    if LAUNCHSITE not in visited: 
        print(f'{attributes["character"]}, you are at LAUNCHSITE.\n\n{descriptions[LAUNCHSITE]}\n\nThere is not much to do here... Where would you like to go next? You could also request balance.') 
        visited.append(LAUNCHSITE)
    else:
        print(f'Welcome back. What would you like to do next?')
        # Get the inflation choice for this location by randomly choosing from the inflation rates list
        inflationChoice = random.choice(inflationRates)
        # Update the balance by calling the function from econ
        econ.updateBalance(inflationChoice)
        # Append the current inflation choice to the inflationRates key in attributes
        attributes["inflationRates"].append(inflationChoice)

    # Add the request balance option
    print('[0]. REQUEST Balance')
    # Print the possible options by calling the grabConnections function
    grabConnections(LAUNCHSITE)
    
    # Get the users choice for the next location (each number allocated to either balance or the locations from grabConnections)
    userChoice = getNextLocations(['0', '1', '2', '3', '4'])

    # If the userChoice is 0, output the balance but then ask for another input until they give a location to go to using the getNextLocations function
    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(LAUNCHSITE)
    
        userChoice = getNextLocations(['0', '1', '2', '3', '4'])

    # For the possible options, clear screen after one second and call the allocated function
    if userChoice == '1': 
        clearScreen(1)
        geyser(attributes, visited) 
    elif userChoice == '2': 
        clearScreen(1)
        lavasiphon(attributes, visited) 
    elif userChoice == '3': 
        clearScreen(1)
        epicenter(attributes, visited) 
    elif userChoice == '4': 
        clearScreen(1)
        climatizer(attributes, visited) 

def geyser(attributes, visited): 
    """
    Function for the geyser location
    Args
        attributes: dictionary
        visited: list
    Returns
        None
    """

    # Update the balance by a randomized inflation rate
    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    # Check if geyser is in visited. 
    # If it is, output the description with the welcome, otherwise, only welcome them back
    if GEYSER not in visited:
        print(f'{attributes["character"]}, you are at GEYSER.\n\n{descriptions[GEYSER]}\n\n')
        visited.append(GEYSER)
    else:
        print(f'Welcome back to GEYSER!') 
    
    # See if the user wants to play the game for the location
    gameBool = playGame() 

    # If they want to play, clear screen and call the game function
    # If they don't, the program will skip to the next locations part
    if gameBool == 'y': 
        # Clear screen after a second
        clearScreen(1)
        # Add rockpaperscissros to games played in attributes
        attributes["gamesPlayed"].append("rockpaperscissors")
        # Check if they win the game and give them the reward accordingly 
        if games.rockpaperscissors(attributes["character"]) == 0: 
            econ.updateBalance(50000)
        else:
            econ.updateBalance(25000) 
    
    # Ask where they would like to go
    print("\nWhere would you like to go next?")
    # Add request balance option
    print('[0]. REQUEST Balance')
    # Print the connections and possible locations they can go to
    grabConnections(GEYSER)
    
    # Get their input for where they want to go
    userChoice = getNextLocations(['0', '1', '2'])

    # If the userChoice is 0, output the balance but then ask for another input until they give a location to go to using the getNextLocations function 
    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(GEYSER)
    
        userChoice = getNextLocations(['0', '1', '2'])
    
    # For the possible options, clear screen after one second and call the allocated function
    if userChoice == "1":
        clearScreen(1)
        launchsite(attributes, visited) 
    elif userChoice == "2": 
        clearScreen(1)
        thermalstation(attributes, visited)

def thermalstation(attributes, visited): 
    """
    Function for the thermal station location
    Args
        attributes: dictionary
        visited: list
    Returns
        None
    """
    # Update the balance by a randomized inflation rate
    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    # Check if thermal station is in visited. 
    # If it is, output the description with the welcome, otherwise, only welcome them back
    if THERMALSTATION not in visited:
        print(f'{attributes["character"]}, you are at THERMAL STATION.\n\n{descriptions[THERMALSTATION]}\n\n')
        visited.append(THERMALSTATION)
    else:
        print(f'Welcome back to THERMAL STATION!') 
    
    # See if the user wants to play the game for the location
    gameBool = playGame() 

    # If they want to play, clear screen and call the game function
    # If they don't, the program will skip to the next locations part
    if gameBool == 'y': 
        # Clear screen after a second
        clearScreen(1)
        # ADd cf to games played in attributes
        attributes["gamesPlayed"].append("cf")
        # Check if they win the game and give them the reward accordingly
        if games.cf(attributes["character"], random.randint(25, 75)) == 0: 
            econ.updateBalance(30000)
        else:
            econ.updateBalance(0) 
    
    # Ask where they would like to go
    print("\nWhere would you like to go next?")
    # Add request balance option
    print('[0]. REQUEST Balance')
    # Print the connections and possible locations they can go to
    grabConnections(THERMALSTATION)
    
    # Get input for where they want to go
    userChoice = getNextLocations(['0', '1', '2'])

    # If the userChoice is 0, output the balance but then ask for another input until they give a location to go to using the getNextLocations function 
    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(THERMALSTATION)
    
        userChoice = getNextLocations(['0', '1', '2'])
    
    # For the possible options, clear screen after one second and call the allocated function
    if userChoice == "1":
        clearScreen(1)
        geyser(attributes, visited) 
    elif userChoice == "2": 
        clearScreen(1)
        epicenter(attributes, visited)

def epicenter(attributes, visited): 
    """
    Function for the epicenter location
    Args
        attributes: dictionary
        visited: list
    Returns
        None
    """

    # Update the balance by a randomized inflation rate
    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    # Check if epicenter is in visited. 
    # If it is, output the description with the welcome, otherwise, only welcome them back
    if EPICENTER not in visited:
        print(f'{attributes["character"]}, you are at EPICENTER.\n\n{descriptions[EPICENTER]}\n\n')
        visited.append(EPICENTER)
    else:
        print(f'Welcome back to EPICENTER!') 
    
    # See if the user wants to play the game for the location
    gameBool = playGame() 

    # If they want to play, clear screen and call the game function
    # If they don't, the program will skip to the next locations part
    if gameBool == 'y': 
        # Clear screen after a second
        clearScreen(1)
        # Add guessing to games played in attributes
        attributes["gamesPlayed"].append("guessing")
        # Generate the upperbound to pass as argument
        upperBound = random.randint(100, 1000) 
        # Check if they win the game and give them the reward accordingly
        if games.guessing(attributes["character"], upperBound) == 0: 
            econ.updateBalance(upperBound * 1000)
        else:
            econ.updateBalance(0) 
    
    # Ask where they would like to go
    print("\nWhere would you like to go next?")
    # Add request balance option
    print('[0]. REQUEST Balance')
    # Print the conections and possible locations they can go to
    grabConnections(EPICENTER)
    
    # Get their input for where they want to go
    userChoice = getNextLocations(['0', '1', '2', '3'])

    # If the userChoice is 0, output the balance but then ask for another input until they give a location to go to using the getNextLocations function 
    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(EPICENTER)
    
        userChoice = getNextLocations(['0', '1', '2', '3'])
    
    # For the possible options, clear screen after one second and call the allocated function
    if userChoice == "1":
        clearScreen(1)
        launchsite(attributes, visited) 
    elif userChoice == "2": 
        clearScreen(1)
        thermalstation(attributes, visited)
    elif userChoice == "3": 
        clearScreen(1)
        climatizer(attributes, visited)

def climatizer(attributes, visited): 
    """
    Function for the climatizer location
    Args
        attributes: dictionary
        visited: list
    Returns
        None
    """

    # Update the balance by a randomized inflation rate
    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    # Check if climatizer is in visited. 
    # If it is, output the description with the welcome, otherwise, only welcome them back
    if CLIMATIZER not in visited:
        print(f'{attributes["character"]}, you are at CLIMATIZER.\n\n{descriptions[CLIMATIZER]}\n\n')
        visited.append(CLIMATIZER)
    else:
        print(f'Welcome back to CLIMATIZER!') 
    
    # See if the user wants to play the game for the location
    gameBool = playGame() 

    # If they want to play, clear screen and call the game function
    # If they don't, the program will skip to the next locations part
    if gameBool == 'y': 
        # Clear screen after a second
        clearScreen(1)
        # Add memory to games played in attributes
        attributes["gamesPlayed"].append("memory")
        # Generate the length of the memory string between 5 and 10
        # Check if they win the game and give reward accordingly
        memLength = random.randint(5, 10) 
        if games.memory(attributes["character"], memLength) == 0: 
            econ.updateBalance(memLength * 1300)
        else:
            econ.updateBalance(0) 
    
    # Ask where they would like to go
    print("\nWhere would you like to go next?")
    # Add request balance option
    print('[0]. REQUEST Balance')
    # Print the connections and possible locations they can go to
    grabConnections(CLIMATIZER)
    
    # GEt their input for where they want to go
    userChoice = getNextLocations(['0', '1', '2', '3', '4', '5'])

    # If the userChoice is 0, output the balance but then ask for another input until they give a location to go to using the getNextLocations function
    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(CLIMATIZER)
    
        userChoice = getNextLocations(['0', '1', '2', '3', '4', '5'])
    
    # For the possible options, clear screen after one second and call the allocated function
    if userChoice == "1":
        clearScreen(1)
        epicenter(attributes, visited) 
    elif userChoice == "2": 
        clearScreen(1)
        launchsite(attributes, visited)
    elif userChoice == "3": 
        clearScreen(1)
        skyhook(attributes, visited)
    elif userChoice == "4": 
        clearScreen(1)
        countdown(attributes, visited)
    elif userChoice == "5": 
        clearScreen(1)
        harvester(attributes, visited)

def countdown(attributes, visited): 
    """
    Function for the countdown location
    Args
        attributes: dictionary
        visited: list
    Returns
        None
    """

    # Update the balance by a randomized inflation rate
    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    # Check if countdown is in visited. 
    # If it is, output the description with the welcome, otherwise, only welcome them back
    if COUNTDOWN not in visited:
        print(f'{attributes["character"]}, you are at COUNTDOWN.\n\n{descriptions[COUNTDOWN]}\n\n')
        visited.append(COUNTDOWN)
    else:
        print(f'Welcome back to COUNTDOWN!') 
    
    # See if the user wants to play the game for the location
    gameBool = playGame() 

    # If they want to play, clear screen and call the game function
    # If they don't, the program will skip to the next locations part
    if gameBool == 'y': 
        # Clear screen after a second
        clearScreen(1)
        # Add paradox to games played in attributes
        attributes["gamesPlayed"].append("paradox")
        # Check if they win the game and give them the reward accordingly
        userResult = games.envelopeParadox(attributes["character"]) 
        if userResult == 0: 
            econ.updateBalance(10000)
        else:
            econ.updateBalance(userResult) 
    
    # Ask where they would like to go
    print("\nWhere would you like to go next?")
    # Add request balance option
    print('[0]. REQUEST Balance')
    # Print the connections and possible locations they can go to
    grabConnections(COUNTDOWN)
    
    # Get their input for where they want to go
    userChoice = getNextLocations(['0', '1', '2'])

    # If the userChoice is 0, output the balance but then ask for another input until they give a location to go to using the getNextLocations function
    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(COUNTDOWN)
    
        userChoice = getNextLocations(['0', '1', '2'])
    
    # For the possible options, clear screen after one second and call the allocated function
    if userChoice == "1":
        clearScreen(1)
        climatizer(attributes, visited) 
    elif userChoice == "2": 
        clearScreen(1)
        harvester(attributes, visited)

def lavasiphon(attributes, visited): 
    """
    Function for the lavasiphon location
    Args
        attributes: dictionary
        visited: list
    Returns
        None
    """

    # Update the balance by a randomized inflation rate
    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    # Check if lava siphon is in visited. 
    # If it is, output the description with the welcome, otherwise, only welcome them back
    if LAVASIPHON not in visited:
        print(f'{attributes["character"]}, you are at LAVA SIPHON.\n\n{descriptions[LAVASIPHON]}\n\n')
        visited.append(LAVASIPHON)
    else:
        print(f'Welcome back to LAVA SIPHON') 
    
    # See if the user wants to play the game for the location
    gameBool = playGame() 

    # If they want to play, clear screen and call the game function
    # If they don't, the program will skip to the next locations part
    if gameBool == 'y': 
        # Clear screen after a second
        clearScreen(1)
        # Add dice to the games played in attributes
        attributes["gamesPlayed"].append("dice")
        # Check if they win the game and give them the reward accordingly 
        gameResult = games.dice(attributes["character"], "LAVA SIPHON", random.randint(6, 12))
        if  gameResult == 0: 
            econ.updateBalance(5000)
        elif gameResult == 1:
            econ.updateBalance(500)
        elif gameResult == 2:
            econ.updateBalance(2500) 
    
    # Ask where they would like to go
    print("\nWhere would you like to go next?")
    # Add request balance opttion
    print('[0]. REQUEST Balance')
    # Print the connections and possible locations they can go to
    grabConnections(LAVASIPHON)
    
    # Get their input for where they want to go
    userChoice = getNextLocations(['0', '1', '2'])

    # If the userChoice is 0, output the balance but then ask for another input until they give a location to go to using the getNextLocations function
    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(LAVASIPHON)
    
        userChoice = getNextLocations(['0', '1', '2'])
    
    # For the possible options, clear screen after one second and call the allocated function
    if userChoice == "1":
        clearScreen(1)
        launchsite(attributes, visited) 
    elif userChoice == "2": 
        clearScreen(1)
        skyhook(attributes, visited)

def skyhook(attributes, visited): 
    """
    Function for the skyhook location
    Args
        attributes: dictionary
        visited: list
    Returns
        None
    """

    # Update the balance by a randomized inflation rate
    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    # Check if skyhook is in visited. 
    # If it is, output the description with the welcome, otherwise, only welcome them back
    if SKYHOOK not in visited:
        print(f'{attributes["character"]}, you are at SKYHOOK.\n\n{descriptions[SKYHOOK]}\n\n')
        visited.append(SKYHOOK)
    else:
        print(f'Welcome back to SKYHOOK!') 
    
    # See if the user wants to play the game for the location
    gameBool = playGame() 

    # If they want to play, clear screen and call the game function
    # If they don't, the program will skip to the next locations part
    if gameBool == 'y': 
        # Clear screen after a second
        clearScreen(1)
        # Add wordle to the games played attributes
        attributes["gamesPlayed"].append("wordle")
        # List of words to pass as argument
        wordChoices = ['H U M O R', 'F R A M E', 'A L O F T', 'P L E A T', 'S H A R D', 'M O I S T', 'T H O S E', 'L I G H T', 'W R U N G', 'C O U L D']
        # Randomize target word
        targetWord = random.choice(wordChoices)
        # Check if they won game and adjust balance accordingly
        if games.wordguess(attributes["character"], targetWord) == 0: 
            econ.updateBalance(20000)
        else:
            econ.updateBalance(0) 
    
    # Ask where they would like to go
    print("\nWhere would you like to go next?")
    # Add request balance option
    print('[0]. REQUEST Balance')
    # Print the connections and possible locations they can go to
    grabConnections(SKYHOOK)
    
    # GEt their input for where they want to go
    userChoice = getNextLocations(['0', '1', '2', '3'])

    # If the userChoice is 0, output the balance but then ask for another input until they give a location to go to using the getNextLocations function
    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(SKYHOOK)
    
        userChoice = getNextLocations(['0', '1', '2', '3'])
    
    # For the possible options, clear screen after one second and call the allocated function
    if userChoice == "1":
        clearScreen(1)
        launchsite(attributes, visited) 
    elif userChoice == "2": 
        clearScreen(1)
        climatizer(attributes, visited)
    elif userChoice == "3": 
        clearScreen(1)
        harvester(attributes, visited)


def harvester(attributes, visited): 
    """
    Function for the harvester location
    Args
        attributes: dictionary
        visited: list
    Returns
        None
    """

    # Check if harvester is in visited
    # If it is, output the description with the welcome, otherwise, only welcome them back
    if HARVESTER not in visited: 
        print(f'{attributes["character"]}, you are at HARVESTER.\n\n{descriptions[HARVESTER]}\n\n') 
        visited.append(HARVESTER)
    else:
        print(f'Welcome back.')
        # Update balance by inflation rate amount
        inflationChoice = random.choice(inflationRates)
        econ.updateBalance(inflationChoice)
        attributes["inflationRates"].append(inflationChoice)

    # Only allow them to continue to the final game if they have over 99999 dollars
    if econ.requestBalance() > 99999:
        # Clear terminal after a second
        clearScreen(1)
        # rr is the result of the russian roulette game
        rr = games.russianroulette(attributes["character"])
        # If the user lost, print out the ascii art and exit game
        if rr == 1 :
            print("""\n____    ____  ______    __    __      __        ______        _______.___________.
\   \  /   / /  __  \  |  |  |  |    |  |      /  __  \      /       |           |
 \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  |    |   (----`---|  |----`
  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  |     \   \       |  |     
    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | .----)   |      |  |     
    |__|     \______/   \______/     |_______| \______/  |_______/       |__|     
                                                                                  """)
            sys.exit() 
        
        # If the user won, print out the ascii art and exit game
        else:
            print("""\n____    ____  ______    __    __     ____    __    ____  ______   .__   __. 
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / /  __  \  |  \ |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   / |  |  |  | |   \|  | 
  \_    _/  |  |  |  | |  |  |  |      \            /  |  |  |  | |  . `  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /   |  `--'  | |  |\   | 
    |__|     \______/   \______/         \__/  \__/     \______/  |__| \__| 
                                                                            """)
            sys.exit() 
    # If they don't have enough money, tell them to go back and get more money
    else:
        print(f"You do not have enough money. Go back and get more money to finish the game.") 

    # Add option to request balance
    print('[0]. REQUEST Balance')
    # Print out connections for harvester
    grabConnections(HARVESTER)
    
    # Get user input for next location
    userChoice = getNextLocations(['0', '1', '2', '3'])

    # If the userChoice is 0, output the balance but then ask for another input until they give a location to go to using the getNextLocations function
    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(HARVESTER)
    
        userChoice = getNextLocations(['0', '1', '2', '3'])

    # For the possible options, clear screen after one second and call the allocated function
    if userChoice == '1': 
        skyhook(attributes, visited) 
    elif userChoice == '2': 
        climatizer(attributes, visited) 
    elif userChoice == '3': 
        countdown(attributes, visited) 