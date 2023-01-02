#!/usr/bin/env python
# coding: utf-8

# # Numpy Demo

# In[3]:


a="hello"
print(a)
b="hi"
print(b)


# In[4]:


import numpy as np


# In[6]:


l1=[10,20,30]
a=np.array(l1)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[8]:


l1=[[1,2,3],[10,20,30]]
a=np.array(l1,dtype=float)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[9]:


l1=[[[1,2,3],[10,20,30]],[[100,200,300],[1000,2000,3000]]]
a=np.array(l1,dtype=int)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.itemsize)
print(a.dtype)
print(a.data)


# In[13]:


a=np.ones(5)
print(a)
a=np.ones(5,dtype=complex)
print(a)
a=np.ones(5,dtype=int)
print(a)

a=np.ones((5,2))
print(a)
a=np.ones((2,5),dtype=complex)
print(a)
a=np.ones((2,3,5),dtype=int)
print(a)


# In[14]:


a=np.zeros(5)
print(a)
a=np.zeros(5,dtype=complex)
print(a)
a=np.zeros(5,dtype=int)
print(a)

a=np.zeros((5,2))
print(a)
a=np.zeros((2,5),dtype=complex)
print(a)
a=np.zeros((2,3,5),dtype=int)
print(a)


# In[15]:


a=np.empty(5)
print(a)
a=np.empty(5,dtype=complex)
print(a)
a=np.empty(5,dtype=int)
print(a)

a=np.empty((5,2))
print(a)
a=np.empty((2,5),dtype=complex)
print(a)
a=np.empty((2,3,5),dtype=int)
print(a)


# In[16]:


a=np.full(5,8,dtype=int)
print(a)

a=np.full((5,2),10)
print(a)

a=np.full((2,3,5),7,dtype=int)
print(a)


# In[17]:


a=np.identity(5)
print(a)


# In[19]:


a=np.eye(5,3,k=-1)
print(a)


# In[20]:


a=np.eye(5,3,k=1)
print(a)


# In[22]:


a=np.random.random(5)
print(a)
a=np.random.random((5,3))
print(a)


# In[23]:


a=np.random.randint(1,10,5)
print(a)
a=np.random.randint(20,40,(5,3))
print(a)


# In[27]:


a=np.arange(1,12)
print(a)

a=np.arange(1,13).reshape(2,6)
print(a)

a=np.arange(1,13).reshape(4,3)
print(a)

a=np.arange(1,13).reshape(2,3,2)
print(a)


# In[29]:


a=np.arange(1,13).reshape(4,3)
print(a)
print(a+2)


# In[31]:


print(a)
print(a/2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




