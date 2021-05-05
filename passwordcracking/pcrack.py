import hashlib
import itertools 


words1 = [line.strip().lower() for line in open('words.txt')]


print(list(itertools.permutations(words1, 2)))