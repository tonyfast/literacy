
# coding: utf-8

# In[4]:


__all__ = ['ip']
try:
    from repl import unload_ipython_extension, load_ipython_extension
except:
    from .repl import unload_ipython_extension, load_ipython_extension
from IPython import get_ipython
ip = get_ipython()


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python __init__.ipynb')


# In[ ]:




