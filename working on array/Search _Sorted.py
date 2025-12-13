import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)

print(x)


arr1= np.array([6, 7, 8, 9])

x = np.searchsorted(arr1,8,side='right')

print(x)