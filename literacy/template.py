
# coding: utf-8

# In[1]:


from importlib import machinery


# In[2]:


try:
    from .literate import LiterateTransformer, extension, exporter
except:
    from literate import LiterateTransformer, extension, exporter
import sys


# In[3]:


class TemplateTransformer(LiterateTransformer):
    def weave(self, code):
        return exporter.environment.from_string(code).render(
            getattr(self.shell, 'user_ns', dict))


# In[4]:


load_ipython_extension = extension(TemplateTransformer.instance())


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python template.ipynb')

