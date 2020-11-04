
from cards import Card
from cards import values
from cards import Deck
from players import Player
from blackjack import BlackJack


input_value = input ("enter the value 1 or 2 : ")
# creating a deck of the cards
deck = Deck()
blackjack = BlackJack()
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
    print("Player bla bla has got:\t\n {},".format(player)[0:-1] + "you are currently at {}:".format(player.value))
    blackjack.hit_stay(deck,player)
    if player.value > 21:
        print ("\n")
        print ("You are at currently at Bust!")
        print("\t With the hand :{}".format(player.value),*player.player_hands,sep='\n')
        print("Dealer win!!!!")
        break


    elif player.value == 21:
        print(f"You win!!!!")
        game= False

    print ("\n")
    print((f"Dealer** has got: \n{dealer} \n\t you are currently at: { dealer.value}"))
    while dealer.value <=17:
        dealer_card = deck.deal_card()
        dealer.add_card(dealer_card)
        print(f"****You took the card: {dealer_card}")
        print((f"****You got: \n{dealer} \n\t you are currently at: { dealer.value}"))

    blackjack.hit_stay(deck,dealer)
    print ("\n")
    if dealer.value >21:
        print("You are at currently at Bust!")
        print((f"Dealer has got: \n{dealer} \n\t you are currently at: { dealer.value}"))
        print("Player win!!!!")
        break

    elif dealer.value == 21:
        print(f"Dealer win!!!!")
        game= False

    if dealer.value > player.value:
        print(f"Dealer win!!!!")
    elif dealer.value == player.value == 21:
        print("Game is tie..")
    elif player.value > dealer.value:
        print(f"Player win!!!!")


input_value = input ("enter the value: ")

if input_value == '2':
    print("end of the game")


