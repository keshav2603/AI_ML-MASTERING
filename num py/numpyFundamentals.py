import numpy as np

# Basics of NumPy
'''
a = np.array([1, 2, 3, 4], dtype="int16")
b = np.array([[1, 2], [3, 4]])
print(a, a.ndim, a.shape)
print(b, b.ndim, b.shape)
print(a.dtype, a.itemsize, a.nbytes)
print(b.dtype, b.itemsize, b.size)'''

# Accessing elements in a 2D array
'''
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a.shape)
print(a[1, 5])
print(a[0, :])
print(a[:, 0])
print(a[0, 1:6:2])

a[1, 5] = 20
a[:, 2] = [12, 3]
print(a)
'''

# 3D array
'''
a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a)
print(a[0, 1, 1])
'''

# Special matrices
'''
a = np.zeros([2, 2, 2])
print(a)
a = np.ones([2, 2, 2])
print(a)
a = np.full((2, 2), 99)
print(a)
'''

# Random numbers
'''
b = np.ones((2, 2, 2))
a = np.random.rand(2, 4)
c = np.random.random_sample(b.shape)
print(a)
'''

# Random integers
'''
a = np.random.randint(10, 100, size=(4, 4, 4))
print(a)
'''

# Identity matrix
'''
a = np.identity(3)
print(a)
'''

# Repeat array
'''
a = np.array([[1, 2, 3]])
r1 = np.repeat(a, 3, axis=0)
print(r1)
'''

# Exercise: Create a specific matrix
'''
output = np.ones((5, 5))
z = np.zeros((3, 3))
z[1, 1] = 9
output[1:4, 1:4] = z
print(output)
'''

# Be careful while copying arrays
'''
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100
print(a)
'''

# Using math with arrays
'''
a = np.array([1, 2, 3, 4])
print(a + 2)
print(a - 2)
print(a / 2)
print(a % 2)
print(a ** 2)
print(a * 2)
b = np.array([[10], [20], [30], [40]])
print(a * b)
print(np.tan(a))
'''

# np mat myltipier and determinent
'''
a= np.ones((2,3))
b=np.full((3,2),2)
print(np.matmul(a,b))
c=np.identity(4)
print(np.linalg.det(c))
'''

# statistics
'''
a=np.array([[1,2,3],[4,5,6]])
print(np.min(a))
print(np.min(a,axis=0))
print(np.min(a, axis=1))
print(np.max(a))
print(np.max(a,axis=0))
print(np.max(a, axis=1))
print(np.sum(a))
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))
'''

# organising array
'''
before =np.array([[1,2,3,4],[5,6,7,8]])
after = before.reshape((8,1))
print(after)
'''

# vertical stacking
'''
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
v3=np.vstack([v1,v2,v1,v2])
print(v3)
'''

# horizantal stack
'''
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
v3=np.hstack((v1,v2,v1,v2))
print(v3)
'''

# miscellaneous
a=np.genfromtxt("data.txt", delimiter=",")
print(a)