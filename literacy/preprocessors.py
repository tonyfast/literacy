# coding: utf-8

# In[4]:

try:
    from markdown import renderer
except:
    from .markdown import renderer

# In[5]:

from nbformat import NotebookNode
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from nbconvert.filters import comment_lines
from nbconvert.preprocessors import Preprocessor
from functools import partial, wraps
from traitlets import Any, Unicode
from inspect import getfullargspec
__all__ = ['Explode', 'Dedent']

# In[6]:


def preprocessor(function, base=Preprocessor):
    """A decorator to create nbconvert preprocessors."""
    args = getfullargspec(function).args
    if not args[0] == 'self':
        raise ValueError('Preprocessor must define `self`.')
    return (type(function.__name__, (base, ), {
        'preprocess' + {
            4: '_cell',
            3: ''
        }[len(args)]: function,
    }))


# In[7]:


@preprocessor
def NumberCell(self, cell, resources, index):
    return cell['metadata'].update({'index': index}) or cell, resources


# In[8]:


@preprocessor
def Explode(self, nb, resources):
    cells = []
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            new = renderer.render(cell, cell['metadata'])
            cells.extend(new['cells'])
        else:
            cells.append(cell)
    return nb.update(cells=cells) or nb, resources


# In[9]:


@preprocessor
def SplitSourceCell(self, cell, resources, index):
    if isinstance(cell['source'], str):
        cell['source'] = cell['source'].splitlines()
    return cell, resources


# In[10]:


@preprocessor
def JoinSource(self, cell, resources, index):
    if not isinstance(cell['source'], str):
        cell['source'] = '\n'.join(cell['source'])
    return cell, resources


# In[11]:


def dedent(lines):
    dedent, out = 0, []
    if isinstance(lines, str):
        lines = lines.splitlines()

    if any(map(str.strip, lines)):
        dedent = next(filter(str.strip, lines))
        dedent = len(dedent) - len(dedent.lstrip())

    return '\n'.join(map(lambda x: x[dedent:], lines))


# In[12]:


@preprocessor
def Dedent(self, cell, resources, i):
    return cell.update(source=dedent(cell['source'])) or cell, resources


# In[ ]:

if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python preprocessors.ipynb')
    get_ipython().system('yapf -i preprocessors.py')

# In[ ]:
