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
# Parameter(s):
def getBit(n, b):
    mod = 2 ** b
    return (n % (2 * mod)) / mod 

# Just a function with 2 arguments
# Solely for testing purposes
# Parameters(2):
#     a is an integer
#     b is an integer
def twoArgumentFunction(a, b):
    return a + b

# Makes the Karnaugh map of twoArgumentFunction
# that has 2 inputs whose maximum size, in bits,
# is inputSize
# Will be extended to other functions later
# Will be extended to accept inputs of different
# sizes later
# Parameter(s):
#     inputSize is an integer
def karnaughMap(inputSize):
    karList = karnaughList(inputSize)
    karMap = []
    for i in karList:
        row = []
        for j in karList:
            val = twoArgumentFunction(i, j)
            row.append(val)
        karMap.append(row)
    return karMap

# Finds the largest value in the map
# Parameter(s):
#     array is a list of lists
def mapMax(array):
    m = array[0][0]
    for i in array:
        if(max(i) > m):
            m = max(i)
    return m

def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "test"):
            # rev tests
            l = [1, 1, 2, 3, 5, 8]
            rl = [8, 5, 3, 2, 1, 1]
            testing.equality(l, rev(rl))
            testing.inequality(rev(l), rev(rl))

            # karnaughList tests
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

            # twoArgumentFunction tests
            testing.equality(twoArgumentFunction(1, 2), 3)
            testing.equality(twoArgumentFunction(3, 5), 8)
            testing.equality(twoArgumentFunction(6, 6), 12)

            # karnaughMap tests
            km1 = [[0, 1], [1, 2]]
            km2 = [[0, 1, 3, 2], [1, 2, 4, 3], [3, 4, 6, 5], [2, 3, 5, 4]]
            testing.equality(karnaughMap(1), km1)
            testing.equality(karnaughMap(2), km2)

            # mapMax tests
            testing.equality(mapMax(karnaughMap(1)), 2)
            testing.equality(mapMax(karnaughMap(2)), 6)
            testing.equality(mapMax(karnaughMap(3)), 14)
            testing.equality(mapMax(karnaughMap(4)), 30)

            testing.main()
        else:
            for i in karnaughMap(int(sys.argv[1])):
                print i

if __name__ == "__main__":
    main()
