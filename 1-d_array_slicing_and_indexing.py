#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy


# In[2]:


x = numpy.arange(1,21)


# In[3]:


print(x)


# In[6]:


x[6] # prints 6th index element of list


# In[7]:


x[-1] #prints last integer of the list


# In[9]:


x[13] # prints 13th index integer


# In[10]:


x[:10] # prints list till 9th index


# In[11]:


x[10:] # prints list starting from 10th index upto last


# In[13]:


x[2:5] # prints list from 2nd index to 4th


# In[14]:


y = x[1:10] = 69 # assigns value 69 to all numbers in list from 1st index to 9th index


# In[15]:


print(y)


# In[16]:


print(x)


# In[17]:


z = x.copy() # make a copy of list


# In[18]:


print(z)


# In[ ]:




