
class BlackJack:

    def __init__(self):
        pass

    def hit_stay(self,deck,actor_hand):
        game = True
        while game == True:
            response = int(input(" Hit or stay? (Hit = 1, Stay = 0)"))
            if response == 1:
                self.hit(deck,actor_hand)
            elif response == 0:
                print(f'You are staying now')
                game=False
                break

    def hit(self,deck,actor_hand):
        new_card = deck.deal_card()
        print(f" this player took the card: {new_card}")
        actor_hand.add_card(new_card)

    def check_winner(self,dealer,player):
        if dealer.value > player.value:
            print(f"Dealer win!!!!")
        elif dealer.value == player.value:
            print("Game is tie..")
        elif player.value > dealer.value:
            print(f"Player win!!!!")


    def show_cards(self,player,dealer):
        print("\nDealer's hand:", *dealer.hand_cards , sep = '\n')
        print("Dealer's hand:", dealer.value)
        print("\nPlayer's hand:", *player.hand_cards, sep='\n')
        print("Player's hand:", player.value)


