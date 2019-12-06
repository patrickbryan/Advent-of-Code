with open('input04a.txt', 'r') as inFile:
    totalValid = 0
    for line in inFile:
        line = line.strip().split()
        for i,item in enumerate(line):
            line[i] = ''.join(sorted(item))
        if len(line) == len(set(line)):
            totalValid += 1

print(totalValid)
