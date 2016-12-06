import sys

def probInput():
    return open(r"C:\Users\pbryan\Desktop\Release\in.txt").readlines()

def day3b():
    data = probInput()
    data = data[0]
    houses = 1
    posSanta = (0,0)
    posRobot = (0,0)
    visited = [posSanta]
    turnSanta = True

    def newPos(pos, c):
        if c == '^':
           pos = (pos[0], pos[1] + 1)
        elif c == 'v':
            pos = (pos[0], pos[1] - 1)
        elif c == '>':
            pos = (pos[0] + 1, pos[1])
        elif c == '<':
            pos = (pos[0] - 1, pos[1])
        return pos

    for c in data:
        if turnSanta:
            posSanta = newPos(posSanta, c)
            if posSanta not in visited:
                visited.append(posSanta)
                houses += 1
        else:
            posRobot = newPos(posRobot, c)
            if posRobot not in visited:
                visited.append(posRobot)
                houses += 1
        turnSanta = turnSanta == False

    print (houses)

def day3a():
    data = probInput()
    data = data[0]
    houses = 1
    pos = (0,0)
    visited = [pos]

    for c in data:
        if c == '^':
            pos = (pos[0], pos[1] + 1)
        elif c == 'v':
            pos = (pos[0], pos[1] - 1)
        elif c == '>':
            pos = (pos[0] + 1, pos[1])
        elif c == '<':
            pos = (pos[0] - 1, pos[1])

        if pos not in visited:
            visited.append(pos)
            houses += 1

    print (houses)
