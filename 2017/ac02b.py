with open('input02a.txt', 'r') as inFile:
    total = 0
    for line in inFile:
        line = list(map(int, line.strip().split()))
        for i,num in enumerate(line):
            for x in range(i+1,len(line)):
                numTwo = line[x]
                if num % numTwo == 0 or numTwo % num == 0:
                    if num > numTwo:
                        total += int(num / numTwo)
                        break
                    else:
                        total += int(numTwo / num)
    print(total)
