#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 


# In[5]:


a=np.arange(1,11)
a


# In[6]:


a.reshape(5,2)


# In[7]:


b= np.random.randint(1,10,(6,5))
b


# In[9]:


b= np.random.randint(1,10,(6,5))
b.a+(3,3)
b


# In[11]:


b.reshape(-1)


# In[12]:


b


# In[13]:


b.flatten()


# In[14]:


print(b)
b+1


# In[15]:


print(b)
b-1


# In[16]:


print(b)
b**2


# In[17]:


print(b)
print(b.sum())
print(b.min())
print(b.max())


# In[18]:


print(b)
print(b.sum(axis=0))
print(b.min(axis=0))
print(b.max(axis=0))


# In[19]:


print(b)
print(b.sum(axis=1))
print(b.min(axis=1))
print(b.max(axis=1))


# In[20]:


a=np.arange(1,7).reshape(2,3)
a


# In[22]:


b=np.arange(11,17).reshape(2,3)
b


# In[23]:


print(a)
print(b)
a+b


# In[24]:


print(a)
print(b)
b-a


# In[25]:


print(a)
print(b)
a*b


# In[27]:


print(a)
print(b)
b%a


# In[28]:


c=np.random.randint(1,5,(5,3))
c


# In[29]:


np.unique(c)


# In[32]:


d=np.sort(c)
d


# In[33]:


np.append(c,d)


# In[36]:


a=np.arange(1,5).reshape(2,2)
a


# In[ ]:





# In[37]:


b=np.arange(6,10).reshape(2,2)
b


# In[38]:


a.T #transpose


# In[40]:


print(a)
print(b)
a.dot(b)


# a=np.random.randint(1,31,(6,5))
# a

# In[43]:


a=np.random.randint(1,31,(6,5)) 
a


# In[44]:


a[1,2]


# In[47]:


a[2:4,1:3]


# In[ ]:





# In[45]:


a[4,2:]


# In[46]:


a[::-1] #reverse the array


# In[48]:


print(a)


# In[49]:


a[a%2==1]


# In[50]:


a[a%2==0]


# In[51]:


a[a%2==1]=9


# In[52]:


print(a)


# In[53]:


a%2==1


# In[ ]:





# In[42]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




