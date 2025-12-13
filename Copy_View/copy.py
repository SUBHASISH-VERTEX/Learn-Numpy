import numpy as np
arr =np.array([1,2,4,5,6,7])
# creae a copy
x = arr.copy()
# change the value in arr
arr[0] = 42
# array is chamnge 
print(arr)
# but x is not change because it is copy as arr . i am operation arr
print(x)