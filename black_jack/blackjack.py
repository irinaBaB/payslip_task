
class BlackJack:

    def __init__(self):
        pass

    def hit_stay(self,deck,actor):
        isHitAgain = True
        while isHitAgain and not self.is_actor_bust(actor):
            response = int(input("Hit or stay? (Hit = 1, Stay = 0)"))
            if response == 1:
                self.hit(deck,actor)
            elif response == 0:
                print(f'You are staying now')
                isHitAgain = False
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


    def is_actor_bust(self,actor):
        return actor.value > 21

    def is_actor_blackjack(self,actor):
        return actor.value==21






