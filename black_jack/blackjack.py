from players import Player
from cards import Deck



class BlackJack:

    def __init__(self):
        pass

    def hit_stay(self,deck,actor):
        game = True
        while game == True:
            response = int(input(" Hit or stay? (Hit = 1, Stay = 0)"))
            if response == 1:
                new_card = deck.deal_card()
                print(f"You took the card: {new_card}")
                actor.add_card(new_card)
                actor.ace_adjust()

            elif response ==0:
                print(f'{actor} is staying, now is dealer turn')
                game = False

            #Adjusting the total score - player

            print(f"\tPlayer with hand : \t\n{actor} \n\t you are currently at : { actor.value}")