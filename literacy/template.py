
# coding: utf-8

# In[1]:


try: 
    from repl import Literate, unload_ipython_extension, repl
except:
    from .repl import Literate, unload_ipython_extension, repl


# In[2]:


from nbconvert.exporters.base import export, get_exporter
exporter = get_exporter('python')(config={})        


# In[3]:


class Template(Literate):
    def read(self, text):
        return super().read(
        exporter.environment.from_string(text).render(**self.kernel.user_ns))


# In[4]:


load_ipython_extension = repl(Template)


# In[5]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python template.ipynb')


# In[ ]:




