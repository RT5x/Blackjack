import time
import random
import sys
from sys import exit
from cards import types
from cards import suits
from cards import deck

#Blackjack game, by RT5x
#Copy code into Python IDE and play in the terminal

print("Welcome to Blackjack! ")
print("   ")
time.sleep(1.0)
print("Here, let me deal the cards out first...")
time.sleep(2)
print("   ")
print("Here are your two cards... Only you can see them.")
card1 = random.choice(types)
card2 = random.choice(types)
print(card1)
print(card2)
total_p = int(card1) + int(card2)
print("Your current total is " + str(total_p) + ".")
#Outputs a random card choice from the deck

time.sleep(2.0)
choice1 = int(input("Would you like to hit or stand? (Type '1' to hit, and type '2' to stand)."))

if choice1== 1:
    print("Here is your new card:")

    card3 = random.choice(types)
    print(card3)
    time.sleep(1.0)
    total_p += card3
    print("Your current total is " + str(total_p) + ".")

    time.sleep(1.5)

    print("Alright, let me show you my cards.")
    time.sleep(1.0)
    card_d1 = random.choice(types)
    card_d2 = random.choice(types)
    total_d = card_d1 + card_d2
    print(card_d1)
    print(card_d2)
    time.sleep(0.5)
    print("The dealer's current total is " + str(total_d) + ".") 
    time.sleep(0.5)
if int(choice1)==2:
  time.sleep(1.0)
  print("Alright, let me show you my cards.")

  card_d1 = random.choice(types)
  card_d2 = random.choice(types)
  total_d = card_d1 + card_d2
  
  print(card_d1)
  print(card_d2)
  print("The dealer's current total is " + str(total_d) + ".")    

else:
  print(" ")
  pass

if int(total_p) > 21:
      print("You went over 21! Dealer wins!")
      sys.exit()
if int(total_p) == 21:
    print("21! You win!")
    sys.exit()
if int(total_d) == 21:
    print("21! Dealer wins!")
    sys.exit()

if int(total_d) > 21:
      print("Dealer busts! You win!")
      sys.exit()

if int(total_d) > int(total_p):
    print()
    sys.exit()
if int(total_d) < int(total_p):
    sys.exit()
else:
    print("Error, please restart the game.")
    sys.exit("Error, please restart the game.")

choice2 = int(input("Would you like to hit or stand? (Type '1' to hit, and type '2' to stand)."))

if choice2 == 1:
  print("Here is your new card:")
  card4 = random.choice(types)
  print(card4)
  total_p += card4
  time.sleep(0.5)
  print("Your current total is " + str(total_p) + ".")
  time.sleep(1.0)
  print("As a reminder, the dealer's new total is " + str(total_d) + ".") 
if choice2 == 2:
  time.sleep(0.8)
  print("Now I will choose a new card.")
  time.sleep(0.5)
  card_d3 = random.choice(types)
  total_d += card_d3
  time.sleep(0.82)
  print("The dealer's current total is " + str(total_d) + ".") 
  time.sleep(1.0)

while int(total_p) < 21:
  if total_p > total_d:
    break
    print("You win!")
  pass

if int(total_p) > 21:
      print("You went over 21! Dealer wins!")
      sys.exit()
if int(total_p) == 21:
    print("21! You win!")
    sys.exit()
if int(total_d) == 21:
    print("21! Dealer wins!")
    sys.exit()
if int(total_d) > 21:
      print("Dealer busts! You win!")
      sys.exit()
if int(total_d) > int(total_p):
    print()
    sys.exit()
if int(total_d) < int(total_p):
    sys.exit()
else:
    print("Error, please restart the game.")
    sys.exit("Error, please restart the game.")
choice3 = int(input("Would you like to hit or stand? (Type '1' to hit, and type '2' to stand)."))

if choice3 ==1:
  print("Here is your new card:")
  card5 = random.choice(types)
  print(card5)
  total_p += card5
  time.sleep(0.5)
  print("Your current total is " + str(total_p) + ".")
  time.sleep(1.0)
  print("As a reminder, the dealer's new total is " + str(total_d) + ".")
if choice3 ==2:
  time.sleep(0.8)
  print("Now I will choose a new card.")
  card_d4 = random.choice(types)
  total_d += card_d4
  time.sleep(0.5)
  print("The dealer's current total is " + str(total_d) + ".") 

while int(total_p) < 21:
  if total_p > total_d:
    break
    print("You win!")
  pass

if int(total_p) > 21:
      print("You went over 21! Dealer wins!")
      sys.exit()
if int(total_p) == 21:
    print("21! You win!")
    sys.exit()
if int(total_d) == 21:
    print("21! Dealer wins!")
    sys.exit()
if int(total_d) > 21:
      print("Dealer busts! You win!")
      sys.exit()
if int(total_d) > int(total_p):
    print()
    sys.exit()
if int(total_d) < int(total_p):
    sys.exit()
else:
    print("Error, please restart the game.")
    sys.exit("Error, please restart the game.")
