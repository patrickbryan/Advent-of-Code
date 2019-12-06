with open('input02a.txt', 'r') as inFile:
    total = 0
    for line in inFile:
        line = list(map(int, line.strip().split()))
        total += abs(max(line) - min(line))
    print(total)
