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

# Takes the values in an array and returns a new
# array with the bit, b, of that value as the
# element of the new array.
# 0 indexed
# Big endian
# Parameter(s):
#     array is a list of lists
#     b is an integer
def bitArray(array, b):
    newArray = []
    for i in array:
        newRow = []
        for j in i:
            newRow.append(getBit(j, b))
        newArray.append(newRow)
    return newArray

# Returns the indeces of any 1's in the list.
# Parameter(s):
#     l is a list
def locOfOnes(l):
    loc = []
    for i in range(len(l)):
        if(l[i] == 1):
            loc.append(i)
    return loc

# TODO write this function
# Expect to fail 57 tests
# Returns the start and end of each group of 1's
# in a row
# Parameter(s):
#     l is a list
def rowLength(l):
    return []

# Finds the largest power of 2 less than 
# or equal to value
# Parameter(s):
#     value is a number
def largestPowerOfTwo(value):
    p = 1
    while(p <= value):
        p = p * 2
    return p / 2

def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "test"):
            # rev tests (1 - 2)
            l = [1, 1, 2, 3, 5, 8]
            rl = [8, 5, 3, 2, 1, 1]
            testing.equality("Test 0", l, rev(rl))
            testing.inequality("Test 1", rev(l), rev(rl))

            # karnaughList tests (3 - 6)
            kl1 = [0, 1]
            kl2 = [0, 1, 3, 2]
            kl3 = [0, 1, 3, 2, 6, 7, 5, 4]
            kl4 = [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
            testing.equality("Test 2", karnaughList(1), kl1)
            testing.equality("Test 3", karnaughList(2), kl2)
            testing.equality("Test 4", karnaughList(3), kl3)
            testing.equality("Test 5", karnaughList(4), kl4)

            # getBit tests (7 - 26)
            testing.equality("Test 6", getBit(4, 3), 0)
            testing.equality("Test 7", getBit(4, 2), 1)
            testing.equality("Test 8", getBit(4, 1), 0)
            testing.equality("Test 9", getBit(4, 0), 0)
            for i in range(16):
                n = (2 ** 16) - 1
                testing.equality("Test " + str(i + 1), getBit(n, i), 1)

            # twoArgumentFunction tests (27 - 29)
            testing.equality("Test 27", twoArgumentFunction(1, 2), 3)
            testing.equality("Test 28", twoArgumentFunction(3, 5), 8)
            testing.equality("Test 29", twoArgumentFunction(6, 6), 12)

            # karnaughMap tests (30 - 31)
            km1 = [[0, 1], [1, 2]]
            km2 = [[0, 1, 3, 2], [1, 2, 4, 3], [3, 4, 6, 5], [2, 3, 5, 4]]
            testing.equality("Test 30", karnaughMap(1), km1)
            testing.equality("Test 31", karnaughMap(2), km2)

            # mapMax tests (32 - 35)
            testing.equality("Test 32", mapMax(karnaughMap(1)), 2)
            testing.equality("Test 33", mapMax(karnaughMap(2)), 6)
            testing.equality("Test 34", mapMax(karnaughMap(3)), 14)
            testing.equality("Test 35", mapMax(karnaughMap(4)), 30)

            # bitArray tests (36 - 41)
            ba10 = [[0, 1], [1, 0]]
            ba11 = [[0, 0], [0, 1]]
            ba20 = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
            ba21 = [[0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
            ba22 = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]]
            ba23 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            km1 = karnaughMap(1)
            km2 = karnaughMap(2)
            testing.equality("Test 36", bitArray(km1, 0), ba10)
            testing.equality("Test 37", bitArray(km1, 1), ba11)
            testing.equality("Test 38", bitArray(km2, 0), ba20)
            testing.equality("Test 39", bitArray(km2, 1), ba21)
            testing.equality("Test 40", bitArray(km2, 2), ba22)
            testing.equality("Test 41", bitArray(km2, 3), ba23)

            # rowLength tests (42 - 103)
            tl0 = [0]
            tl1 = [1]
            tl2 = [0, 0]
            tl3 = [0, 1]
            tl4 = [1, 0]
            tl5 = [1, 1]
            tl6 = [0, 0, 0]
            tl7 = [0, 0, 1]
            tl8 = [0, 1, 0]
            tl9 = [0, 1, 1]
            tl10 = [1, 0, 0]
            tl11 = [1, 0, 1]
            tl12 = [1, 1, 0]
            tl13 = [1, 1, 1]
            tl14 = [0, 0, 0, 0]
            tl15 = [0, 0, 0, 1]
            tl16 = [0, 0, 1, 0]
            tl17 = [0, 0, 1, 1]
            tl18 = [0, 1, 0, 0]
            tl19 = [0, 1, 0, 1]
            tl20 = [0, 1, 1, 0]
            tl21 = [0, 1, 1, 1]
            tl22 = [1, 0, 0, 0]
            tl23 = [1, 0, 0, 1]
            tl24 = [1, 0, 1, 0]
            tl25 = [1, 0, 1, 1]
            tl26 = [1, 1, 0, 0]
            tl27 = [1, 1, 0, 1]
            tl28 = [1, 1, 1, 0]
            tl29 = [1, 1, 1, 1]
            tl30 = [0, 0, 0, 0, 0]
            tl31 = [0, 0, 0, 0, 1]
            tl32 = [0, 0, 0, 1, 0]
            tl33 = [0, 0, 0, 1, 1]
            tl34 = [0, 0, 1, 0, 0]
            tl35 = [0, 0, 1, 0, 1]
            tl36 = [0, 0, 1, 1, 0]
            tl37 = [0, 0, 1, 1, 1]
            tl38 = [0, 1, 0, 0, 0]
            tl39 = [0, 1, 0, 0, 1]
            tl40 = [0, 1, 0, 1, 0]
            tl41 = [0, 1, 0, 1, 1]
            tl42 = [0, 1, 1, 0, 0]
            tl43 = [0, 1, 1, 0, 1]
            tl44 = [0, 1, 1, 1, 0]
            tl45 = [0, 1, 1, 1, 1]
            tl46 = [1, 0, 0, 0, 0]
            tl47 = [1, 0, 0, 0, 1]
            tl48 = [1, 0, 0, 1, 0]
            tl49 = [1, 0, 0, 1, 1]
            tl50 = [1, 0, 1, 0, 0]
            tl51 = [1, 0, 1, 0, 1]
            tl52 = [1, 0, 1, 1, 0]
            tl53 = [1, 0, 1, 1, 1]
            tl54 = [1, 1, 0, 0, 0]
            tl55 = [1, 1, 0, 0, 1]
            tl56 = [1, 1, 0, 1, 0]
            tl57 = [1, 1, 0, 1, 1]
            tl58 = [1, 1, 1, 0, 0]
            tl59 = [1, 1, 1, 0, 1]
            tl60 = [1, 1, 1, 1, 0]
            tl61 = [1, 1, 1, 1, 1]
            rl0 = []
            rl1 = [[0, 0]]
            rl2 = []
            rl3 = [[1, 1]]
            rl4 = [[0, 0]]
            rl5 = [[0, 1]]
            rl6 = []
            rl7 = [[2, 2]]
            rl8 = [[1, 1]]
            rl9 = [[1, 2]]
            rl10 = [[0, 0]]
            rl11 = [[0, 0], [2, 2]]
            rl12 = [[0, 1]]
            rl13 = [[0, 2]]
            rl14 = []
            rl15 = [[3, 3]]
            rl16 = [[2, 2]]
            rl17 = [[2, 3]]
            rl18 = [[1, 1]]
            rl19 = [[1, 1], [3, 3]]
            rl20 = [[1, 2]]
            rl21 = [[1, 3]]
            rl22 = [[0, 0]]
            rl23 = [[0, 0], [3, 3]]
            rl24 = [[0, 0], [2, 2]]
            rl25 = [[0, 0], [2, 3]]
            rl26 = [[0, 1]]
            rl27 = [[0, 1], [3, 3]]
            rl28 = [[0, 2]]
            rl29 = [[0, 3]]
            rl30 = []
            rl31 = [[4, 4]]
            rl32 = [[3, 3]]
            rl33 = [[3, 4]]
            rl34 = [[2, 2]]
            rl35 = [[2, 2], [4, 4]]
            rl36 = [[2, 3]]
            rl37 = [[2, 4]]
            rl38 = [[1, 1]]
            rl39 = [[1, 1], [4, 4]]
            rl40 = [[1, 1], [3, 3]]
            rl41 = [[1, 1], [3, 4]]
            rl42 = [[1, 2]]
            rl43 = [[1, 2], [4, 4]]
            rl44 = [[1, 3]]
            rl45 = [[1, 4]]
            rl46 = [[0, 0]]
            rl47 = [[0, 0], [4, 4]]
            rl48 = [[0, 0], [3, 3]]
            rl49 = [[0, 0], [3, 4]]
            rl50 = [[0, 0], [2, 2]]
            rl51 = [[0, 0], [2, 2], [4, 4]]
            rl52 = [[0, 0], [2, 3]]
            rl53 = [[0, 0], [2, 4]]
            rl54 = [[0, 1]]
            rl55 = [[0, 1], [4, 4]]
            rl56 = [[0, 1], [3, 3]]
            rl57 = [[0, 1], [3, 4]]
            rl58 = [[0, 2]]
            rl59 = [[0, 2], [4, 4]]
            rl60 = [[0, 3]]
            rl61 = [[0, 4]]
            testing.equality("Test 42", rl0, rowLength(tl0))
            testing.equality("Test 43", rl1, rowLength(tl1))
            testing.equality("Test 44", rl2, rowLength(tl2))
            testing.equality("Test 45", rl3, rowLength(tl3))
            testing.equality("Test 46", rl4, rowLength(tl4))
            testing.equality("Test 47", rl5, rowLength(tl5))
            testing.equality("Test 48", rl6, rowLength(tl6))
            testing.equality("Test 49", rl7, rowLength(tl7))
            testing.equality("Test 50", rl8, rowLength(tl8))
            testing.equality("Test 51", rl9, rowLength(tl9))
            testing.equality("Test 52", rl10, rowLength(tl10))
            testing.equality("Test 53", rl11, rowLength(tl11))
            testing.equality("Test 54", rl12, rowLength(tl12))
            testing.equality("Test 55", rl13, rowLength(tl13))
            testing.equality("Test 56", rl14, rowLength(tl14))
            testing.equality("Test 57", rl15, rowLength(tl15))
            testing.equality("Test 58", rl16, rowLength(tl16))
            testing.equality("Test 59", rl17, rowLength(tl17))
            testing.equality("Test 60", rl18, rowLength(tl18))
            testing.equality("Test 61", rl19, rowLength(tl19))
            testing.equality("Test 62", rl20, rowLength(tl20))
            testing.equality("Test 63", rl21, rowLength(tl21))
            testing.equality("Test 64", rl22, rowLength(tl22))
            testing.equality("Test 65", rl23, rowLength(tl23))
            testing.equality("Test 66", rl24, rowLength(tl24))
            testing.equality("Test 67", rl25, rowLength(tl25))
            testing.equality("Test 68", rl26, rowLength(tl26))
            testing.equality("Test 69", rl27, rowLength(tl27))
            testing.equality("Test 70", rl28, rowLength(tl28))
            testing.equality("Test 71", rl29, rowLength(tl29))
            testing.equality("Test 72", rl30, rowLength(tl30))
            testing.equality("Test 73", rl31, rowLength(tl31))
            testing.equality("Test 74", rl32, rowLength(tl32))
            testing.equality("Test 75", rl33, rowLength(tl33))
            testing.equality("Test 76", rl34, rowLength(tl34))
            testing.equality("Test 77", rl35, rowLength(tl35))
            testing.equality("Test 78", rl36, rowLength(tl36))
            testing.equality("Test 79", rl37, rowLength(tl37))
            testing.equality("Test 80", rl38, rowLength(tl38))
            testing.equality("Test 81", rl39, rowLength(tl39))
            testing.equality("Test 82", rl40, rowLength(tl40))
            testing.equality("Test 83", rl41, rowLength(tl41))
            testing.equality("Test 84", rl42, rowLength(tl42))
            testing.equality("Test 85", rl43, rowLength(tl43))
            testing.equality("Test 86", rl44, rowLength(tl44))
            testing.equality("Test 87", rl45, rowLength(tl45))
            testing.equality("Test 88", rl46, rowLength(tl46))
            testing.equality("Test 89", rl47, rowLength(tl47))
            testing.equality("Test 90", rl48, rowLength(tl48))
            testing.equality("Test 91", rl49, rowLength(tl49))
            testing.equality("Test 92", rl50, rowLength(tl50))
            testing.equality("Test 93", rl51, rowLength(tl51))
            testing.equality("Test 94", rl52, rowLength(tl52))
            testing.equality("Test 95", rl53, rowLength(tl53))
            testing.equality("Test 96", rl54, rowLength(tl54))
            testing.equality("Test 97", rl55, rowLength(tl55))
            testing.equality("Test 98", rl56, rowLength(tl56))
            testing.equality("Test 99", rl57, rowLength(tl57))
            testing.equality("Test 100", rl58, rowLength(tl58))
            testing.equality("Test 101", rl59, rowLength(tl59))
            testing.equality("Test 102", rl60, rowLength(tl60))
            testing.equality("Test 103", rl61, rowLength(tl61))

            # locOfOnes tests (104 - 165)
            rl0 = []
            rl1 = [0]
            rl2 = []
            rl3 = [1]
            rl4 = [0]
            rl5 = [0, 1]
            rl6 = []
            rl7 = [2]
            rl8 = [1]
            rl9 = [1, 2]
            rl10 = [0]
            rl11 = [0, 2]
            rl12 = [0, 1]
            rl13 = [0, 1, 2]
            rl14 = []
            rl15 = [3]
            rl16 = [2]
            rl17 = [2, 3]
            rl18 = [1]
            rl19 = [1, 3]
            rl20 = [1, 2]
            rl21 = [1, 2, 3]
            rl22 = [0]
            rl23 = [0, 3]
            rl24 = [0, 2]
            rl25 = [0, 2, 3]
            rl26 = [0, 1]
            rl27 = [0, 1, 3]
            rl28 = [0, 1, 2]
            rl29 = [0, 1, 2, 3]
            rl30 = []
            rl31 = [4]
            rl32 = [3]
            rl33 = [3, 4]
            rl34 = [2]
            rl35 = [2, 4]
            rl36 = [2, 3]
            rl37 = [2, 3, 4]
            rl38 = [1]
            rl39 = [1, 4]
            rl40 = [1, 3]
            rl41 = [1, 3, 4]
            rl42 = [1, 2]
            rl43 = [1, 2, 4]
            rl44 = [1, 2, 3]
            rl45 = [1, 2, 3, 4]
            rl46 = [0]
            rl47 = [0, 4]
            rl48 = [0, 3]
            rl49 = [0, 3, 4]
            rl50 = [0, 2]
            rl51 = [0, 2, 4]
            rl52 = [0, 2, 3]
            rl53 = [0, 2, 3, 4]
            rl54 = [0, 1]
            rl55 = [0, 1, 4]
            rl56 = [0, 1, 3]
            rl57 = [0, 1, 3, 4]
            rl58 = [0, 1, 2]
            rl59 = [0, 1, 2, 4]
            rl60 = [0, 1, 2, 3]
            rl61 = [0, 1, 2, 3, 4]
            testing.equality("Test 104", rl0, locOfOnes(tl0))
            testing.equality("Test 105", rl1, locOfOnes(tl1))
            testing.equality("Test 106", rl2, locOfOnes(tl2))
            testing.equality("Test 107", rl3, locOfOnes(tl3))
            testing.equality("Test 108", rl4, locOfOnes(tl4))
            testing.equality("Test 109", rl5, locOfOnes(tl5))
            testing.equality("Test 110", rl6, locOfOnes(tl6))
            testing.equality("Test 111", rl7, locOfOnes(tl7))
            testing.equality("Test 112", rl8, locOfOnes(tl8))
            testing.equality("Test 113", rl9, locOfOnes(tl9))
            testing.equality("Test 114", rl10, locOfOnes(tl10))
            testing.equality("Test 115", rl11, locOfOnes(tl11))
            testing.equality("Test 116", rl12, locOfOnes(tl12))
            testing.equality("Test 117", rl13, locOfOnes(tl13))
            testing.equality("Test 118", rl14, locOfOnes(tl14))
            testing.equality("Test 119", rl15, locOfOnes(tl15))
            testing.equality("Test 120", rl16, locOfOnes(tl16))
            testing.equality("Test 121", rl17, locOfOnes(tl17))
            testing.equality("Test 122", rl18, locOfOnes(tl18))
            testing.equality("Test 123", rl19, locOfOnes(tl19))
            testing.equality("Test 124", rl20, locOfOnes(tl20))
            testing.equality("Test 125", rl21, locOfOnes(tl21))
            testing.equality("Test 126", rl22, locOfOnes(tl22))
            testing.equality("Test 127", rl23, locOfOnes(tl23))
            testing.equality("Test 128", rl24, locOfOnes(tl24))
            testing.equality("Test 129", rl25, locOfOnes(tl25))
            testing.equality("Test 130", rl26, locOfOnes(tl26))
            testing.equality("Test 131", rl27, locOfOnes(tl27))
            testing.equality("Test 132", rl28, locOfOnes(tl28))
            testing.equality("Test 133", rl29, locOfOnes(tl29))
            testing.equality("Test 134", rl30, locOfOnes(tl30))
            testing.equality("Test 135", rl31, locOfOnes(tl31))
            testing.equality("Test 136", rl32, locOfOnes(tl32))
            testing.equality("Test 137", rl33, locOfOnes(tl33))
            testing.equality("Test 138", rl34, locOfOnes(tl34))
            testing.equality("Test 139", rl35, locOfOnes(tl35))
            testing.equality("Test 140", rl36, locOfOnes(tl36))
            testing.equality("Test 141", rl37, locOfOnes(tl37))
            testing.equality("Test 142", rl38, locOfOnes(tl38))
            testing.equality("Test 143", rl39, locOfOnes(tl39))
            testing.equality("Test 144", rl40, locOfOnes(tl40))
            testing.equality("Test 145", rl41, locOfOnes(tl41))
            testing.equality("Test 146", rl42, locOfOnes(tl42))
            testing.equality("Test 147", rl43, locOfOnes(tl43))
            testing.equality("Test 148", rl44, locOfOnes(tl44))
            testing.equality("Test 149", rl45, locOfOnes(tl45))
            testing.equality("Test 150", rl46, locOfOnes(tl46))
            testing.equality("Test 151", rl47, locOfOnes(tl47))
            testing.equality("Test 152", rl48, locOfOnes(tl48))
            testing.equality("Test 153", rl49, locOfOnes(tl49))
            testing.equality("Test 154", rl50, locOfOnes(tl50))
            testing.equality("Test 155", rl51, locOfOnes(tl51))
            testing.equality("Test 156", rl52, locOfOnes(tl52))
            testing.equality("Test 157", rl53, locOfOnes(tl53))
            testing.equality("Test 158", rl54, locOfOnes(tl54))
            testing.equality("Test 159", rl55, locOfOnes(tl55))
            testing.equality("Test 160", rl56, locOfOnes(tl56))
            testing.equality("Test 161", rl57, locOfOnes(tl57))
            testing.equality("Test 162", rl58, locOfOnes(tl58))
            testing.equality("Test 163", rl59, locOfOnes(tl59))
            testing.equality("Test 164", rl60, locOfOnes(tl60))
            testing.equality("Test 165", rl61, locOfOnes(tl61))
            
            testing.main()
        else:
            for i in karnaughMap(int(sys.argv[1])):
                print i
    else:
        print "Use: $ python karnaugh.py i"
        print "Where i is the number of bits that"
        print "you want for each input."
        # TODO make those print statements clearer.

if __name__ == "__main__":
    main()
