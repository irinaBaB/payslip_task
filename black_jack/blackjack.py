from players import Person
from cards import Deck



class BlackJack:

    def __init__(self):
        pass

    def hit_stay(self,deck,actor_hand):
        game = True
        while game == True:
            response = int(input(" Hit or stay? (Hit = 1, Stay = 0)"))
            if response == 1:
                new_card = deck.deal_card()
                print(f" this player took the card: {new_card}")
                actor_hand.add_card(new_card)
                if actor_hand.value > 21:

                    game=False
                    break

            elif response == 0:
                print(f'You are staying now')
                game=False
                break

    def check_winner(self,dealer,player):
        if dealer.value > player.value:
            print(f"Dealer win!!!!")
        elif dealer.value == player.value:
            print("Game is tie..")
        elif player.value > dealer.value:
            print(f"Player win!!!!")
