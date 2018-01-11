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
playerValue = sum(playerCards)
computerValue = sum(computerCards)

print("Welcome to Blackjack! The goal of the game is to get as close to 21 as possible, without going over. Type 'h' or 'hit' to draw a card, and type 's' or 'stand' when you're done")
print("Your Cards: "),
print('[%s]' % ', '.join(map(str, playerCards)))
print("Computer's Cards: "),
print('[%s]' % ', '.join(map(str, computerCards)))

while True:
  action = input("h/it or s/tand?")
  action = action.lower()
  if playerValue > 21:
    print("You've gone over 21! You lost!")
    break
  if action == "hit" or action == "h":
    playerCards.append(getCards())
    playerValue = sum(playerCards)
    print(playerCards)
    print(computerCards)
  elif action == "stand" or action == "s":
    break
  else:
    print("I'm not sure what you said, try again!")
       
while (computerValue < playerValue):
  computerCards.append(getCards())
  computerValue = sum(computerCards)
  if computerValue == 21:
    break
    
if playerValue > computerValue and playerValue <= 21:
  print("You Win!")
elif playerValue == computerValue and playerValue <= 21:
  print("It's a Tie!")
elif playerValue < computerValue and playerValue <= 21:
  print("The computer got a higher score, you lost!")
