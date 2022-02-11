import random
import libs.economy as econ
import libs.games as games 

HARVESTER = "HARVESTER"
SKYHOOK = "SKYHOOK"
COUNTDOWN = "COUNTDOWN"
LAVASIPHON = "LAVA SIPHON"
GEYSER = "GEYSER"
CLIMATIZER = "CLIMATIZER"
THERMALSTATION = "THERMAL STATION"
EPICENTER = "EPICENTER"
LAUNCHSITE = "LAUNCHSITE" 

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

inflationRates = econ.generateRates(5) 

def grabConnections(place): 
    for i in range(1, len(connections[place.upper()]) +1 ): 
        print(f'[{i}]. {connections[place.upper()][i-1]}') 

def getNextLocations(possibleLocations):
    nextLoc = input(f'Enter the number allocated to the location you would like to visit: ') 
    while nextLoc not in possibleLocations: 
        nextLoc = input('That is not a possible location. Enter a valid location or 0 for request balance: ') 
    
    return nextLoc

def playGame():
    choice = input("Would you like to play the game for this location? (y/n): ") 
    choiceOptions = ['y', 'n']
    while choice not in choiceOptions: 
        choice = input("Would you like to play the game for this location? (y/n): ") 
    
    return choice 

def launchsite(attributes, visited): 
    if LAUNCHSITE not in visited: 
        print(f'{attributes["character"]}, you are at LAUNCHSITE.\n\n{descriptions[LAUNCHSITE]}\n\nThere is not much to do here... Where would you like to go next? You could also request balance.') 
        visited.append(LAUNCHSITE)
    else:
        print(f'Welcome back. What would you like to do next?')
        inflationChoice = random.choice(inflationRates)
        econ.updateBalance(inflationChoice)
        attributes["inflationRates"].append(inflationChoice)

    print('[0]. REQUEST Balance')
    grabConnections(LAUNCHSITE)
    
    userChoice = getNextLocations(['0', '1', '2', '3', '4'])

    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(LAUNCHSITE)
    
        userChoice = getNextLocations(['0', '1', '2', '3', '4'])

    if userChoice == '1': 
        geyser(attributes, visited) 
    elif userChoice == '2': 
        lavasiphon(attributes, visited) 
    elif userChoice == '3': 
        epicenter(attributes, visited) 
    elif userChoice == '4': 
        climatizer(attributes, visited) 

def geyser(attributes, visited): 

    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    if GEYSER not in visited:
        print(f'{attributes["character"]}, you are at GEYSER.\n\n{descriptions[GEYSER]}\n\n')
        visited.append(GEYSER)
    else:
        print(f'Welcome back to GEYSER!') 
    
    gameBool = playGame() 

    if gameBool == 'y': 
        attributes["gamesPlayed"].append("rockpaperscissors")
        if games.rockpaperscissors(attributes["character"]) == 0: 
            econ.updateBalance(50000)
        else:
            econ.updateBalance(25000) 
    
    print("Where would you like to go next?")
    print('[0]. REQUEST Balance')
    grabConnections(GEYSER)
    
    userChoice = getNextLocations(['0', '1', '2'])

    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(GEYSER)
    
        userChoice = getNextLocations(['0', '1', '2'])
    
    if userChoice == "1":
        launchsite(attributes, visited) 
    elif userChoice == "2": 
       thermalstation(attributes, visited)

def thermalstation(attributes, visited): 

    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    if THERMALSTATION not in visited:
        print(f'{attributes["character"]}, you are at THERMAL STATION.\n\n{descriptions[THERMALSTATION]}\n\n')
        visited.append(THERMALSTATION)
    else:
        print(f'Welcome back to THERMAL STATION!') 
    
    gameBool = playGame() 

    if gameBool == 'y': 
        attributes["gamesPlayed"].append("cf")
        if games.cf(attributes["character"], random.randint(25, 75)) == 0: 
            econ.updateBalance(30000)
        else:
            econ.updateBalance(0) 
    
    print("Where would you like to go next?")
    print('[0]. REQUEST Balance')
    grabConnections(THERMALSTATION)
    
    userChoice = getNextLocations(['0', '1', '2'])

    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(THERMALSTATION)
    
        userChoice = getNextLocations(['0', '1', '2'])
    
    if userChoice == "1":
        geyser(attributes, visited) 
    elif userChoice == "2": 
        epicenter(attributes, visited)

def epicenter(attributes, visited): 

    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    if EPICENTER not in visited:
        print(f'{attributes["character"]}, you are at EPICENTER.\n\n{descriptions[EPICENTER]}\n\n')
        visited.append(EPICENTER)
    else:
        print(f'Welcome back to EPICENTER!') 
    
    gameBool = playGame() 

    if gameBool == 'y': 
        attributes["gamesPlayed"].append("guessing")
        upperBound = random.randint(100, 1000) 
        if games.guessing(attributes["character"], upperBound) == 0: 
            econ.updateBalance(upperBound * 1000)
        else:
            econ.updateBalance(0) 
    
    print("Where would you like to go next?")
    print('[0]. REQUEST Balance')
    grabConnections(EPICENTER)
    
    userChoice = getNextLocations(['0', '1', '2', '3'])

    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(EPICENTER)
    
        userChoice = getNextLocations(['0', '1', '2', '3'])
    
    if userChoice == "1":
        launchsite(attributes, visited) 
    elif userChoice == "2": 
        thermalstation(attributes, visited)
    elif userChoice == "3": 
        climatizer(attributes, visited)

def climatizer(attributes, visited): 

    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    if CLIMATIZER not in visited:
        print(f'{attributes["character"]}, you are at CLIMATIZER.\n\n{descriptions[CLIMATIZER]}\n\n')
        visited.append(CLIMATIZER)
    else:
        print(f'Welcome back to CLIMATIZER!') 
    
    gameBool = playGame() 

    if gameBool == 'y': 
        attributes["gamesPlayed"].append("memory")
        memLength = random.randint(5, 10) 
        if games.memory(attributes["character"], memLength) == 0: 
            econ.updateBalance(memLength * 1300)
        else:
            econ.updateBalance(0) 
    
    print("Where would you like to go next?")
    print('[0]. REQUEST Balance')
    grabConnections(CLIMATIZER)
    
    userChoice = getNextLocations(['0', '1', '2', '3', '4', '5'])

    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(CLIMATIZER)
    
        userChoice = getNextLocations(['0', '1', '2', '3', '4', '5'])
    
    if userChoice == "1":
        epicenter(attributes, visited) 
    elif userChoice == "2": 
        launchsite(attributes, visited)
    elif userChoice == "3": 
        skyhook(attributes, visited)
    elif userChoice == "4": 
        countdown(attributes, visited)
    elif userChoice == "5": 
        harvester(attributes, visited)

def countdown(attributes, visited): 

    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    if COUNTDOWN not in visited:
        print(f'{attributes["character"]}, you are at COUNTDOWN.\n\n{descriptions[COUNTDOWN]}\n\n')
        visited.append(COUNTDOWN)
    else:
        print(f'Welcome back to COUNTDOWN!') 
    
    gameBool = playGame() 

    if gameBool == 'y': 
        attributes["gamesPlayed"].append("paradox")
        userResult = games.envelopeParadox(attributes["character"]) 
        if userResult == 0: 
            econ.updateBalance(10000)
        else:
            econ.updateBalance(userResult) 
    
    print("Where would you like to go next?")
    print('[0]. REQUEST Balance')
    grabConnections(COUNTDOWN)
    
    userChoice = getNextLocations(['0', '1', '2'])

    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(COUNTDOWN)
    
        userChoice = getNextLocations(['0', '1', '2'])
    
    if userChoice == "1":
        climatizer(attributes, visited) 
    elif userChoice == "2": 
        harvester(attributes, visited)

def lavasiphon(attributes, visited): 

    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    if LAVASIPHON not in visited:
        print(f'{attributes["character"]}, you are at LAVA SIPHON.\n\n{descriptions[LAVASIPHON]}\n\n')
        visited.append(LAVASIPHON)
    else:
        print(f'Welcome back to LAVA SIPHON') 
    
    gameBool = playGame() 

    if gameBool == 'y': 
        attributes["gamesPlayed"].append("dice")
        gameResult = games.dice(attributes["character"], "LAVA SIPHON", random.randint(6, 12))
        if  gameResult == 0: 
            econ.updateBalance(5000)
        elif gameResult == 1:
            econ.updateBalance(500)
        elif gameResult == 2:
            econ.updateBalance(2500) 
    
    print("Where would you like to go next?")
    print('[0]. REQUEST Balance')
    grabConnections(LAVASIPHON)
    
    userChoice = getNextLocations(['0', '1', '2'])

    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(LAVASIPHON)
    
        userChoice = getNextLocations(['0', '1', '2'])
    
    if userChoice == "1":
        launchsite(attributes, visited) 
    elif userChoice == "2": 
        skyhook(attributes, visited)

def skyhook(attributes, visited): 

    econ.updateBalance(int(random.choice(inflationRates) * econ.requestBalance()))

    if SKYHOOK not in visited:
        print(f'{attributes["character"]}, you are at SKYHOOK.\n\n{descriptions[SKYHOOK]}\n\n')
        visited.append(SKYHOOK)
    else:
        print(f'Welcome back to SKYHOOK!') 
    
    gameBool = playGame() 

    if gameBool == 'y': 
        attributes["gamesPlayed"].append("wordle")
        wordChoices = ['H U M O R', 'F R A M E', 'A L O F T', 'P L E A T', 'S H A R D', 'M O I S T', 'T H O S E', 'L I G H T', 'W R U N G', 'C O U L D']
        targetWord = random.choice(wordChoices)
        if games.wordguess(attributes["character"], targetWord) == 0: 
            econ.updateBalance(20000)
        else:
            econ.updateBalance(0) 
    
    print("Where would you like to go next?")
    print('[0]. REQUEST Balance')
    grabConnections(SKYHOOK)
    
    userChoice = getNextLocations(['0', '1', '2', '3'])

    while userChoice == '0': 
        print(econ.requestBalance())
        print('[0]. REQUEST Balance')
        grabConnections(SKYHOOK)
    
        userChoice = getNextLocations(['0', '1', '2', '3'])
    
    if userChoice == "1":
        launchsite(attributes, visited) 
    elif userChoice == "2": 
        climatizer(attributes, visited)
    elif userChoice == "3": 
        harvester(attributes, visited)