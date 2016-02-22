import sys
import itertools

weapons = [[8, 4], [10, 5], [25, 6], [40, 7], [74, 8]]
armor = [[0, 0], [13, 1], [31, 2], [53, 3], [75, 4], [102, 5]]
rings = [[0, 0, 0], [0, 0, 0], [25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]

def day21b():
    maxCost = 0
    
    for w in weapons:
        for a in armor:
            for r in itertools.combinations(rings, 2):
                if (not canWin(100, w[1] + r[0][1] + r[1][1], a[1] + r[0][2] + r[1][2])):
                    cost = calcCost(w, a, r)
                    maxCost = cost if cost > maxCost else maxCost

    print (maxCost)

def day21a():
    minCost = 10000
    
    for w in weapons:
        for a in armor:
            for r in itertools.combinations(rings, 2):
                if (canWin(100, w[1] + r[0][1] + r[1][1], a[1] + r[0][2] + r[1][2])):
                    cost = calcCost(w, a, r)
                    minCost = cost if cost < minCost else minCost

    print (minCost)

def canWin(heroHp, heroDmg, heroAmr):
    bossHp = 100
    bossDmg = 8
    bossAmr = 2

    while (bossHp >= 0 and heroHp >= 0):
        bossHp -= 1 if heroDmg - bossAmr < 1 else heroDmg - bossAmr
        heroHp -= 1 if bossDmg - heroAmr < 1 else bossDmg - heroAmr

    return True if bossHp <= 0 else False

def calcCost(w, a, r):
    return w[0] + a[0] + r[0][0] + r[1][0]
