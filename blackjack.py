import math 
import random

suits = ['Spades','Hearts','Diamonds','Clubs']

computerCards = []
computerValue = 0
playerCards = []
playerValue = 0

def faceCards(card):
  if card > 10:
    card = 10
    return card

def computerDeal():
  computerCards.append(random.randint(1,13))
  computerCards.append(random.randint(1,13))

def playerDeal():
  playerCards.append(random.randint(1,13))
  playerCards.append(random.randint(1,13))

computerDeal()
playerDeal()
print(computerCards)
print(playerCards)
