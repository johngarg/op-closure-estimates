#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from limits import derive_general_limits, derive_best_general_limits, derive_loop_limits, LAMBDA, print_general_limits


# In[2]:


decay_rates = []
best_limits = derive_best_general_limits(decay_rates=decay_rates)

for decay_rate in decay_rates:
    decay_rate["process"] = "$" + decay_rate["process"] + "$"
    
# fieldstring_limits = derive_loop_limits(general_limits=best_limits)


# In[3]:


# 26/09/2023
print_general_limits(best_limits=best_limits)


# In[ ]:




