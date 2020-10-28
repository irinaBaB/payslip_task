
# 1. get collection of the blocks
# 2. be able to prinnt each row (item) from collection


def can_make_word(word):
    created_word=''
    temp = []
    blocks =['BO','XK','DQ','CP','NA','GT','RE','TG','QD','FS','JW','HU','VI','AN','OB','ER','FS','LY','PC','ZM']
    # block_current=blocks.copy()
    for w in word.upper():
        for block in blocks:
            if w in block:
                created_word += w
                temp.append(block)
                blocks.remove(block)
                break

    if created_word == word.upper():
        print('TRUE')
    else:
        for block in temp:
            blocks.append(block)
        print('FALSE')
    print(blocks)




# Currently it's checking every time same letter multiple times in the blocks

def user_input():
    word = input("can_make_word ")
    return word.upper()

