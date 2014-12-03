import sys
import numpy as np


data=sys.argv[1:] #read the command line input 

arr=np.array([]) #create a empty array

for a in data:   
  arr=np.append(arr,float(a)) #append every value to array
 
print arr
print type(arr)
print len(arr)


test_is_odd()

