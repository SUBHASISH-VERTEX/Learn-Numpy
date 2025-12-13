import numpy as np
arr = np.array([1,4,3,2,5,6,7])
x = np.where(arr==4)
print(x)

arr1= np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr1%2==1)

print(x)