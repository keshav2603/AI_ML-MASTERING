import numpy as np

# l1= [1,2,3,4]
# arr1 = np.array([20,30,40,50])
# arr2 = np.array([20,30,40,50])
# print(arr1+arr2)
# print(arr1-arr2)
# print(arr1*arr2)
# print(arr1/arr2)
# print(l1)

# print(np.empty(2))    print a empty array 
# print(np.arange(2,10,2))

# arr3 = np.array([20, 30, True])
# # print(arr3)

# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(np.concatenate(arr))
# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# b = arr.reshape(2,2,2)
# print(b)

# arr1 =np.arange(10)
# # print(np.reshape(arr1, (2,1,5)))
# # print (arr1[np.newaxis,np.newaxis])
# print(np.expand_dims(arr1, 0))
# print(np.expand_dims(arr1, 1))

# print(arr1[arr1>5])

# a = np.array([1, 2, 3, 4, 5, 6, 7, 8,9, 10, 11, 12,13, 14, 15, 16])
# # b = np.nonzero(a < 5)
# # print(a[1:])
# # print(np.hsplit(a,( 3,2)))

# b1=a[0:4]
# b1[0]=99
# print(b1)
# # print(a)
# rng = np.random.default_rng().integers(10, size=(2,4)) 
# # # print(rng.random((2,4)))
# # # print(rng) 
# # print(rng.integers(10, size=(2,4))) 
# # a,b=np.unique(rng,return_counts=True)
# a,b=np.unique(rng,axis=0)
# print(a,b)

# a= np.arange(10).reshape((2,5))
# print(a.flatten())