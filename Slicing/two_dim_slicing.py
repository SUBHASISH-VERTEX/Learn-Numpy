import numpy as np
twoD_arr =np.array([[4,5,6,7,8],[1,6,4,9,2]])

# [row,coloum]  
print(twoD_arr[1,1:4])
print(twoD_arr[1:2,1:4])
print(twoD_arr[0:2,1:3])
print(twoD_arr[1:2,0:4])

'''
coloum 0,1,2,3,4
row-0 [4,5,6,7,8],
row-2 [1,6,4,9,2]]
'''

# [1:2,1:4]
'''
in this case  1:2 --> row   means 1 row and 2 row 
              1:4 -->coloum   meaans 1 coloumto 3 coloum
              in this row and coloum common element is [1:2,1:4]...
'''
