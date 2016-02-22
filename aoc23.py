def probInput():
    return open(r"C:\Users\pbryan\Desktop\Release\in.txt").readlines()

def day23a():
    data = probInput()
    a = 1
    b = 0
    i = 0

    while i < len(data):
        if data[i][:3] == 'hlf':
            if data[i][4] == 'a':
                a = int(a / 2)
            elif data[i][4] == 'b':
                b = int(b / 2)
        elif data[i][:3] == 'tpl':
            if data[i][4] == 'a':
                a *= 3
            elif data[i][4] == 'b':
                b *= 3
        elif data[i][:3] == 'inc':
            if data[i][4] == 'a':
                a += 1
            elif data[i][4] == 'b':
                b += 1
        elif data[i][:3] == 'jmp':
            i += int(data[i][4:]) - 1
        elif data[i][:3] == 'jie':
            jump = False
            if data[i][4] == 'a' and a % 2 == 0:
                jump = True
            elif data[i][4] == 'b' and b % 2 == 0:
                jump = True
            if jump:
                i += int(data[i][7:]) - 1
        elif data[i][:3] == 'jio':
            jump = False
            if data[i][4] == 'a' and a == 1:
                jump = True
            elif data[i][4] == 'b' and b == 1:
                jump = True
            if jump:
                i += int(data[i][7:]) - 1
        i += 1

    print (b)
