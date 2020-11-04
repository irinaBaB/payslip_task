from cards import values

class Player:

    def __init__(self):
        self.player_hands = []
        self.value = 0
        self.aces = 0


    def add_card(self,card):
        self.player_hands.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.aces+=1
        if self.value >21 and self.aces>0:
            self.aces -=1
            self.value -=10

    
    def __str__(self):
        player_cards = ""
        for card in self.player_hands:
            player_cards += card.rank  + ' of ' + card.suit + '\n'
        return player_cards



