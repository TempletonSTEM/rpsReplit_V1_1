"""
Header information
Name: Janze
Class: ICT 9-12
Date: 2021/10/12
Description: Rock, Paper, Scissors game.  Now with easier GamePlay!!
References: tutorial from https://teachyourkidscode.com/python-for-kids-tutorial-2/
"""
from random import randint

#List of options
# rpsChoices  = ["Rock", "Paper", "Scissors"]
rpsChoices  = ["r", "p", "s"]
#Assigning a random option to rpsBot
rpsBot = rpsChoices[randint(0,2)]


#Keep count for points
scorePlayer = 0
scoreBot = 0

rpsContinue = True

#Loop goes on until rpsContinue is false
while(rpsContinue):
    #Ask for user input
    rpsPlayer = input("Rock -r-, Paper -p- or Scissors -s-? or enter Finish -f- to end!\n")

    #Check for scenarios
    if(rpsPlayer == 'f'):
        rpsContinue = False
    elif(rpsPlayer == rpsBot):
        print("Tie!")
    elif(rpsPlayer == "r"):
        if(rpsBot == "p"):
            print("You lose! Paper covers Rock")
            scoreBot = scoreBot + 1 
        else:
            print("You win! Rock smashes Scissors")
            scorePlayer = scorePlayer + 1
    elif(rpsPlayer == "p"):
        if(rpsBot == "s"):
            print("You lose! Scissors cut Paper")
            scoreBot = scoreBot + 1
        else:
            print("You win! Paper covers Rock")
            scorePlayer = scorePlayer + 1
    elif(rpsPlayer == "s"):
        if(rpsBot == "r"):
            print("You lose! Rock smashes Scissors")
            scoreBot = scoreBot + 1
        else:
            print("You win! Scissors cut Paper")
            scorePlayer = scorePlayer + 1
    else:
        print("That's not a valid play. Check your spelling!")
    #Assigning a random option to rpsBot
    rpsBot = rpsChoices[randint(0,2)]
    print('Next Turn')

#Printing final points
print("Final Points")
print("Player: ", scorePlayer)
print("Computer: ", scoreBot)