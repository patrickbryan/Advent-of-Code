totalTwo = 0
totalThree = 0
total = 0

with open("input02.txt", "r") as file:
    for line in file:
        alphaDict = { }
        twoAmt = 0
        threeAmt = 0
        for char in line:
            if char in alphaDict:
                alphaDict[char] += 1
            else:
                alphaDict[char] = 1
            if alphaDict[char] == 2:
                twoAmt += 1
            elif alphaDict[char] == 3:
                twoAmt -= 1
                threeAmt += 1
            elif alphaDict[char] == 4:
                threeAmt -= 1
        if twoAmt > 0:
            totalTwo += 1
        if threeAmt > 0:
            totalThree += 1
    total = totalTwo * totalThree

print (total)
