#!/usr/bin/env python
# coding: utf-8

# In[1]:


range(10)


# In[4]:


for i in range(10):
    print(i)


# In[6]:


def test_fib(n):
    a,b =0,1
    for i in range(n):  
        yield a         #yield is a keyword which is used for making generator function
        a,b = b,a+b


# In[8]:


test_fib(10)


# In[10]:


for i in test_fib(10):
    print(i)


# write fibonacci series?

# In[24]:


def fib(x):
    a,b = 0,1
    for i in range(x):
        
        yield a 
        
        a,b = b, a + b 
        
    return fib


# In[25]:


fib(10)


# In[26]:


for i in fib(10):
    print(i)


# In[29]:


x  = "Lucky"
for i in x:
    print(i)


# In[32]:


next(x)


# what is iterator ?

# In[33]:


L = iter(x) #it will work only in string


# In[34]:


next(L)


# In[35]:


next(L)


# In[36]:


next(L)


# In[37]:


next(L)


# In[38]:


next(L)


# In[39]:


next(L)


# In[ ]:




