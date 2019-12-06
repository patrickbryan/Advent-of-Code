def rec7b(disc, found = 0):
    curDiscLink = discLinks[disc]
    sums = []
    linkList = []
    for link in curDiscLink:
        discSum = allDiscs[link]
        if link in discLinks:
            tempSum, found = rec7b(link, found)
            discSum += tempSum
        sums.append(discSum)
        linkList.append(link)
    if not found and sums[1:] != sums[:-1]:
        if min(sums) == sums[0] and min(sums) == sums[-1]:
            discIndex = sums.index(min(sums))
            print(allDiscs[linkList[discIndex]] + max(sums) - min(sums))
        else:
            discIndex = sums.index(max(sums))
            print(allDiscs[linkList[discIndex]] - max(sums) + min(sums))
        found = 1
    return sum(sums), found
    

with open('input07a.txt', 'r') as inFile:
    bottom = 'vtzay'

    allDiscs = {}
    discLinks = {}
    for line in inFile:
        line = line.strip().replace(',','').split()
        allDiscs[line[0]] = int(line[1][1:-1])
        if len(line) > 2:
            discLinks[line[0]] = ()
            for i in range(3,len(line)):
                discLinks[line[0]] += (line[i],)
    rec7b(bottom)
