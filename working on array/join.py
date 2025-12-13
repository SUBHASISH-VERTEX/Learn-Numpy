# import numpy as np
# arr1 = ([1,5,6,7])
# arr2 = ([2,3,4,5])
# arr = np.concatenate((arr1,arr2))
# print(arr)

print("concatination in axis")
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

# stack method
print("stack method:")
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)

print(arr)

# vstack - vertical stack
print("vertrical stack")
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))

print(arr)

# dtack - vertical stack
print("digonal stack")
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))

print(arr)
