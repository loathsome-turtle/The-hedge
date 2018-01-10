import math 
import random

suits = ['Spades','Hearts','Diamonds','Clubs']

computerCards = []
computerValue = 0
playerCards = []
playerValue = 0

def deal():
  computerCards.append(random.randint(1,10))

deal()
print(computerCards)
