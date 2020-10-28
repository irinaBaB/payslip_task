https://github.com/MYOB-Technology/General_Developer/blob/main/katas/kata-foundational/foundational-kata-blackjack.md

	1. Create card class to understand logic of suits, ranks, values and later we can use that logic to compare the value of the player cards
	2. Create a deck of 52 cards
	suits=('Hearts','Diamonds','Spades','Clubs')
	ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
	values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
	3. Adding Player logic (Player Hand) - player 1
		a. Shuffle deck
		b. Receive 2 cards
		c. Hitting / staying - need to calculate the cards value

	4. Dealer logic (Dealer Hand) player 2

    5. Score Ace cases: Ace can be worth 1 or 11
       Score general

Game Logic:

• If the player has blackjack (21), they win, unless the dealer also has blackjack, in which case the game is a tie.  WIN or TIE
• If the dealer busts and the player doesn't, the player wins. BUST is over 21
• If the player busts, the dealer wins.
• If the player and the dealer both don't bust, whoever is closest to 21 wins.

Winner logic:

Not sure yet
