import sys

def probInput():
    return open(r"C:\Users\pbryan\Desktop\Release\in.txt").readlines()

def day1a():
    data = probInput()
    up = 0
    down = 0
    for c in data:
        if (c == '('):
            up += 1
        elif (c == ')'):
            down += 1

    print(up - down)

def day1b():
    data = probInput()
    curF = 0
    pos = 0
    for c in data:
        if (c == '('):
            curF += 1
        elif (c == ')'):
            curF -= 1
        pos += 1
        if (curF < 0):
            break;

    print(pos)
