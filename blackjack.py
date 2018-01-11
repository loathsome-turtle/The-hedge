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

while (playerValue < 21):
  playerValue = sum(playerCards)
  computerValue = sum(computerCards)
