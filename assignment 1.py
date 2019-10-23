#!/usr/bin/env python
# coding: utf-8

# # task 1

# In[1]:


print("Hello World!")


# 2

# In[2]:


for i in range(2000,3200):
    if i%7==0 and i%5 !=0:
        print(i,end=',') 


# In[3]:


s='srinu s'


# In[4]:


a=s[:5]


# In[5]:


b=s[5:6]


# In[6]:


b+' '+a


# In[7]:


a=s.split()


# In[8]:


' '.join(a[::-1])


# In[9]:


a[-1]+' '+a[0]


# In[10]:


c='srinivasa rao s'


# In[11]:


c[-1]+' '+c[:-1]


# 4

# In[12]:


v=4/3*22/7*12**3
v


# In[13]:


import math


# In[14]:


v=4/3*math.pi*12**3
v


# # task 2

# 1

# In[15]:


x=input('Enter numbers:')
print(x,sep=',')
lit=[]
for i in x:
    lit.append(int(i))
print(lit)    
    


# 2

# In[23]:


row = int(input("Enter number : "))

for i in range (0, row):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range (row, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("\r")


# 3

# In[17]:


W= 'AcadGild'


# In[18]:


w=input('type nmae:')
w[::-1]


# 4

# In[19]:


print('WE, THE PEOPLE OF INDIA,\n\t having solemnly resolved to constitute India into a SOVEREIGN,!\n\t\t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t  and to secure to all its citizens')


# In[ ]:




