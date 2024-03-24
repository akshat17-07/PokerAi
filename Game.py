"""
This class would run one game of poker. I had decided to create the game seprately than table so that I could run more than one games at once
"""
from Player_Class import *

def create_deck():
    suits = ["H", "D", "S", "C"]
    number = ["A", "K", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    cards = []
    for j in suits:
        for i in number:
            cards.append(i+j)
    return cards

def create_cards(nums):
    pass
def game(players):
    deck = create_deck()
    cards = create_cards(len(players))