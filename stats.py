import random
from statistics import mean
ucode = '817341' 
lcode = '817344'
def stat():
    locked = True
    c = ''
    o = 0
    while True:
        c += str(random.randint(0,9))
        while o < len(c)-5:
            if c[o:o+6] == ucode:
                locked = False
                break
            elif c[o:o+6] == lcode:
                locked = True
                o += 6
            else:
                o += 1
        if not locked:
            break
    # print(len(c))
    # print("Unlocked")
    return len(c)
v = []

while True:
    try:
        n = int(input('Numer of test iterations (1-100): '))
        if n < 1 or n > 100:
            raise ValueError
        break
    except ValueError:
        print('Please enter an integer between 1 and 100.')

for i in range(int(n)):
    v.append(stat())
print('Test results:')
print("Max: " + str(max(v)))
print("Min: " + str(min(v)))
print("Mean: " + str(mean(v)))
