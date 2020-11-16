from cards import values

class Person:

    def __init__(self):
        self.hand_cards = []
        self.value = 0
        self.aces = 0


    def add_card(self,card):
        self.hand_cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.aces+=1
        if self.value >21 and self.aces>0:
            self.aces -=1
            self.value -=10

    def clear_hands(self):
        self.hand_cards.clear()
        self.value=0
        self.aces = 0




    def __str__(self):
        player_cards = ""
        for card in self.hand_cards:
            player_cards += card.rank  + ' of ' + card.suit + '\n'
        return player_cards







