"""
Test script for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

Author: Mr. Park
"""
import a1

def testA():
    assert (a1.eval("3 + 4") == 7), "should be '7'"

        

testA()
print('Module a1 passed all tests')