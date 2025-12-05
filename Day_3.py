## Joltage == number formed by the digits on the batteries you've turned on
## Largest possible joltage each bank can produce

file = 'day3.txt'

blocks = [[int(x) for x in line.strip()] for line in open(file).readlines()]

def find_joltage_n(l: list[int], n:int):
    """Find the maximum n-length joltage from the list of battery values"""
    L = len(l)
    jolt_s = ''
    start = 0
    for i in range(n):
        v = -1
        end = L - n + 1 + i
        for j in range(start, end):
            c = l[j]
            if c > v:
                v = c
                start = j + 1
        jolt_s += str(v)
    return int(jolt_s)

part2 = True
sum = 0
for block in blocks:
    sum += find_joltage_n(block, 12 if part2 else 2)
print(sum)