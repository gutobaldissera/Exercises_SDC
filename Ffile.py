import sys
import numpy as np

data=sys.argv[1:]
print data

arr=np.array([])

for a in data:
  arr=np.append(arr,float(a))
 

print arr
print type(arr)



