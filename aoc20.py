import math

def day20b():
    presents = 0
    i = 9
    while (presents < 29000000):
        i += 1
        presents = 0
        for d in divisorGenerator(i):
            if i/d <= 50:
                presents += d * 11

    print (i)

def day20a():
    presents = 0
    i = 9
    while (presents < 29000000):
        i += 1
        presents = 0
        for d in divisorGenerator(i):
            presents += d * 10

    print (i)

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
