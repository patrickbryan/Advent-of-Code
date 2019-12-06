packages = []

def sameLetters(a, b):
    ans = ''
    for i,char in enumerate(a):
        if b[i] == char:
            ans = ans + char
    print (ans)

with open("input02.txt", "r") as file:
    for line in file:
        line = line.strip()
        for p in packages:
            notSame = 0
            for i,char in enumerate(p):
                if line[i] != char:
                    notSame += 1
                if notSame > 1:
                    break
            if notSame == 1:
                sameLetters(p, line)
                exit
        packages.append(line)
