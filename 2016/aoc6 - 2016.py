import collections

pInput = []
with open('aoc6Input.txt', 'r') as fp:
   for line in fp:
       pInput.append(line.strip())

def partOne():
    rotated = zip(*pInput[::-1])
    word = ''
    for w in rotated:
        word += collections.Counter(w).most_common(1)[0][0]
    
    return word

def partTwo():
    rotated = zip(*pInput[::-1])
    word = ''
    for w in rotated:
        word += collections.Counter(w).most_common()[-1][0]
    
    return word

print("Part One Answer: " + str(partOne()))
print("Part Two Answer: " + str(partTwo()))
