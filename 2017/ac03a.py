import math

puzzle = 289326
top = int(math.sqrt(puzzle))
if top**2 != puzzle:
    top += 1
    if (top)**2 % 2 == 0:
        top += 1
bottom = top - 2
ring = int((top - 1)/2)
spot = 0
for i in range(1,5):
    if (bottom + (i/2))**2 >= puzzle:
        newBottom = int((bottom + ((i-1)/2))**2)
        newTop = int((bottom + (i/2))**2)
        if newBottom % 2 == 0:
            newBottom += 1
        if newTop % 2 == 0:
            newTop += 1
        for x in range(newBottom, newTop + 1):
            if x == puzzle:
                if x - newBottom > ring:
                    spot += 1
                break
            if x - newBottom < ring:
                spot -= 1
            elif x - newBottom > ring:
                spot += 1
        break
print((ring*2) + spot)
