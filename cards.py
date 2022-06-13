import random
from itertools import product

#this file contains all of the cards in the standard 52-card deck
#♥, ♠, ♣, ♦ are Hearts, Spades,  Clubs, and Diamonds respectively


Ace = 1
Jack = 10
Queen = 10
King = 10


types = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]
suits = ['♥', '♠', '♣', '♦']

deck = list(product(types, suits))

deck1 = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]

