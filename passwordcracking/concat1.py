import glob
import os

user_pass_set = set()

for fname in glob.glob('cracked1*.txt'):
    with open(fname) as f:
        for line in f:
            user_pass_set.add(line)
    os.remove(fname)

with open("passwords1.txt", "w") as f:
    for user_pass in user_pass_set:
        f.write(user_pass)

sum_cracked = len(user_pass_set)
sum_hash = 0
sum_time = 0

for fname in glob.glob('timings1*.txt'):
    with open(fname) as f:
        for line in f:
            split = line.split(" ")
            sum_hash += int(split[0])
            sum_time += float(split[1])
    os.remove(fname)

with open("times1.txt", "w") as f:
    f.write("time = " + str(sum_time) + "\n")
    f.write("hashes = " + str(sum_hash) + "\n") 
    f.write("cracked = " + str(sum_cracked) + "\n")
