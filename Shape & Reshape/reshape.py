import numpy as np
# reshape 1-d to 2-d
print(" 1-d array to 2-d array: ")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)  #4-row,3-coloum
print(newarr)

# reshape 1-d to 3-d
print("1-d arry to 3-d array:")
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr2 = arr.reshape(2, 3, 2)

print(newarr2)