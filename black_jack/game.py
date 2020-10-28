from random import shuffle

suits=('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


# 1. Setting up a Card class:

class Card():

    def __init__(self,suit,rank):
        suit = suit
        rank = rank

    def __str__(self):
        return self.rank + 'of' + self.suit


