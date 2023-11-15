
import math
import sys
import matplotlib.pyplot as plt
import numpy as np
path = sys.executable
 
print(path)

k="1"

def aa(k):
    print("sss"+k)
    
tan = np.tan(45*np.pi/180)  
print ("tan=",tan)  
tan_v = np.arctan(1)/np.pi*180   
    
print("t=",tan_v)
aa("11")

x = np.arange(0, 1, 0.001) #從-5到5，間隔是1，不含結束點5，

print(x)
y = (1-x)*(1-x)
print(y)
plt.plot(x,y)
y = (1-x)*x*2
print(y)
plt.plot(x,y)
plt.axhline(y=0)#x軸
plt.axvline


a=[1.1,1.6,11.4,4.1,5.3,17.5,9.4,11.5,12.1]

A = np.array([[1.1]*9]*3)
A[0]=a
f=[7.9,24.8,-28.8,42.6,29.6,-34.6,-3.1,-28.7,-39.6]
k=a
for i in range(2):
    for j in range(9):    
        k[j]=k[j]*k[j]
    A[i+1]=k
print("oo")
print(A)       
b = np.array([9, 8, 3])
x = np.linalg.solve(A, f)

print("ok")
print(x)









