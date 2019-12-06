with open('input07a.txt', 'r') as inFile:
    allDiscs = set()
    topDiscs = set()
    for line in inFile:
        line = line.strip().replace(',','').split()
        allDiscs.add(line[0])
        if len(line) > 2:
            for i in range(3,len(line)):
                topDiscs.add(line[i])
    print(list(allDiscs - topDiscs)[0])
