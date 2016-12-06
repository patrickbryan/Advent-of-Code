import sys
import re

def probInput():
    return open(r"C:\Users\pbryan\Desktop\Release\in.txt").readlines()

def day5a():
    data = probInput()
    nice = 0
    doub = re.compile(r".*([a-z])\1.*")
    vowel = re.compile(r".*([aeiou]).*([aeiou]).*([aeiou]).*")
    bad = re.compile(r".*(ab|cd|pq|xy).*")

    for w in data:
        if (doub.match(w) and vowel.match(w) and bad.match(w) == None):
            nice += 1

    print (nice)
