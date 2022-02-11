import random
import os

def initBalance(): 
    print(f'You will be given three choices for your intial balance. While it may be tempting to choose the highest value keep in mind that your balance is randomly inflated and deflated every move.\n\nHere are your chocies: $1000, $5000, $10000.\n')

    balanceStr = input("What would you like your initial balance to be (enter the numerical option)? ") 

    options = ["1000", "5000", "10000"]

    while balanceStr not in options: 
        balanceStr = input('That is not a valid option - enter a valid option: ') 

    print(os.getcwd())
    file = open("./src/libs/balance.txt", "r+") 
    file.truncate(0) 
    file.write(balanceStr) 
    file.close() 

def requestBalance(): 
    with open('./src/libs/balance.txt') as f:
        contents = f.read()
        return int(float(contents))

def updateBalance(amount):
    with open('./src/libs/balance.txt') as f:
        contents = f.read()
  
    file = open("./src/libs/balance.txt", "r+") 
    file.truncate(0) 
    file.write(str(int(float(contents))+amount))
    file.close() 

def generateRates(amount):
    rates = [] 

    rates.append(round(random.uniform(00.20, 00.99), 2))

    for i in range(amount - 1):
        rates.append(round(random.uniform(00.20, 20.00), 2))
    
    return rates

