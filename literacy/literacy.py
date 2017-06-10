
# coding: utf-8

# In[8]:


__all__ = 'load_ipython_extension', 'unload_ipython_extension'


# ### create a `mistune` renderer that captures code cells.

# In[16]:


try:
    from display import style
except:
    from .display import style


# In[9]:


from mistune import Markdown, Renderer
from nbconvert.filters import ipython2python


# In[10]:


class Literate(Renderer):
    source = [] 
    def block_code(self, code, language=None):
        # Strip leading indent
        lines = code.split('\n')
        tab = len(lines[0]) - len(lines[0].lstrip())
        return self.source.append((
                ipython2python('\n'.join([line[tab:] for line in lines])), True
        )) or code

    def codespan(self, code):
        """Do not record codespan histories"""
        return self.source.append((ipython2python(code), False)) or code


# In[11]:


class Codify(Markdown):
    def render(self, text):
        self.renderer.source = []
        super().render(text)
        return self.renderer.source
renderer = Codify(renderer=Literate())


# ### IPython
# 
# A replacement `run_cell` function for Ipython

# In[12]:


from IPython.display import display, Markdown as MarkDisplay
from IPython.core.interactiveshell import InteractiveShell

def run_cell(self, raw_cell, store_history=True, silent=True, shell_futures=True):
    display(MarkDisplay(raw_cell + """\n\n---\n"""))
    for source, history in renderer.render(raw_cell) or [("""""", False)]:
        executed = InteractiveShell.run_cell(self, source, history, silent, shell_futures)
    return executed


# ### Magics
# 
# Use `%load literate` to activate literate programming; `%unload literate` reverses this behavior.

# In[13]:


from types import MethodType
from IPython import get_ipython
def load_ipython_extension(ip=get_ipython()):
    ip.run_cell = MethodType(run_cell, ip)
    style(__style_block__)
    
def unload_ipython_extension(ip=get_ipython()):
    ip.run_cell = MethodType(InteractiveShell.run_cell, ip)


# In[17]:


if __name__ == '__main__': 
    get_ipython().system('jupyter nbconvert --to script literacy.ipynb')


# In[18]:


__style_block__ = """
.output_subarea.output_markdown.rendered_html {
    flex: .9;
    padding-left: 0px;
}
.output_subarea {
    flex: .9;
    padding-left: 10%;
}"""

