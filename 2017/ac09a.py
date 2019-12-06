import re

with open('input09a.txt', 'r') as inFile:
    for line in inFile:
        line = line.strip()
        line = re.sub('!.','',line)
        line = re.sub('\<.*?\>','',line)

        curGroup = 1
        total = 0

        for c in line:
            if c == '{':
                total += curGroup
                curGroup += 1
            elif c == '}':
                curGroup -= 1
        print(total)
        

            
