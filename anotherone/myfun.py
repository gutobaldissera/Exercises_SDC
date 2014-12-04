import numpy as np

def is_odd(a):
   if ( float(a) < 1.0 )  :
        return False
   elif ( float(a)%1.0 > 1  ) :
        return False 
   elif ( float(a)%2.0 == 1.0 ) :
        return False
   else: 
        return True	

 


