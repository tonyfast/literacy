
# coding: utf-8

# In[4]:


try:
    from literacy import run_cell, load_ipython_extension, unload_ipython_extension
except:
    from .literacy import run_cell, load_ipython_extension, unload_ipython_extension
from nbconvert.exporters.templateexporter import TemplateExporter
exporter, _load = TemplateExporter(), load_ipython_extension


# In[5]:


def run_template_cell(self, text: str, store_history=True, silent=True, shell_futures=True):
    """Render a cell body as jinja template before running the code."""
    return run_cell(
        self, exporter.environment.from_string(text).render(**self.user_ns), store_history, silent, shell_futures)


# In[6]:


def load_ipython_extension(ip=__import__('IPython').get_ipython()):
    _load(ip, run_template_cell)


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python template.ipynb')


# In[ ]:




