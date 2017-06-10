
# coding: utf-8

# In[1]:


__all__ = 'c',


# In[2]:


try:
    from literacy import renderer
except:
    from .literacy import renderer
    
from nbconvert.preprocessors.base import Preprocessor
from nbconvert.exporters.python import PythonExporter
from nbformat.v4 import new_code_cell, new_markdown_cell

if 'c' not in locals():
    c = __import__('traitlets').config.Config()


# In[3]:


class LiteracyPreprocessor(Preprocessor):
    def preprocess(self, nb, resources):
        cells = []
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                source = cell['source']
                renderer.render(source)
                cells.append(new_markdown_cell(source))
                cells.append(new_code_cell(**cell))
                cells[-1].update(
                    source='\n'.join([s[0] for s in renderer.renderer.source]),
                    outputs=cells[-1].outputs[1:])
            else:
                cells.append(cell)
            
        return nb.update(cells=cells) or nb, resources
    
c.Exporter.preprocessors = [LiteracyPreprocessor]


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python config.ipynb')


# In[ ]:




