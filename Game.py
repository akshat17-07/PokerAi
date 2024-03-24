"""
This class would run one game of poker. I had decided to create the game seprately than table so that I could run more than one games at once
"""
from Player_Class import *
import random

def create_deck():
    suits = ["H", "D", "S", "C"]
    number = ["A", "K", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    cards = []
    for j in suits:
        for i in number:
            cards.append(i+j)
    return cards

def create_cards(nums, deck):
    dealed_cards = []
    for i in range(nums):
        dealed_cards.append([])
        temp = random.choice(deck)
        dealed_cards[-1].append(temp)
        deck.remove(temp)
        temp = random.choice(deck)
        dealed_cards[-1].append(temp)
        deck.remove(temp)
    return (dealed_cards, deck)
def game(players):
    deck = create_deck()
    dealed_cards, deck = create_cards(len(players), deck)
    print(dealed_cards, deck)