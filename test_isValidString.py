from isValidString import *
import pytest

# List data 
listData  = ['()', '()[]{}']
@pytest.mark.parametrize('s', listData)

def testIsValidString(s):
    result = isValidString(s)
    #then
    assert result == 'valid'
    
def testIsInvalidString() :
    s ='([)]'
    assert isValidString(s) == "invalid"

def testThrowException():
    s = '}'
    with pytest.raises(QueueIsOutOfRange):
        isValidString(s)
    # with pytest.raises(IndexError):
    #     isValidString(s)
        
def testStringIsTooLong():
    s = "{{{{{{{{{{}}}}}}}}}}{{{{{{{{{{}}}}}}}}}}{{{{{{{{{{}}}}}}}}}}{{{{{{{{{{}}}}}}}}}}{{{{{{{{{{{}}}}}}}}}}}{{{{{{{}}}}}}}"
    assert isValidString(s) == 'invalid'

def testStringIsTooShort():
    s = ""
    assert isValidString(s) == 'invalid'

