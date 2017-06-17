
# coding: utf-8

# In[22]:


try: 
    from literacy import renderer, dedent
except:
    from .literacy import renderer, dedent


# In[23]:


from nbformat import NotebookNode
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from nbconvert.filters import comment_lines
from nbconvert.preprocessors import Preprocessor
from traitlets import Any, Unicode


# In[24]:


class SplitSource(Preprocessor):
    def preprocess_cell(self, cell, resources, index):
        if isinstance(cell['source'], str):
            cell['source'] = cell['source'].splitlines()
        return cell, resources


# In[25]:


class JoinSource(Preprocessor):
    def preprocess_cell(self, cell, resources, index):
        if not isinstance(cell['source'], str):
            cell['source'] = '\n'.join(cell['source'])
        return cell, resources


# In[26]:


class SingleCell(Preprocessor):
    new_cell = Any(default_value=new_markdown_cell)
    def preprocess(self, nb, resources):
        new_cell = self.new_cell()
        for cell in nb.cells:
            new_cell['source'] += '\n'+self.preprocess_cell(cell, resources, None)[0]['source']
        return new_notebook(cells=[new_cell]), resources

class SingleCode(SingleCell):
    new_cell = Any(default_value=new_code_cell)
    def preprocess_cell(self, cell, resources, index):
        if cell['cell_type'] != 'code':
            cell['source'] = comment_lines(cell['source'])
        return cell, resources
    # Attach outputs later
    
class SingleMarkdown(SingleCell):
    new_cell = Any(default_value=new_markdown_cell)


# In[27]:


class NumberCell(Preprocessor):
    key = Unicode(default_value="_")
    def preprocess_cell(self, cell, resources, index):
        return cell['metadata'].update({self.key:index}) or cell, resources


# In[28]:


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


# In[29]:


class Dedent(Preprocessor):
    def preprocess_cell(self, cell, resources, i):
        return cell.update(source=dedent(cell['source'])) or cell, resources


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python preprocessors.ipynb')


# In[ ]:




