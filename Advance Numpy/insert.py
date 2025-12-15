import numpy as np
'''
np.insert(array,index,value,axis= none)
array- original array
axis =0, row-wise
axis = 1, coloum wise
'''

arr = np.array([10,20,33,45,22,27,23])
new_arr = np.insert(arr,2,100,axis=0)
print(new_arr)

# index number 3 = 33 that change to 100