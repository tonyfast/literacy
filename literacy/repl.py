
# coding: utf-8

# In[1]:


try: 
    from preprocessors import Explode
except:
    from .preprocessors import Explode
from IPython.display import display, Markdown

from nbformat import NotebookNode
from nbformat.v4 import new_code_cell, new_notebook
from types import MethodType

from IPython import get_ipython
from IPython.core.interactiveshell import InteractiveShell, ExecutionResult
__all__ = []


# In[2]:


class Repl:
    kernel = get_ipython()
    def read(self, text):
        return text
    
    def eval(self, text):
        return new_notebook(cells=[new_code_cell(source=text)])            

    def print(*args, **kwargs): ...

    def __call__(self, content, *args, **kwargs):
        if not isinstance(content, NotebookNode):
            content = self.read(content)
        node = self.eval(content)
        result = self.loop(node, *args, **kwargs)
        return self.print(node) or result


# In[3]:


class RunCell(Repl):                
    def loop(self, node, store_history=False, silent=False, shell_futures=True):
        last = ExecutionResult()
        for cell in node['cells']:
            if cell['cell_type'] == 'code':
                last = InteractiveShell.run_cell(self.kernel, cell['source'], store_history=store_history, silent=silent, shell_futures=shell_futures)
        return last


# In[4]:


class Literate(RunCell):
    def read(self, text):
        display(Markdown(text))
        return text
    def eval(self, text):
        nb = super(Literate, self).eval(text)
        nb = Explode().preprocess(nb, {})[0]
        return nb


# In[5]:


def load_ipython_extension(ip=__import__('IPython').get_ipython()):
    ip.run_cell = Literate()

def unload_ipython_extension(ip=__import__('IPython').get_ipython()):
    ip.run_cell = MethodType(InteractiveShell.run_cell, ip)


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python repl.ipynb')


# In[ ]:




