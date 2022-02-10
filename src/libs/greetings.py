def titleText():
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
    print(titleText())
    print(f"\n\nWelcome to the Apex Games...\nYou are here because you have been conscripted by The Syndicate. You're task in these games is to travel through the map and face the trials till the end location, where you will only be allowed to exit if you have enough liquid capital to do so. Don't let the others know, but a hint from The Syndicate - get a paper and make the graph as you travel around the map. A word for the wise - as an extra challenge try to see if you can calculate the shortest possible route.\n\nTHE ECONOMY SYSTEM: At almost every location, you will face a challenge and you must pay a fee to accept the challenge, but will be rewarded generously for succeeding. However, there is a catch! Every time you move to a new location, a day passes and your balance inflates or deflates at the same rate as a randomized crypto or stock that day. I'm guessing you can see why not many people escape The Syndicate...\n\n")

def accept():
    isAccept = "x"
    while isAccept != "Y" and isAccept != "N": 
        isAccept = input("Do you accept the games? (Y/N) ")
    
    if isAccept == "Y": 
        return True 
    else:
        return False 

# Load functions 
if __name__ == "__main__":
    titleText() 
    introduction()
    accept()