
# 1. get collection of the blocks
# 2. be able to prinnt each row (item) from collection


blocks =['(B O)','(X K)','(D Q)','(C P)','(N A)','(G T)','(R E)','(T G)','(Q D)','(F S)','(J W)','(H U)','(V I)',
         '(A N)','(O B)','(E R)','(F S)','(L Y)','(P C)','(Z M)']

for item in blocks:
    print(item)

# list of blocks to begin
# Create new empty list to set used value there
# create a loop - when user enter the Letter
#  -Capitilise it (any letter user entered)
#  -Check if that letter is already used in the used_list (give an error message and end) print 'False'
#  -Check if any letter is available in any blocks that available and print 'True'
# will think about some tests (not the focus  right now)