
from cards import Card
from cards import values
from cards import Deck
from players import Player


input_value = input ("enter the value 1 or 2 : ")
# creating a deck of the cards
deck = Deck()
#introducing two players player and dealer
player = Player()
dealer= Player()
#shuffle deck
deck.shuffle()
#player taking 2 cards
player.add_card(deck.deal_card())
player.add_card(deck.deal_card())
#dealer taking 2 cards
dealer.add_card(deck.deal_card())
dealer.add_card(deck.deal_card())
while input_value =='1':
    print(f"Player has got: \n{player} \n\t With score: { player.value}")
    print((f"Dealer has got: \n{dealer} \n\t With score: { dealer.value}"))
    input_value = input ("enter the value: ")

if input_value == '2':
    print("end of the game")


