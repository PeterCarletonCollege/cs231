import hashlib
import itertools 
wordsRaw = [line.strip().lower() for line in open('words.txt')]
outList = []
for i in wordsRaw:
    for j in wordsRaw:
        outList.append(i+j)


print(outList)