
from cards import Card
from cards import values
from cards import Deck
from players import Player


input_value = input ("enter the value 1 or 2 : ")
deck = Deck()
player = Player()
dealer= Player()
deck.shuffle()
player.add_card(deck.deal_card())
player.add_card(deck.deal_card())
dealer.add_card(deck.deal_card())
dealer.add_card(deck.deal_card())
while input_value =='1':
    print(player, player.value)
    print(dealer,dealer.value)
    input_value = input ("enter the value: ")

if input_value == '2':
    print("end of the game")


