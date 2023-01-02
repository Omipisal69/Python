#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


df=pd.DataFrame()
df


# In[4]:


a=np.array([10,20,30])
a1=np.array([-10,-20,30])
a2=np.array([10,20,-30,40])
df=pd.DataFrame([a,a1,a2],columns=['a','b','c','d'])


# In[5]:


df


# In[6]:


df.index


# In[7]:


df.columns


# In[8]:


df.info


# In[9]:


df.describe()


# In[10]:


df.min()


# In[11]:


df.max()


# In[12]:


mydict={
    'Prod_ID':[101,102,103,104,105,106,107],
    'Prod_name':['Watch','Bag','Shoes','Smartphone','Books','Oil','Laptop'],
    'Category':['Fashion','Fashion','Fashion','Electronics','Study','Grocery','Electronics'],
    'Price':[299.0,1350.50,2999.0,14999.0,145.0,110.0,79999.0],
    'City':['Delhi','Mumbai','Chennai','Kolkatta','Delhi','Chennai','Bengalore']
}
df=pd.DataFrame(mydict)
df


# In[13]:


df.info


# In[14]:


df.describe()


# In[15]:


df.min()


# In[16]:


df.max()


# In[17]:


df.index


# In[18]:


df.columns


# In[19]:


df["Prod_ID"]


# In[20]:


df[["Prod_ID","Price"]]


# In[22]:


df[df["Price"]<200]


# In[23]:


df


# In[24]:


df[(df["Price"]<200)|(df["City"]=="Delhi") ]


# In[25]:


df[(df["Price"]<200)&(df["City"]=="Delhi") ]


# In[26]:


df["City"].value_counts()


# In[27]:


df["City"]


# In[29]:


df["City"].head(2)


# In[30]:


df.head()


# In[31]:


df.head(3)


# In[32]:


df[["Prod_ID","Price"]].tail(4)


# In[33]:


df[:] #complete df


# In[35]:


df[1::2]


# In[41]:


df[1::2]


# In[44]:


df.loc[1::2,"Prod_name":"Price"]


# In[46]:


df.iloc[1::2,1:4]


# In[47]:


df.sort_values("Price")


# In[48]:


df.sort_values("Price",ascending=False)


# In[52]:


df.sort_values(["Category","Price"],ascending=[True,True])


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




