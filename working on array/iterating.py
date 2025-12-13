import numpy as np
print("1d array iterating")
arr = np.array([1,2,3,4,5])
for i in arr:
    print(i)

# 2-d array
print("2-d array iteratin")
import numpy as np
arr2= np.array([[1, 2, 3], [4, 5, 6]])

for x in arr2:
     print(x)

# Iterating 3-D Arrays
import numpy as np
print("Iterating 3-D Arrays")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)