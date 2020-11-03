
from cards import Card
from cards import values
from cards import Deck
from players import Player

game = True


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

#adjust for ace
player.ace_adjust()
dealer.ace_adjust()


while input_value =='1':
    print(f"Player has got: \n{player} \n\t you are currently at : { player.value}")
    print((f"Dealer has got: \n{dealer} \n\t you are currently at: { dealer.value}"))

    # adding hit or stand functions for player
    while game == True:
        response = int(input("Hit or stay? (Hit = 1, Stay = 0)"))
        if response == 1:
            new_card = deck.deal_card()
            print(new_card)

            print(f"You took the card {new_card}")
        elif response ==0:
            print('Player is staying, now is dealer turn')
            game == False
            break


    input_value = input ("enter the value: ")

if input_value == '2':
    print("end of the game")


