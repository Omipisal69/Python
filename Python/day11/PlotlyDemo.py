#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
fig=px.line(x=["India","Pak","England"],y=[137,10,45])
fig.show()


# In[2]:


import plotly.express as px
df=px.data.iris()
print(df.head())


# In[8]:


import plotly.express as px
df=px.data.iris()
fig = px.line(df,x="sepal_width",y="sepal_length",color="species")
fig.show()


# In[9]:


import plotly.express as px
df=px.data.iris()
fig = px.scatter(df,x="sepal_width",y="sepal_length",color="species")
fig.show()


# In[ ]:





# In[11]:


import plotly.express as px
df=px.data.iris()
fig = px.bar(df,x="species",y="sepal_length",color="species")
fig.show()


# In[12]:


import plotly.express as px
df=px.data.iris()
fig = px.box(df,x="species",y="sepal_length",color="species")
fig.show()


# In[13]:


import plotly.express as px
df=px.data.iris()
fig = px.box(df,x="species",y="sepal_length")
fig.show()


# In[16]:


import plotly.express as px
df=px.data.iris()
fig = px.violin(df,x="species",y="sepal_length",color="species")
fig.show()


# In[17]:


import plotly.express as px
df=px.data.iris()
fig = px.line_3d(df,x="species",y="sepal_length",z="sepal_width",color="species")
fig.show()


# In[18]:


import plotly.express as px
df=px.data.iris()
fig = px.scatter_3d(df,x="species",y="sepal_length",z="sepal_width",color="species")
fig.show()


# In[19]:


import plotly.express as px
df=px.data.tips()
print(df)


# 

# In[27]:


import numpy as np
import plotly.graph_objects as go
xd=np.random.randint(1,20,30)
yd=np.random.randint(1,20,30)

fig=go.Figure(go.Scatter(x=xd,y=yd,mode="markers"))
fig.show()


# In[28]:


import plotly
import plotly.graph_objects as go
cnt= ["india","Pak","nepal","Bhutan","Mexico","Texas"]
ydata= [3000,200,450,670,890,480]
fig=go.Figure([go.Pie(labels=cnt,values=ydata)])
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




