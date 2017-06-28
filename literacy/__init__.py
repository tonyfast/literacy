
# coding: utf-8

# In[1]:


try:
    from template import unload_ipython_extension, load_ipython_extension
except:
    from .template import unload_ipython_extension, load_ipython_extension


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python __init__.ipynb')


# In[ ]:




