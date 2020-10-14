
# 1. get collection of the blocks
# 2. be able to prinnt each row (item) from collection


blocks =['BO','(X K)','(D Q)','(C P)','(N A)','(G T)','(R E)','(T G)','(Q D)','(F S)','(J W)','(H U)','(V I)',
         '(A N)','(O B)','(E R)','(F S)','(L Y)','(P C)','(Z M)']



new_list=[]

def can_make_word(word):
    count=0
    index =0
    while index < len(word):
        w = word[index]
        for w in word:
            for block in blocks:
                if w in block and block not in new_list:
                    #create a counter of the word that I do not use same letter again
                    new_list.append(block)
                    count+=1
                    index+=1
                    print(f'letter {w},{block} is in the list ')

                else:
                    print(f"this {block} is taken")
        break


# Currently it's checking every time same letter multiple times in the blocks

def user_input():
    word = input("What is your word?: ")
    return word.upper()

