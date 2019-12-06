import numpy as np

fabric = [[0] * 1000] * 1000

with open("input03.txt", "r") as file:
    for line in file:
        line = line.strip().replace(',',' ').replace(':','').replace('x',' ').split(' ')
        x = int(line[2])
        y = int(line[3])
        c = int(line[4])
        r = int(line[5])
        for i in range(r):
            fabric[i+y] = fabric[i+y][0:x] + [z+1 for z in fabric[i+y][x:x+c]] + (fabric[i+y][x+c:])
    npFabric = np.matrix(fabric)
    npFabric = npFabric[np.where(np.matrix(npFabric) > 1)]
    print(len(npFabric.flatten().tolist()[0]))

