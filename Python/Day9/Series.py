#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


s=pd.Series([10,20,30])
s


# In[5]:


s.name="Temp"
s


# In[6]:


s.size # no of elements


# In[7]:


s.shape #shape of Series


# In[8]:


s.dtype #data type


# In[9]:


s.index #index of Series


# In[10]:


s.index=['a','b','c']  #modify index values
s


# In[12]:


s1=pd.Series((11,22,33),index=['a','b','c'])
s1


# In[13]:


s2=pd.Series() #empty series 


# In[14]:


s


# In[15]:


s+1 #mathamatical operations on Series 


# In[16]:


s-2 #mathamatical operations on Series 


# In[17]:


s%5 #mathamatical operations on Series 


# In[19]:


print(s)
print(s1)


# In[20]:


s+s1 #mathamatical operations on two Series 


# In[21]:


s1-s#mathamatical operations on two Series 


# In[22]:


s1*s #mathamatical operations on two Series 


# In[23]:


s['a'] #accessing value using index name


# In[24]:


s.loc['a'] #accessing value using index name


# In[25]:


s['a':'c'] #accessing value using index name using slicing  #range is included


# In[26]:


s.loc['a':'c'] #accessing value using index name using slicing and loc #range is included


# In[27]:


s[0] #accessing value using index number


# In[28]:


s[0:2]#accessing value using index number and slicing  #range is excluded


# In[29]:


s.iloc[0] #accessing value using index number and iloc 


# In[30]:


s.iloc[0:3] #accessing value using index number and iloc slicing #range is excluded


# In[32]:


a=np.random.randint(1,20,15)
s=pd.Series(a)
s


# In[33]:


s.head()#return first 5 rows


# In[34]:


s.head(8)#return first 8 rows


# In[35]:


s.tail()#return last 5 line


# In[36]:


s.tail(2)#return last 2 line


# In[37]:


s.count() #no of records


# In[38]:


s.min() # minimum value


# In[39]:


s.max() # maximum value


# In[40]:


s[s.index%2==1] #return record which are having odd index


# In[41]:


s[13]=20 #modify value using index


# In[42]:


s


# In[43]:


s[15]=100 #added new record as 15 is not present in index


# In[44]:


s


# In[45]:


s[150]=100 #add new record as 15 is not present in index


# In[46]:


s


# In[47]:


s=pd.Series((10,20,30))


# In[48]:


s


# In[52]:


s1=pd.Series((1,2,3),index=[1,2,'c'])


# In[ ]:





# In[53]:


s1


# In[54]:


s+s1


# In[57]:


s=pd.Series({1:10,'Rima':20,3:30})


# In[ ]:





# In[58]:


s


# In[61]:


s=pd.Series({1:[10,20,30],'Rima':[20,30,30],3:[30,40,50]})
s


# In[ ]:





# In[62]:


df=pd.DataFrame({1:[10,20,30],'Rima':[20,30,30],3:[30,40,50]})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




