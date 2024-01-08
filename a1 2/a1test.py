"""
Test script for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

Author: Mr. Park
"""
import a1

def testA():
    print(a1.exchange('USD','CUP',2.5))
    pass

testA()
print('Module a1 passed all tests')