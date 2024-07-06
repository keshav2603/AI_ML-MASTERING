import numpy as np

# basics of numpy 

# a = np.array([1,2,3,4],dtype="int16")
# b=np.array([[1,2],[3,4]])
# print(a, a.ndim, a.shape)
# print(b, b.ndim, b.shape)

# print(a.dtype)
# print(a.itemsize)
# print(a.nbytes)
# # print(b.dtype)
# # print(b.itemsize)
# # print(b.size)

# assessing elements 2d array

# a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a.shape)
# print(a[1,5])
# print(a[0,])
# print(a[:,0])
# print(a[0,1:6:2])

# a[1,5] = 20
# a[:,2]=[12,3]
# print(a)

# 3d array
# a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(a)
# print(a[0,1,1])

# all zeroes matrix
# a= np.zeros([2,2,2])
# print(a)

# all ones matrix
# a= np.ones([2,2,2])
# print(a)

# any other number
# a = np.full((2,2), 99)
# print(a)

# genrate random number
a=np.random.rand(2,4)
print(a)