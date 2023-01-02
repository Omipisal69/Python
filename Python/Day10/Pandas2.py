#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_excel(r"C:\DBDA\Python\Day9\Order_data.xlsx")
df


# In[3]:


df.max()


# In[4]:


df.min()


# In[5]:


df.corr() #imp


# In[6]:


df["Unit Cost"]


# In[7]:


df["Unit Cost"].astype(int) #change datatype float to int


# In[8]:


df


# In[9]:


df.count()


# In[10]:


df["cust"].value_counts()


# In[11]:


df["cust"].value_counts().max() #return maximum record


# In[12]:


df.sort_values("cust")


# In[13]:


df.sort_values("cust",ascending=False)


# In[14]:


df.sort_values(["cust","Item"],ascending=False)


# In[20]:


g1=df.groupby("cust")


# In[21]:


g1


# In[ ]:





# In[17]:


g1.groups


# In[19]:


g1.first()


# In[22]:


g1.get_group("Kavita")


# In[25]:


g1=df.groupby("cust").sum()
g1


# In[27]:


g1=df.groupby("cust")
g1.get_group("Kavita")


# In[30]:


g1=df.groupby("cust")

print(g1.get_group("Thompson"))
g1=df.groupby("cust").max()
print(g1)


# In[31]:


df


# In[32]:


df["Temp"]=np.nan
df


# In[33]:


df["Temp1"]=10
df


# In[34]:


df["Temp1"]=df["Total"]+100
df


# In[35]:


del df["Temp"]
df


# In[36]:


df.drop(columns='Temp1') #drop column Temp1


# In[37]:


df1=df.drop(columns=['OrderDate','Temp1']) #drop column OrderDate and Temp1
df1


# In[38]:


df1.loc['k']= 78 ,"South","Temp","Laptop",1,350000,35000 #insert new row


# In[39]:


df1


# In[40]:


df1.loc['k','cust']


# In[41]:


df1.loc['k','cust']="Rashmi" #update row


# In[42]:


df1


# In[44]:


df1.loc['k',['cust','Item']]


# In[45]:


df1.loc['k',['cust','Item']]="kirti","Mobile"
df1


# In[49]:


df1.drop(index='k',inplace=False) #Delete kth row from df and return new modified df

df1.drop(index='k',inplace=True) #Delete kth row from Df1
df1


# In[50]:


exam_data  = {'name': ['Sonu', 'Raja', 'Ketaki', 'Rupa', 'Radha', 'Reshma', 'Keshav', 'Narendra', 'Rani', 'Kittu'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df= pd.DataFrame(exam_data,index=labels)
df


# In[51]:


df.dropna() #delete rows having none values


# In[53]:


df.dropna(axis=1) #delete columns having none values


# In[55]:


df["score"].isnull()


# In[59]:


exam_data  = {'name': ['Sonu', 'Raja', 'Ketaki', 'Rupa', 'Radha', 'Reshma', 'Keshav', 'Narendra', 'Rani', 'Kittu'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df= pd.DataFrame(exam_data,index=labels)
df


# In[65]:


df1= df['score'].fillna(100)


# In[67]:


df['qualify']=df['qualify'].map({'yes':True,'no':False})


# In[68]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[63]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[57]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[24]:





# In[ ]:





# In[ ]:





# In[ ]:




