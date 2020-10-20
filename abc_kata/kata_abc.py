
# 1. get collection of the blocks
# 2. be able to prinnt each row (item) from collection


blocks =['BO','XK','DQ','CP','NA','GT','RE','TG','QD','FS','JW','HU','VI','AN','OB','ER','FS','LY','PC','ZM']


def can_make_word(word):
    created_word=''
    block_current=blocks.copy()
    for w in word.upper():
        for block in block_current:
            if w in block:
                created_word += w
                block_current.remove(block)
                break

    if created_word == word.upper():
        print('TRUE')
    else:
        print('FALSE')



# Currently it's checking every time same letter multiple times in the blocks

def user_input():
    word = input("What is your word?: ")
    return word.upper()

