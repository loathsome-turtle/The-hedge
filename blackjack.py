import math 
import random

suits = ['Spades','Hearts','Diamonds','Clubs']

computerCards = []
computerValue = 0
playerCards = []
playerValue = 0

def getCards():
  card = random.randint(1,13)
  if card > 10:
    card = 10
  return card

def computerDeal():
  computerCards.append(getCards())
  computerCards.append(getCards())

def playerDeal():
  playerCards.append(getCards())
  playerCards.append(getCards())
  
computerDeal()
playerDeal()
print(computerCards)
print(playerCards)

playerValue = sum(playerCards)
computerValue = sum(computerCards)

while (playerValue < 21):
  action = input("h/it or s/tand?")
  action = action.lower()
  if action == "hit" or action == "h":
    playerCards.append(getCards())
    playerValue = sum(playerCards)
  elif action == "stand" or action == "s":
    break
  else:
    print("I'm not sure what you said, try again!")

while (computerValue < playerValue):
  computerCards.append(getCards())
  computerValue = sum(computerCards)
