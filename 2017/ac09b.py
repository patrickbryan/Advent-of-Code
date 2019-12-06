import re

with open('input09a.txt', 'r') as inFile:
    for line in inFile:
        line = line.strip()
        line = re.sub('!.','',line)

        curGroup = 0
        total = 0

        for c in line:
            if c == '<' and curGroup == 0:
                curGroup = 1
            elif c == '>':
                curGroup = 0
            else:
                total += curGroup

        print(total)
        

            
