#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tensorflow


# In[3]:


import tensorflow as tf


# In[5]:


a = 12
b = 10


# In[23]:


c = tf.add(a,b,name='Add')
d = tf.multiply(a,b,name ='Multiply')
e = tf.truediv(a,b,name = 'Division')


# In[24]:


c


# In[25]:


d


# In[26]:


e

