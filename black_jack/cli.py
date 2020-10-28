
from game import Card
from game import values
from game import Deck


input_value = input ("enter the value: ")
deck = Deck()
while input_value =='1':
    print(deck)
    input_value = input ("enter the value: ")

if input_value == '2':
    print("end of the game")


