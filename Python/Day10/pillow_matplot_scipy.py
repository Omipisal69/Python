#!/usr/bin/env python
# coding: utf-8

# In[4]:


from PIL import Image 


# In[6]:


img=Image.open(r"C:\DBDA\Python\Day10\cartoon1.png")
img.show()
display(img)


# In[7]:


print(img.size)


# In[8]:


print(img.filename)


# In[9]:


print(img.mode)


# In[10]:


print(img.format)


# In[11]:


angle=50
img=Image.open(r"C:\DBDA\Python\Day10\cartoon1.png")
nimg=img.rotate(angle)
display(img)
display(nimg)


# In[13]:


angle=180
img=Image.open(r"C:\DBDA\Python\Day10\cartoon1.png")
nimg=img.rotate(angle)
nimg.save(r"C:\DBDA\Python\Day10\cartoon1_rotate.png")
nimg1= Image.open(r"C:\DBDA\Python\Day10\cartoon1_rotate.png")
display(nimg1)


# In[17]:


img=Image.open(r"C:\DBDA\Python\Day10\cartoon.jpg")
display(img)
nimg=img.reduce((5,5))
display(nimg)


# In[18]:


img=Image.open(r"C:\DBDA\Python\Day10\cartoon.jpg")
display(img)
nimg=img.resize((350,350))
display(nimg)


# In[22]:


print(img.width)


# In[23]:


img=Image.open(r"C:\DBDA\Python\Day10\cartoon.jpg")
display(img)
img.thumbnail((10,10))
display(img)


# In[25]:


img=Image.open(r"C:\DBDA\Python\Day10\cartoon.jpg")
img=img.convert("L")
display(img)


# In[26]:


import matplotlib.pyplot as plt


# In[27]:


l1=["s1","s2","s3","s4","s5","s6"]
l2=[23 ,34,5,40,12,4]
plt.plot(l1,l2)


# In[28]:


l1=["s1","s2","s3","s4","s5","s6"]
l2=[23 ,34,5,40,12,4]
plt.plot(l1,l2)
plt.title("Result")
plt.xlabel("Students")
plt.ylabel("Marks")


# In[29]:


l1=["s1","s2","s3","s4","s5","s6"]
l2=[23 ,34,5,40,12,4]
plt.plot(l1,l2,marker="*",color="r")
plt.title("Result")
plt.xlabel("Students")
plt.ylabel("Marks")


# In[30]:


l1=["s1","s2","s3","s4","s5","s6"]
l2=[23 ,34,5,40,12,4]
plt.scatter(l1,l2,marker="3",color="b")
plt.title("Result")
plt.xlabel("Students")
plt.ylabel("Marks")


# In[31]:


l1=["s1","s2","s3","s4","s5","s6"]
l2=[23 ,34,5,40,12,4]
plt.bar(l1,l2,color="m")
plt.title("Result")
plt.xlabel("Students")
plt.ylabel("Marks")


# In[33]:


import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read #import the required function from the module
samplerate, data = read(r'C:\DBDA\Python\Day10\test.wav')
print(samplerate) #echo samplerate
print(data) #echo data -> note that the data is a single dimensional array


# In[34]:


import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read #import the required function from the module
samplerate, data = read(r'C:\DBDA\Python\Day10\test.wav')
print(samplerate) #echo samplerate
print(data) #echo data -> note that the data is a single dimensional array
duration = len(data)/samplerate
time = np.arange(0,duration,1/samplerate) #time vector
plt.plot(time,data)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('CantinaBand3.wav')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:


help(Image)


# In[ ]:





# In[ ]:





# In[ ]:




