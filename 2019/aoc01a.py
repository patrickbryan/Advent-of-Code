with open("input01.in", "r") as file:
    total = 0
    remainders = 0
    count = 0
    for line in file:
        num = int(line)
        total += num
        remainders += num % 3
        count += 1
    total = ((total - remainders) // 3) - (2 * count)
    print (total)
