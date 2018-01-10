import math 
import random

cardValues = [1,2,3,4,5,6,7,8,9,10,11,12,13]
suits = ['Spades','Hearts','Diamonds','Clubs']

computerCards = []
computerValue = 0
playerCards = []
playerValue = 0

def deal():
  computerCards = [cardValues[random.randint()], cardValues[random.randint()]]
  
  
