import sys

def probInput():
    return open(r"C:\Users\pbryan\Desktop\Release\in.txt").readlines()

def day2a():
    data = probInput()
    paper = 0

    for box in data:
        d = box.split('x')
        l = int(d[0])
        w = int(d[1])
        h = int(d[2])
        smallest = l * w
        smallest = l * h if l * h < smallest else smallest
        smallest = w * h if w * h < smallest else smallest
        paper += 2*((l * w) + (l * h) + (w * h)) + smallest

    print(paper)
            
def day2b():
    data = probInput()
    rib = 0

    for box in data:
        d = box.split('x')
        l = int(d[0])
        w = int(d[1])
        h = int(d[2])
        v = l * w * h
        large = l if l > w else w
        large = h if h > large else large
        side = 2*(l + w + h) - 2*(large)
        rib += (side) + (v)

    print (rib)
