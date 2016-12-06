import re

def probInput():
    return open(r"C:\Users\pbryan\Desktop\Release\in.txt").readlines()

def day12a():
    data = probInput()
    negNumReg = re.compile('-[0-9]+')
    posNumReg = re.compile('[0-9]+')
    negNums = negNumReg.findall(data[0])
    posNums = posNumReg.findall(data[0])
    negNums = list(map(int, negNums))
    posNums = list(map(int, posNums))
    total = 0
    total += sum(posNums)
    total += sum(negNums)
    total += sum(negNums)
    print (posNums)
    print ('')
    print (negNums)

    print (total)
