from itertools import permutations
from random import shuffle

#main string to permute
string = "kulturuke"

#get all permutations
perms = permutations(string)

#join them into a list of permutations
permList = [''.join(p) for p in perms]

#shuffle them to create a better reading experience
#we want the first element in the original position
copy = permList[1:]
shuffle(copy)
permList[1:] = copy

#write them to a file
f = open("dikt.txt", "w")
for p in permList:
    f.write(p.capitalize() + '\n')
f.close()

