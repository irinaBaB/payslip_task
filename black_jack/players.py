class Player:

    def __init__(self):
        self.player_hands = []

    def add_card(self,card):
        self.player_hands.append(card)

    def __str__(self):
        player_cards = ""
        for card in self.player_hands:
            player_cards += card.rank  + ' of ' + card.suit + '\n'
        return player_cards


#player1
#player2 diller
# need to add card to player

