from Ffile import *


#def test_is_integer():
#	assert is_integer(1.5) == False ,         'fail integer number function' 
#	assert is_integer(1.0) == True ,          'fail integer number function' 

def test_is_odd():
        assert is_odd(2) == False  , 'fail is_odd function, for even'
        assert is_odd(1) == True   , 'fail, is_odd function, for odd'
        assert is_odd(-1) == False , 'fail, is_odd function, negative number'
	assert is_odd(3.3)== False , 'fail, is_odd function, float number'


