#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re 


# In[4]:


s="The quick broun fox jumps over the lazy dog."
print(re.findall('o',s))
print(re.search('o',s))
print(re.split('o',s))
print(re.sub('o',"oo",s))

for i in re.finditer('o',s):
    print(i)
    
pat=re.compile(r'o')  
print(re.findall(pat,s))
print(re.search(pat,s))
print(re.split(pat,s))
print(re.sub(pat,"oo",s))

for i in re.finditer(pat,s):
    print(i)


# In[7]:


s="The quick broun fox jumps over the lazy dog."
pat=re.compile(r'^The')  
for i in re.finditer(pat,s):
    print(i)


# In[8]:


s="The quick broun fox jumps over the lazy dog"
pat=re.compile(r'dog$')  
for i in re.finditer(pat,s):
    print(i)


# In[9]:


s="The quick broun fox jumps over the lazy dogpp"
pat=re.compile(r'dog..$')  
for i in re.finditer(pat,s):
    print(i)


# In[11]:


s="The quick broun fox jumps over fee the lazy fea dogpp"
pat=re.compile(r'f..')  
for i in re.finditer(pat,s):
    print(i)


# In[12]:


s="The quick broun fox jumps over fee the lazy fea dogpp"
pat=re.compile(r'q.+k')  
for i in re.finditer(pat,s):
    print(i)


# In[16]:


s="The quick 11 broun fox 12 jumps over fee 456 the 34567 lazy fea dogpp"
pat=re.compile(r'\d{5} | \d{3}')  
for i in re.finditer(pat,s):
    print(i)


# In[17]:


s="The quick 11 broun fox 12 jumps_over fee 456_34567 lazy fea dogpp"
pat=re.compile(r'[a-z]_[a-z]')  
for i in re.finditer(pat,s):
    print(i)


# In[18]:


s="The quick 11 broun fox 12 jumps_over fee 456_34567 lazy fea dogpp"
pat=re.compile(r'[0-9]_[0-9]')  
for i in re.finditer(pat,s):
    print(i)


# In[19]:


s="The quick 11 broun fox 12 jumps_over fee 456_34567 lazy fea dogpp"
pat=re.compile(r'[a-z0-9]_[a-z0-9]')  
for i in re.finditer(pat,s):
    print(i)


# In[25]:


s="The quick 11 broun 466-845-887 fox 12 456-123-867 jumps_over fee 999-345-867 lazy fea dogpp"
pat=re.compile(r'\d{3}-\d{3}-\d{3}')  
for i in re.finditer(pat,s):
    print(i)


# In[26]:


s="The quick 11 broun 466-845-887 fox 12 456-123-867 jumps_over fee 999-345-867 lazy fea dogpp"
pat=re.compile(r'\d{3}-\d{3}-\d{3}')  
print(re.findall(pat,s))
 


# In[ ]:


[^a-zA-Z0-9.] 
get_ipython().run_line_magic('psearch', 'ab*')
ab+?
ab{3}
^[a-z]+_[a-z]+$
^[a-zA-Z0-9_]*
([0-9]{1,3})
(\d{4})-(\d{1,2})-(\d{1,2})


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




