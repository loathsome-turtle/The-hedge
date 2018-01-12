# Importing Modules
import random
import sys

# Creating Variables
suits = ['Spades','Hearts','Diamonds','Clubs']

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
  
# A Function to Print the Player's Cards and the Computer's First Card
def printPlayerCards(player, computer):
  print("Your Cards: ", end = '')
  print('%s' % ', '.join(map(str, player)))
  print("Computer Cards: ", end = '')
  print(computer[0], end = '')
  print(", X")

# A Function to Print the Player's Cards and the Computer's Cards
def printAllCards(player, computer):
  print("Your Cards: ", end = '')
  print('%s' % ', '.join(map(str, player)))
  print("Computer's Cards: ", end = '')
  print('%s' % ', '.join(map(str, computer)))
  
# A Function to ask if the player would like to play again
def playAgain():
  answer = input("Would you like to play again? Yes/No")
  answer = answer.lower()
  if answer == 'yes' or answer == 'y':
    game()
  if answer == 'no' or answer == 'n':
    print("Thank you for playing. Please come again!")
    sys.exit()
  else:
    print("I'm not quite sure what you said")
    playAgain()
                 
# MAIN GAME FUNCTION
def game():
  #setting variables
  computerCards = []
  computerValue = 0
  playerCards = []
  playerValue = 0

  # Dealing and setting the Value
  computerDeal()
  playerDeal()
  playerValue = sum(playerCards)
  computerValue = sum(computerCards)
  printPlayerCards(playerCards, computerCards)

  # Allows the Player to Draw Cards
  while True:
    
    # Exits if the Player Has Busted
    if playerValue > 21:
      print("You've gone over 21! You lost!")
      sys.exit()
    
    # Asking the Player to Hit or Stand
    action = input("Hit or Stand?")
    action = action.lower()
    
    # Carrying out the Commands of the Player
    if action == "hit" or action == "h":
      playerCards.append(getCards())
      if playerValue > 21:
        printAllCards(playerCards, computerCards)
        print("You've gone over 21! You lost!")
        playAgain()
      playerValue = sum(playerCards)
      printPlayerCards(playerCards, computerCards)
    elif action == "stand" or action == "s":
      break
    else:
      print("I'm not sure what you said, try again!")

  # Allowing the Computer to Draw Cards Until It's Busted or It's Score is Higher Than the Player's
  while (computerValue < playerValue):
    computerCards.append(getCards())
    computerValue = sum(computerCards)
    if computerValue > 21 and playerValue <= 21:
      printAllCards(playerCards, computerCards)
      print("You Win! The computer has busted.")
      playAgain()

  # Evaluating The Outcome of the Game
  printAllCards(playerCards, computerCards)
  if playerValue > computerValue and playerValue <= 21:
    print("You Win!")
    playAgain()
  elif playerValue == computerValue and playerValue <= 21:
    print("It's a Tie!")
    playAgain()
  elif playerValue < computerValue and playerValue <= 21 and computerValue <= 21:
    print("The computer got a higher score, you lost!")
    playAgain()

# Introduction, Includes Title, Names, Description and Directions
try:
  print("Welcome to Blackjack! The goal of the game is to get as close to 21 as possible, without going over. Type 'h' or 'hit' to draw a card, and type 's' or 'stand' when you're done")
  print("Made by Tony and Jia Ming")
  game()
except:
  print("Uh Oh, looks like something isn't working right now. Please try restarting the game.")
  sys.exit()
