with open('input08a.txt', 'r') as inFile:
    allRegs = {}
    totalMax = 0
    for line in inFile:
        reg, incDec, val, __, regCheck, oper, valCheck = line.strip().split()
        if reg not in allRegs:
            allRegs[reg] = 0
        if regCheck not in allRegs:
            allRegs[regCheck] = 0
        val = int(val)

        if eval('allRegs[regCheck]' + oper + valCheck):
            if incDec == 'dec':
                val *= -1
            allRegs[reg] += val
        tempMax = allRegs[max(allRegs, key=allRegs.get)]
        if tempMax > totalMax:
            totalMax = tempMax

    print(totalMax)
            
