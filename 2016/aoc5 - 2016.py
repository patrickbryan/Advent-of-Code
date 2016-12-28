import hashlib

pInput = "wtnhxymk"

def partOne():
    password = ""
    i = 0

    while (len(password) < 8):
        m = hashlib.md5()
        inp = (pInput + str(i)).encode('utf-8')
        m.update(inp)
        if (int(m.hexdigest()[0:5], 16) == 0):
            password += m.hexdigest()[5]
        i += 1

    return password

def partTwo():
    password = list("--------")
    passLen = 0
    i = 0

    while (passLen < 8):
        m = hashlib.md5()
        inp = (pInput + str(i)).encode('utf-8')
        m.update(inp)
        pos = int(m.hexdigest()[5], 16)
        if (int(m.hexdigest()[0:5], 16) == 0) and pos < 8 and password[pos] == '-':
            password[pos] = m.hexdigest()[6]
            passLen += 1
        i += 1

    return ''.join(password)

print("Part One Answer: " + str(partOne()))
print("Part Two Answer: " + str(partTwo()))
