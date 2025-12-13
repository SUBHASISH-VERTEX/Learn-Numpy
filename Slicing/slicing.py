import numpy as np
arr= np.array([1,2,3,4,5,6,7])
print("slicing")
print(arr[1:5])
print(arr[1:3])
print(arr[4:6])
print(arr[:64])
print(arr[4:])

# negative slicing
print("negative indexing: ")
print(arr[-3:-1])
print(arr[-6:-1])
print(arr[-5:-2])
print(arr[-1:])
print(arr[-3:-1])

# step
# # [start, end, step]
print("step method: ")
print(arr[1:5:2])
print(arr[1:6:2])
print(arr[1:4:2])
print(arr[:5:2])
print(arr[2::2])