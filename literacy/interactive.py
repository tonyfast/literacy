
# coding: utf-8

# In[7]:


try: 
    from repl import Literate, unload_ipython_extension
    from markdown import renderer
    from template import exporter
except:
    from .repl import Literate, unload_ipython_extension
    from .markdown import renderer
    from .template import exporter
    
from ipywidgets import HTML
from traitlets import Any, observe, Unicode
from IPython.display import display
from IPython import get_ipython
from ipywidgets.widgets.widget import Widget


# In[8]:


class Template(HTML):
    template = Any()
    markdown = Unicode()
    
    @observe('template')
    def render(self, change={}):
        self.markdown = self.template.render(**get_ipython().user_ns)
        self.value = renderer(self.markdown)
        return self


# In[9]:


class Interactive(Literate):
    def read(self, text):
        w = Template(template=exporter.environment.from_string(text))
        display(w)
        return w.markdown
    def print(self, *args):
        [w.render() for w in Widget.widgets.values() if isinstance(w, Template)]


# In[10]:


def load_ipython_extension(ip=__import__('IPython').get_ipython()):
    ip.run_cell = Interactive()


# In[11]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python interactive.ipynb')


# In[ ]:





# In[ ]:




