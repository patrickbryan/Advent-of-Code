pInput = 3001330

def partOne():
    return 2*(pInput - 2**(pInput.bit_length() - 1)) + 1

def partTwo():
    return 'err'

print("Part One Answer: " + str(partOne()))
print("Part Two Answer: " + str(partTwo()))
