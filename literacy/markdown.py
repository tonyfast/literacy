
# coding: utf-8

# In[1]:


from nbformat.v4 import new_markdown_cell, new_code_cell, new_notebook, new_output, nbformat_schema
from nbformat import NotebookNode
from mistune import Markdown, Renderer, preprocessing
__all__ = []


# In[2]:


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


# In[6]:


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
        return new_notebook(cells=body and cells.append(new_markdown_cell(body)) or cells)

class CodeCell(Renderer):
    def block_code(self, code: str, lang='') -> str:
        return self.blocks.append((code, lang or '', 'block_code')) or super().block_code(code, lang)

    def codespan(self, code: str, lang='') -> str:
        return self.blocks.append((code, lang, 'codespan')) or super().codespan(code)

CodeCell.blocks = []

renderer = Notebook(renderer=CodeCell(), parse_block_html=False)


# In[ ]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python markdown.ipynb')


# In[ ]:




