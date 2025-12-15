import numpy as np
arr_2d = np.array([[1,2,3,4],[6,7,5,4]])
print(arr_2d)
new_arr_2d =np.insert(arr_2d,1,[5,6,7,4],axis = 0)
print(new_arr_2d)