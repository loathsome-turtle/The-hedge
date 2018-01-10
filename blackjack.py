import math 
import random

suits = ['Spades','Hearts','Diamonds','Clubs']

computerCards = []
computerValue = 0
playerCards = []
playerValue = 0

def computerDeal():
  computerCards.append(random.randint(1,13))
  computerCards.append(random.randint(1,13))


deal()
print(computerCards)
