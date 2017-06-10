
# coding: utf-8

# In[ ]:


__all__ = 'style',


# Extra style sheets go here.
# 
# These could be arguments to the magic.

# In[16]:


from IPython.display import display, HTML, Javascript


# In[17]:


__style_block__ = """
<style>
{css}
</style>
""".format
    
def style(css="", javascript=""):
    return display(
        HTML(__style_block__(**locals())), Javascript(javascript))


# In[ ]:


if __name__ == '__main__': 
    get_ipython().system('jupyter nbconvert --to script display.ipynb')


# In[ ]:




