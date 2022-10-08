#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Name-Somya Gautam
#Roll Number- 2020BTechCSE076
#Batch-A

# Magic Square

import pandas as pd
import numpy as np

n = int(input("Enter size of matrix (odd only): "))
constant = int(n*(n**2 + 1)/2)

arr1 = [[0 for x in range(n)] for y in range(n)]
arr = np.array(arr1)

i = 0
j = n//2

arr[i,j] = 1

for k in range(2,n*n+1):
    i-=1
    j+=1
    if(i == -1 and j == n):
        i=0
        j=n-2
    if(i == -1):
        i = n-1
    if(j == n):
        j = 0
    if arr[i,j]!=0:
        i+=1
        j-=2
    arr[i,j] = k

print(arr)
print("Constant value : ",constant)


# In[ ]:




