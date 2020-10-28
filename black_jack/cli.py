
from cards import Card
from cards import values
from cards import Deck
from players import Player


input_value = input ("enter the value: ")
deck = Deck()
player_hands = Player()
dealer_hands = Player()
deck.shuffle()
single_card = deck.deal_card()
player_hands.add_card(single_card)
player_hands.add_card(single_card)
dealer_hands.add_card(single_card)
dealer_hands.add_card(single_card)
while input_value =='1':
#these won't print me anything as 'Player' not iterable - need to fix it
    for card in player_hands:
        print(card)
    for card in dealer_hands:
        print(card)
    input_value = input ("enter the value: ")

if input_value == '2':
    print("end of the game")


