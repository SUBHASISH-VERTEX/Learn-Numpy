'''
np.split()  equaly split
np.hsplit()  horizontaly split
np.vsplit()  verticaly split
'''
import numpy as np
arr = np.array([10,20,50,30])
print(np.split(arr,2))
print(np.hsplit(arr,1))
print(np.hsplit(arr,2))