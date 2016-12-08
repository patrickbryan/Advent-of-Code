import re
import collections

pInput = []
with open('aoc4Input.txt', 'r') as fp:
   for line in fp:
       pInput.append([field.strip(']\n') for field in re.split('[\-\[]', line)])

def partOne():
    idSum = 0
    for room in pInput:
        name = ''
        for n in room[:-2]:
            name += n
        freq = collections.Counter(name).most_common()
        checkFreq = ''
        sameFreq = ''
        freqNum = -1
        for char,num in freq:
            if num != freqNum:
                freqNum = num
                checkFreq += ''.join(sorted(sameFreq))
                sameFreq = ''
            sameFreq += char
        checkFreq += ''.join(sorted(sameFreq))
        
        if room[-1] == checkFreq[:5]:
            idSum += int(room[-2])
        
    return idSum

def partTwo():
    roomId = -1

    for room in pInput:
        roomWord = ''
        for word in room[:-2]:
            newWord = ''.join(chr(((ord(w) - 97 + int(room[-2])) % 26) + 97) for w in word)
            if 'northpole' == newWord:
                roomId = int(room[-2])
            roomWord += newWord + ' '
    
    return roomId

print("Part One Answer: " + str(partOne()))
print("Part Two Answer: " + str(partTwo()))
