
# 1. get collection of the blocks
# 2. be able to prinnt each row (item) from collection


blocks =['BO','XK','DQ','CP','NA','GT','RE','TG','QD','FS','JW','HU','VI','AN','OB','ER','FS','LY','PC','ZM']


new_list=[]
created_word=[]
def can_make_word(word):
        for w in word.upper():
            for block in blocks:
                if w in block and block not in new_list:
                    #create a counter of the word that I do not use same letter again
                    new_list.append(block)
                    created_word.append(w)
                    print(f'letter {w},{block} is in the list ')
                    break

                else:
                    print('FALSE')


        if created_word == word:
              print(created_word)
              print('TRUE')


# Currently it's checking every time same letter multiple times in the blocks

def user_input():
    word = input("What is your word?: ")
    return word.upper()

