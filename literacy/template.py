
# coding: utf-8

# In[1]:


try: 
    from repl import Literate, unload_ipython_extension
except:
    from .repl import Literate, unload_ipython_extension


# In[2]:


from nbconvert.exporters.base import export, get_exporter
exporter = get_exporter('python')(config={})        


# In[9]:


class Template(Literate):
    def read(self, text):
        return super().read(
        exporter.environment.from_string(text).render(**self.kernel.user_ns))


# In[10]:


def load_ipython_extension(ip=__import__('IPython').get_ipython()):
    ip.run_cell = Template()


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python template.ipynb')


# In[ ]:




