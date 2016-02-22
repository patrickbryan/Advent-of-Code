import sys

def probInput():
    return open(r"C:\Users\pbryan\Desktop\Release\in.txt").readlines()

def day7a():
    data = probInput()
    wires = {}

    while data:
        for cmd in data:
            iList = (cmd[:-1] if cmd.endswith('\n') else cmd).split(' ')

            if len(iList) == 3: #assign
                if iList[0].isdigit():
                    wires[iList[2]] = int(iList[0])
                    data.remove(cmd)
                elif iList[0] in wires:
                    wires[iList[2]] = wires[iList[0]]
                    data.remove(cmd)
            elif len(iList) == 4 and iList[1] in wires: #not
                wires[iList[3]] = wires[iList[1]] ^ 65535
                data.remove(cmd)
            elif len(iList) == 5 and iList[1] == 'AND' and iList[2] in wires:
                if iList[0].isdigit():
                    wires[iList[4]] = int(iList[0]) & wires[iList[2]]
                    data.remove(cmd)
                elif iList[0] in wires:
                    wires[iList[4]] = wires[iList[0]] & wires[iList[2]]
                    data.remove(cmd)
            elif len(iList) == 5 and iList[1] == 'OR' and iList[0] in wires and iList[2] in wires:
                wires[iList[4]] = wires[iList[0]] | wires[iList[2]]
                data.remove(cmd)
            elif len(iList) == 5 and iList[1] == 'LSHIFT' and iList[0] in wires:
                wires[iList[4]] = wires[iList[0]] << int(iList[2])
                data.remove(cmd)
            elif len(iList) == 5 and iList[1] == 'RSHIFT' and iList[0] in wires:
                wires[iList[4]] = wires[iList[0]] >> int(iList[2])
                data.remove(cmd)

    print(wires['a'])





