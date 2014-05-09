# karnaugh.py
# 2014-05-09+14:44:00

import sys
import testing

# Reverse a list, l
# Parameter(s): 
#     l is a list 
def rev(l):
    return l[::-1]

# Generates a karnaugh list where bits is the
# minimum number of bits required to represent
# the largest number
# Parameter(s):
#     bits is an integer
def karnaugh(bits):
    l = [0, 1]
    length = 2 ** bits
    p = 2
    while(len(l) < length):
        newL = rev(l)
        for i in newL:
            l.append(i + p)
        p = p * 2
    return l

def main():
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "test"):
            # rev tests
            l = [1, 1, 2, 3, 5, 8]
            rl = [8, 5, 3, 2, 1, 1]
            testing.equality(l, rev(rl))
            testing.inequality(rev(l), rev(rl))
            testing.main()
    else:
        print karnaugh(3)

if __name__ == "__main__":
    main()
