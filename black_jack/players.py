from cards import values

class Player:

    def __init__(self):
        self.player_hands = []
        self.value = 0


    def add_card(self,card):

        self.player_hands.append(card)
        self.value+=values[card.rank]

    def __str__(self):
        player_cards = ""
        for card in self.player_hands:
            player_cards += card.rank  + ' of ' + card.suit + '\n'
        return player_cards


#player1
#player2 diller
# need to add card to player

