import random
from random import shuffle

suits=('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

# 1. Setting up a Card class:

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck():

    def __init__(self):
        self.cards= []

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit,rank)
                self.cards.append(new_card)

    def __str__(self):
        all_cards = ""
        for card in self.cards:
            all_cards += card.rank  + ' of ' + card.suit + '\n'
        return all_cards

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
         return self.cards.pop()
















