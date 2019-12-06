with open('input01a.txt', 'r') as inFile:
    for line in inFile:
        line = line.strip()
        total = 0
        lineLen = len(line)
        check = int(lineLen / 2)
        for i,num in enumerate(line):
            if line[(i + check) % lineLen] == num:
                total += int(num)
        print(total)
