puzzle = 289326
spiral = {(0,0):1}
directions = [(0,1),(-1,0),(0,-1),(1,0)]
adjacentDirs = [(0,1),(-1,0),(0,-1),(1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
curDir = 0
curCoord = (1,0)
lastNum = 1

while lastNum < puzzle:
    nextDir = (curDir + 1) % 4
    if (directions[nextDir][0] + curCoord[0], directions[nextDir][1] + curCoord[1]) not in spiral:
        curDir = nextDir

    total = 0
    for dirs in adjacentDirs:
        if (curCoord[0] + dirs[0], curCoord[1] + dirs[1]) in spiral:
            total += spiral[(curCoord[0] + dirs[0], curCoord[1] + dirs[1])]
    spiral[curCoord] = total
    lastNum = total
    
    curCoord = (directions[curDir][0] + curCoord[0], directions[curDir][1] + curCoord[1])

print(lastNum)
