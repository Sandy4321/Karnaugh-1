# testing.py
# 2014-05-09+15:17:00

# I do not currently know a better way to do this
global passed
global failed
passed = 0
failed = 0

# Tests if item1 and item2 are equal
# Parameter(s):
#     item1 is an object
#     item2 is an object
def equality(testName, item1, item2):
    global passed
    global failed
    if(item1 == item2):
        passed = passed + 1
        return True
    else:
        failed = failed + 1
        print "\n" + testName + ":"
        print "\t" + str(item1) + " does not equal " + str(item2)
        print "even though it should.\n"
        return False

# Tests if item1 and item2 are unequal
# Parameter(s):
#     item1 is an object
#     item2 is an object
def inequality(testName, item1, item2):
    global passed
    global failed
    if(item1 != item2):
        passed = passed + 1
        return True
    else:
        failed = failed + 1
        print "\n" + testName + ":"
        print "\t" + str(item1) + " equals " + str(item2)
        print "even though it should not.\n"
        return False

def main():
    print str(passed + failed) + " tests ran."
    print str(passed) + " tests passed."
    print str(failed) + " tests failed."

if __name__ == "__main__":
    main()
