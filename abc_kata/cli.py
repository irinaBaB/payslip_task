from kata_abc import user_input
from kata_abc import can_make_word

word=user_input()
# print(f"your word : {word}")
while word !='1':
    can_make_word(word)
    word=user_input()


