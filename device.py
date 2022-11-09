ucode = '817341' 
lcode = '817344'
locked = True
i = input("Input: ")
c = ''.join(x for x in i if x.isdigit())
o = 0
while o < len(c)-5:
    if c[o:o+6] == ucode:
        locked = False
        o += 6
    elif c[o:o+6] == lcode:
        locked = True
        o += 6
    else:
        o += 1
if locked:
    print("Locked")
else:
    print("Unlocked")