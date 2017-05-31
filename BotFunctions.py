"""

Collection of functions that the bot can run.

"""

def TestFunc1(memory):
    print "Test Func1 has been called"
    return memory

def TestFunc2(memory):
    print "Test Func2 has been called"
    return memory

def TestFunc3(memory):
    print "Test Func3 has been called"
    return memory

FUNCTIONS = {
    "hi": TestFunc1,
    "2": TestFunc2,
    "3": TestFunc3
}

