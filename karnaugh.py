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
def karnaughList(bits):
    l = [0, 1]
    length = 2 ** bits
    p = 2
    while(len(l) < length):
        newL = rev(l)
        for i in newL:
            l.append(i + p)
        p = p * 2
    return l

# Gets the bit, b, of a number, n
# 0 indexed
# big endian
# Parameter(s)
def getBit(n, b):
    mod = 2 ** b
    return (n % (2 * mod)) / mod 


def main():
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "test"):
            # rev tests
            l = [1, 1, 2, 3, 5, 8]
            rl = [8, 5, 3, 2, 1, 1]
            testing.equality(l, rev(rl))
            testing.inequality(rev(l), rev(rl))

            # karnaugh tests
            kl1 = [0, 1]
            kl2 = [0, 1, 3, 2]
            kl3 = [0, 1, 3, 2, 6, 7, 5, 4]
            kl4 = [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
            testing.equality(karnaughList(1), kl1)
            testing.equality(karnaughList(2), kl2)
            testing.equality(karnaughList(3), kl3)
            testing.equality(karnaughList(4), kl4)

            # getBit tests
            testing.equality(getBit(4, 3), 0)
            testing.equality(getBit(4, 2), 1)
            testing.equality(getBit(4, 1), 0)
            testing.equality(getBit(4, 0), 0)
            for i in range(16):
                n = (2 ** 16) - 1
                testing.equality(getBit(n, i), 1)

            testing.main()
    else:
        print karnaugh(3)

if __name__ == "__main__":
    main()
