import numpy as np
arr1 = np.array([1,5,6,3,4])
x = arr1.view()     #create  view method
arr1[1] = 45   #int change index 1 
print(arr1)
print(x)


'''
it means view () method x is not change and arr1 is not change.
'''
