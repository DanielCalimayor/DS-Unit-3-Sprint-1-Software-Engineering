#!/usr/bin/env python
# coding: utf-8

# In[2]:


from random import randint


class Product:
   
    def __init__(self, name, price=10, weight=20,
                 flammability=.5, identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def sab(self):
        steal_ratio = self.price / self.weight
        if steal_ratio < .5:
            return 'not so stealable...'
        elif steal_ratio < 1:
            return 'a little stealable.'
        else:
            return 'very stealable!'

    def explode(self):
        volatility = self.flammability * self.weight
        if volatility < 10:
            return 'small explosion'
        elif volatility < 50:
            return 'big explosive'
        else:
            return 'Nuke explosive'
        
    def punch(self):
        if self.weight < 5:
            return 'No pain'
        elif self.weight < 15:
            return 'Minamal pain'
        else:
            return 'PAIN'


# In[ ]:




