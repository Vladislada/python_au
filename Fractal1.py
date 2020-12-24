#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as tl
r = tl.Turtle()
r.left(90)
r.penup()
r.backward(100)
r.pendown()
r.speed(100)

def draw(m):
    if m < 5:
        return
    else:
        r.forward(m)
        r.left(60)
        draw(3*m/4)
        r.right(120)
        draw(3*m/4)
        r.left(60)
        r.backward(m)
draw(100)


# In[ ]:





# In[ ]:




