from cards import values

class Person:

    def __init__(self):
        self.person_hands = []
        self.value = 0
        self.aces = 0


    def add_card(self,card):
        self.person_hands.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.aces+=1
        if self.value >21 and self.aces>0:
            self.aces -=1
            self.value -=10

    def clear_hands(self):
        self.person_hands.clear()
        self.value=0
        self.aces = 0




    def __str__(self):
        player_cards = ""
        for card in self.person_hands:
            player_cards += card.rank  + ' of ' + card.suit + '\n'
        return player_cards





    def show_cards(self,actor):

        print("Player has got: \n\t {},".format(actor) + "you are currently at {}:".format(actor.value))





