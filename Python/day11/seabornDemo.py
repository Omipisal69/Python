#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sn


# In[4]:


dsets=sn.get_dataset_names()
print(dsets)

df=sn.load_dataset('tips')
df.info()

df.head()


# In[6]:


cls=sn.color_palette()
sn.palplot(cls)


# In[8]:


cls=sn.color_palette("deep",12)
sn.palplot(cls)
cls=sn.color_palette("bright",12)
sn.palplot(cls)
#deep, muted, bright, pastel, dark, colorblind


# In[12]:


cls=sn.color_palette("deep",12)
sn.palplot(cls)
cls=sn.color_palette("PiYG",12)
sn.palplot(cls)
cls=sn.color_palette("GnBu",15)
sn.palplot(cls)


# In[16]:


df.head()
sn.lineplot(x="total_bill",y="tip",hue="sex",data=df)


# In[17]:


sn.lineplot(x="total_bill",y="tip",hue="day",data=df)


# In[19]:


sn.displot(x="total_bill",data=df,kde=True)


# In[20]:


sn.displot(x="total_bill",data=df,kde=True,color="r")


# In[22]:


sn.lmplot(x="total_bill",y="tip",hue="day",data=df)


# In[23]:


sn.lmplot(x="total_bill",y="tip",data=df)


# In[27]:


sn.set(style="darkgrid")
sn.lmplot(x="total_bill",y="tip",hue="sex",data=df)


# In[28]:


sn.set(style="dark")
sn.lmplot(x="total_bill",y="tip",hue="sex",data=df)


# In[31]:


sn.set(style="white")
sn.relplot(x="total_bill",y="tip",data=df)


# In[ ]:





# In[32]:


sn.set(style="white")
sn.relplot(x="total_bill",y="tip",hue="sex",data=df)


# In[35]:


sn.relplot(x="total_bill",y="tip",hue="sex",data=df,col="day",col_wrap=2)


# In[36]:


sn.relplot(x="total_bill",y="tip",hue="sex",data=df,col="day")


# In[ ]:





# In[34]:


sn.relplot(x="total_bill",y="tip",hue="day",data=df,col="sex")


# In[39]:


sn.barplot(x="total_bill",y="tip",data=df)


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




