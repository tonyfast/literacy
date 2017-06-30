
# coding: utf-8

# In[2]:


__import__('importable').load_ipython_extension()
try:
    from template import unload_ipython_extension, load_ipython_extension
    import finder
except:
    from .template import unload_ipython_extension, load_ipython_extension
    from . import preprocessors
    from . import repl
    from . import markdown
    from . import template
    from . import finder
finder.load_ipython_extension()


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python __init__.ipynb')

