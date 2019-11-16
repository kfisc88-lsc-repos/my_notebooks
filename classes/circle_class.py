#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Circle():
    
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14
    
    def __init__(self, radius=1):
        
        # ATTRIBUTES
        self.radius = radius
        self.area = radius*radius*Circle.pi
        
    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2


# In[15]:


my_circle = Circle(25)


# In[16]:


my_circle.pi


# In[17]:


my_circle.radius


# In[18]:


my_circle.get_circumference()

