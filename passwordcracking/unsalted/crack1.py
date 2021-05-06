import hashlib
import binascii
import sys
from math import floor
from time import time
from tqdm import tqdm

def compute_hash(word):
    encoded = word.encode('utf-8')
    md5 = hashlib.md5(encoded)
    word_hash = md5.digest()
    hash_hex = binascii.hexlify(word_hash)
    hash_hex_string = hash_hex.decode('utf-8')
    return hash_hex_string

if __name__ == "__main__":
    try: 
        ident = int(sys.argv[1])
        n = int(sys.argv[2])

        words = [line.strip().lower() for line in open('words.txt')]

        # basic idea:
        # for each word / pair of words, 
        # check if there's a hash that matches it 

        user_hash = dict()

        for line in open('passwords1.txt'):
            line = line.split(":")
            user_hash[line[1]] = line[0]

        hashes_computed = 0
        start = time()

        for i in tqdm(range(floor(ident * len(words) / n), floor((ident + 1) * len(words) / n))):
            word = words[i]
            word_hash = compute_hash(word)
            hashes_computed += 1

            if word_hash in user_hash:
                with open('cracked.txt', "a") as f:
                    f.write("{0}:{1}\n".format(user_hash[word_hash], word))
                    f.flush()

            for second_word in words:
                pair = word + second_word
                pair_hash = compute_hash(pair)
                hashes_computed += 1

                if pair_hash in user_hash:
                    with open('cracked.txt', "a") as f:
                        f.write("{0}:{1}\n".format(user_hash[pair_hash], pair))
                        f.flush()

    finally:
        end = time()
        with open('timings.txt'.format(ident), "w") as f:
            f.write(str(hashes_computed) + " " + str(end - start) + "\n")
            f.flush()
