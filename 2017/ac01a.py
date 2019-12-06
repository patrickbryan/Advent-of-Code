with open('input01a.txt', 'r') as inFile:
    for line in inFile:
        line = line.strip()
        total = 0
        prevNum = line[-1]
        for num in line:
            if prevNum == num:
                total += int(num)
            prevNum = num
        print(total)
