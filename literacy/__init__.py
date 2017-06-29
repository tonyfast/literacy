
# coding: utf-8

# In[10]:


import importable
try:
    from template import unload_ipython_extension, load_ipython_extension
    import preprocessors
except:
    from .template import unload_ipython_extension, load_ipython_extension
    from . import preprocessors
    from . import repl
    from . import markdown
    from . import template
    
importable.exporter.config['Exporter'].update(
    preprocessors=[preprocessors.JoinSource, preprocessors.Explode]
)


# In[9]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python __init__.ipynb')

