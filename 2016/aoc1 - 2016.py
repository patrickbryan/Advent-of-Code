dirInput = 'L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5'
inp = dirInput.split(', ')
#directs = ['N', 'E', 'S', 'W']

def partOne():
    directsIndex = 0
    x = 0
    y = 0

    for d in inp:
        if d[0] == 'L':
            directsIndex = (directsIndex - 1) % 4
        elif d[0] == 'R':
            directsIndex = (directsIndex + 1) % 4
        else:
            print("ERROR. Neither Left nor Right")
            break

        dist = int(d[1:])
        if directsIndex == 0:
            y += dist
        elif directsIndex == 2:
            y -= dist
        elif directsIndex == 1:
            x += dist
        elif directsIndex == 3:
            x -= dist
        else:
            print("ERROR. Compass broken!")
            break

    return abs(x) + abs(y)

def partTwo():
    directsIndex = 0
    x = 0
    y = 0
    locs = [[0,0]]
    final = -1
    found = False
    
    for d in inp:
        if d[0] == 'L':
            directsIndex = (directsIndex - 1) % 4
        elif d[0] == 'R':
            directsIndex = (directsIndex + 1) % 4
        else:
            print("ERROR. Neither Left nor Right")
            break

        #Horrible way to do this for part 2 (but it DOES work)
        dist = int(d[1:])
        if directsIndex == 0:
            for i in range(dist):
                y += 1
                if [x, y] in locs:
                    final = abs(x) + abs(y)
                    found = True
                    break
                locs.append([x, y])
        elif directsIndex == 2:
            for i in range(dist):
                y -= 1
                if [x, y] in locs:
                    final = abs(x) + abs(y)
                    found = True
                    break
                locs.append([x, y])
        elif directsIndex == 1:
            for i in range(dist):
                x += 1
                if [x, y] in locs:
                    final = abs(x) + abs(y)
                    found = True
                    break
                locs.append([x, y])
        elif directsIndex == 3:
            for i in range(dist):
                x -= 1
                if [x, y] in locs:
                    final = abs(x) + abs(y)
                    found = True
                    break
                locs.append([x, y])
        else:
            print("ERROR. Compass broken!")
            break

        if found:
            break

    return final


print("Part One Answer: " + str(partOne()))
print("Part Two Answer: " + str(partTwo()))
