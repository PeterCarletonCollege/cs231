with open('saltyHashesF.txt', "a") as f:
    for line in open('saltyHashes.txt'):
        line= line.strip()
        line = line.split(":")
        f.write("{0}:{1}\n".format(line[1],line[0]))
        f.flush()
