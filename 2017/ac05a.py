with open('input05a.txt', 'r') as inFile:
    inst = []
    loc = 0
    for line in inFile:
        inst.append(int(line.strip()))
    instLen = len(inst)
    steps = 0
    
    while loc < instLen:
        inst[loc] += 1
        loc += inst[loc] - 1
        steps += 1

print(steps)
