import random

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
    else:
        print(f'As expected, I managed to win. Get on your way now, fool, for I cannot be challenged.')


def guessingGame(name, bound): 
    

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
            return "lose" 
        
    return "win" 
        
