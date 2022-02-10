import libs.economy as econ

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
print(inflationRates)

def grabConnections(place): 
    for i in range(1, len(connections[place.upper()]) +1 ): 
        print(f'[{i}]. {connections[place.upper()][i-1]}') 

def getNextLocations(possibleLocations):
    nextLoc = input(f'Enter the number allocated to the location you would like to visit: ') 
    while nextLoc not in possibleLocations: 
        nextLoc = input('That is not a possible location. Enter a valid location or 0 for request balance: ') 
    
    return nextLoc

def launchsite(attributes, visited): 
    print(inflationRates)
    if LAUNCHSITE not in visited: 
        print(f'{attributes["character"]}, you are at LAUNCHSITE.\n\n{descriptions[LAUNCHSITE]}\n\nThere is not much to do here... Where would you like to go next? You could also request balance.') 

        visited.append(LAUNCHSITE)
    else:
        print(f'Welcome back. What would you like to do next?')

    print('[0]. REQUEST Balance')
    grabConnections(LAUNCHSITE)
    
    userChoice = getNextLocations(['0', '1', '2', '3', '4'])

    print(userChoice)
    if userChoice == '0':
        print(econ.requestBalance())
    elif userChoice == '1': 
        geyser() 
    elif userChoice == '2': 
        lavasiphon() 
    elif userChoice == '3': 
        epicenter() 
    elif userChoice == '4': 
        climatizer() 



    

    