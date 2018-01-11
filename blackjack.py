###########################################################################
###Tony I have no idea how to run the program again so you have to do it###
###########################################################################

# Importing Modules
import math
import random
import sys

# Creating Variables
suits = ['Spades','Hearts','Diamonds','Clubs']
computerCards = []
computerValue = 0
playerCards = []
playerValue = 0

# A Function for Getting a Card
def getCards():
  card = random.randint(1,13)
  if card > 10:
    card = 10
  return card

# A Function to Deal Cards to the Computer
def computerDeal():
  computerCards.append(getCards())
  computerCards.append(getCards())

# A Function to Deal Cards to the Player
def playerDeal():
  playerCards.append(getCards())
  playerCards.append(getCards())
  
# A Function to Print the Player's Cards and the Computer's Cards
def printCards(player, computer):
  print("Your Cards: ", end = '')
  print('%s' % ', '.join(map(str, player)))
  print("Computer's Cards: ", end = '')
  print('%s' % ', '.join(map(str, computer)))

# Dealing and setting the Value
computerDeal()
playerDeal()
playerValue = sum(playerCards)
computerValue = sum(computerCards)

# Introduction, Includes Title, Names, Description and Directions
print("Welcome to Blackjack! The goal of the game is to get as close to 21 as possible, without going over. Type 'h' or 'hit' to draw a card, and type 's' or 'stand' when you're done")
print("Made by Tony and Jia Ming")
printCards(playerCards,computerCards)

# Allows the Player to Draw Cards
while True:
  
  # Exits if the Player Has Busted
  if playerValue > 21:
    print("You've gone over 21! You lost!")
    sys.exit()
  
  # Asking the Player to Hit or Stand
  action = input("h/it or s/tand?")
  action = action.lower()
  
  # Carrying out the Commands of the Player
  if action == "hit" or action == "h":
    playerCards.append(getCards())
    playerValue = sum(playerCards)
    printCards(playerCards, computerCards)
  elif action == "stand" or action == "s":
    break
  else:
    print("I'm not sure what you said, try again!")

# Allowing the Computer to Draw Cards Until It's Busted or It's Score is Higher Than the Player's
while (computerValue < playerValue):
  computerCards.append(getCards())
  computerValue = sum(computerCards)
  if computerValue > 21 and playerValue <= 21:
    printCards(playerCards, computerCards)
    print("You Win! The computer has busted.")
    sys.exit()

# Evaluating The Outcome of the Game
printCards(playerCards, computerCards)
if playerValue > computerValue and playerValue <= 21:
  print("You Win!")
elif playerValue == computerValue and playerValue <= 21:
  print("It's a Tie!")
elif playerValue < computerValue and playerValue <= 21 and computerValue <= 21:
  print("The computer got a higher score, you lost!")
