# -*- coding: utf-8 -*-

import numpy as np
a=np.array([2,3,4])
print(a)
print(type(a))

#Range
a=np.arange(1,12,2)
print(a)

#floating  point array
a=np.linspace(1,12,6)
print(a)

#Reshape two dimensional array
a = a.reshape(3,2)
print(a)

print(a.size)
print(a.dtype)
print(a.itemsize)

b = np.array([(1,5,2,3),(4,5,6)])
print(b)

print(a<4)
a*=3
print(a)

a=np.zeros((3,4))
print(a)
a=np.ones(10)
print(a)
a=np.array([2,3,4],dtype=np.int16)
print(a)

a=np.random.random((2,3))
print(a)

print(np.set_printoptions(precision=2,suppress=True))
print(a)

a=np.random.randint(0,10,5)
print(a)

print("sum :",a.sum())
print("max :",a.max())
print("min :",a.min())
print("mean :",a.mean())
print("variance :",a.var())
a=np.random.randint(1,10,6)
a=a.reshape(3,2)
a.sum(axis=1)
a.sum(axis=0)

data=np.loadtxt("data.txt",delimiter=",")
print(data)

data = np.arange(10)
print(data)
a = np.random.shuffle(data)

print(a)
