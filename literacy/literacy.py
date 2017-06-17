
# coding: utf-8

# In[1]:


from nbformat.v4 import new_markdown_cell, new_code_cell, new_notebook, new_output, nbformat_schema
    
from nbconvert.filters import comment_lines
from nbformat import NotebookNode
from mistune import Markdown, Renderer, preprocessing
from IPython.core.interactiveshell import InteractiveShell, ExecutionResult
from types import MethodType
__all__ = 'load_ipython_extension', 'unload_ipython_extension'


# In[2]:


def dedent(lines):
    dedent, out = 0, []
    if isinstance(lines, str):
        lines = lines.splitlines()
        
    if any(map(str.strip, lines)):
        dedent = next(filter(str.strip, lines))
        dedent = len(dedent) - len(dedent.lstrip())
    
    return '\n'.join(map(lambda x: x[dedent:], lines))


# In[3]:


def execute(nb, store_history=False, silent=False, shell_futures=True):
    ip = __import__('IPython').get_ipython()
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            code = cell['source']
            InteractiveShell.run_cell(ip, code, store_history, silent, shell_futures)
    return ExecutionResult()


# In[4]:


def codespan(text, code: str, lang="""""", markdown="""""", SEP='`'):
    return (*text.split(SEP, 2), SEP)

def block_code(text, code: str, lang: str, block="""""", markdown="""""", SEP='```'):
    for line in filter(bool, code.splitlines()):
        leading, text = text.split(line, 1)
        if not block:
            if SEP in leading:
                markdown, leading = leading.split(SEP+lang, 1)
            else:
                (*markdown, leading), SEP = leading.splitlines(), ""
        block += leading + line
    return markdown, block, text, SEP

blocks = {'codespan': codespan, 'block_code': block_code}


# In[5]:


class Notebook(Markdown):
    def render(self, body, metadata={}, outputs=[]):
        if isinstance(body, NotebookNode):
            outputs, body = body.get('outputs'), body.get('source')
        body, cells, self.renderer.blocks = preprocessing(body), [], []
        for code, lang, type in super().render(body) and self.renderer.blocks:
            markdown, block, body, SEP = blocks[type](body, code, lang)
            '\n'.join(markdown).strip() and cells.append(new_markdown_cell(markdown, metadata=metadata))
            if block.strip():
                cells.append(new_code_cell(block, metadata=metadata))
                cells[-1]['metadata'].update({'lang': lang, 'sep': SEP})
            else:
                cells.append(new_markdown_cell(block))
        return new_notebook(
            cells=body and cells.append(new_markdown_cell(body)) or cells
        )

class CodeCell(Renderer):
    def block_code(self, code: str, lang='') -> str:
        return self.blocks.append((code, lang or '', 'block_code')) or super().block_code(code, lang)

    def codespan(self, code: str, lang='') -> str:
        return self.blocks.append((code, lang, 'codespan')) or super().codespan(code)

CodeCell.blocks, renderer = [], Notebook(renderer=CodeCell(), parse_block_html=False)


# In[6]:


def run_cell(self, text: str, store_history=True, silent=True, shell_futures=True) -> ExecutionResult:
    from IPython.display import display, Markdown
    return display(Markdown(text)) or execute(
        renderer.render(text), store_history, silent, shell_futures)


# In[7]:


def load_ipython_extension(ip=__import__('IPython').get_ipython(), runner=run_cell):
    ip.run_cell = MethodType(runner, ip)

def unload_ipython_extension(ip=__import__('IPython').get_ipython()):
    load_ipython_extension(ip, InteractiveShell.run_cell)


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python literacy.ipynb')


# In[ ]:





# In[ ]:




