
# coding: utf-8

# In[1]:


try: 
    from markdown import renderer
except:
    from .markdown import renderer


# In[2]:


from nbformat import NotebookNode
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from nbconvert.filters import comment_lines
from nbconvert.preprocessors import Preprocessor
from traitlets import Any, Unicode
__all__ = ['Explode', 'Dedent']


# In[3]:


class NumberCell(Preprocessor):
    key = Unicode(default_value="_")
    def preprocess_cell(self, cell, resources, index):
        return cell['metadata'].update({self.key:index}) or cell, resources


# In[4]:


class Explode(NumberCell):
    def preprocess(self, nb, resources):
        cells = []
        for cell in super().preprocess(nb, resources)[0]['cells']:
            if cell['cell_type']=='code':
                new = renderer.render(cell, cell['metadata'])
                cells.extend(new['cells'])
            else:
                cells.append(cell)
        return nb.update(cells=cells) or nb, resources


# In[5]:


class SplitSource(Preprocessor):
    def preprocess_cell(self, cell, resources, index):
        if isinstance(cell['source'], str):
            cell['source'] = cell['source'].splitlines()
        return cell, resources


# In[6]:


class JoinSource(Preprocessor):
    def preprocess_cell(self, cell, resources, index):
        if not isinstance(cell['source'], str):
            cell['source'] = '\n'.join(cell['source'])
        return cell, resources


# In[7]:


def dedent(lines):
    dedent, out = 0, []
    if isinstance(lines, str):
        lines = lines.splitlines()
        
    if any(map(str.strip, lines)):
        dedent = next(filter(str.strip, lines))
        dedent = len(dedent) - len(dedent.lstrip())
    
    return '\n'.join(map(lambda x: x[dedent:], lines))


# In[8]:


class Dedent(Preprocessor):
    def preprocess_cell(self, cell, resources, i):
        return cell.update(source=dedent(cell['source'])) or cell, resources


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python preprocessors.ipynb')


# In[ ]:




