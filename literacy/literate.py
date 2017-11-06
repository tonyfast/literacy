
# coding: utf-8

# In[1]:


from types import ModuleType
from importlib.machinery import SourceFileLoader, FileFinder
from pathlib import Path
from os.path import sep, curdir, extsep, exists
from nbformat import *
from operator import ne
import sys
PY2 = sys.version_info.major is 2
from inspect import *
from collections import UserList
from IPython.core.inputtransformer import InputTransformer
from fnmatch import fnmatch
from functools import partial, partialmethod
from IPython import get_ipython, display
from IPython.core.interactiveshell import InteractiveShell
from mistune import Markdown, Renderer
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
from nbconvert import export, get_exporter, filters, exporters
from nbconvert.exporters.python import PythonExporter    
from toolz.curried import compose, do, identity, merge, second, partial
from mimetypes import MimeTypes; mimetypes = MimeTypes()


# In[2]:


def macro(code):
    from IPython import display
    type = mimetypes.guess_type(code)[0]
    is_image = type and type.startswith('image')
    disp = (
        partial(display.Image, embed=True) 
        if is_image else display.Markdown)
    if fnmatch(code, '*[[]*[]](*)'):
        url = (
            code.lstrip('#').lstrip()
            .split(']', 1)[1].lstrip('(')
            .rstrip(')').split('"',1)[0].strip())
        if url and url != '#':
            return (display.Markdown(code), *macro(url))
    if fnmatch(code, 'http*://*'):
        if is_image: 
            return display.Image(url=code),
        return display.IFrame(code, width=600, height=400),
    try:
        if __import__('pathlib').Path(code).is_file(): 
            return disp(filename=code),
    except OSError: pass
    
    return tuple()


# In[3]:


exporter = PythonExporter()


# In[4]:


class Code(Renderer):
    """A mistune.Renderer to accumulate lines of code in a Markdown document."""
    code = """"""
    inline_code = True
    inline_indent = True
    
    def block_code(self, code, lang=None):
        self.code += code + '\n'
        return super(Code, self).block_code(code, lang)

    def codespan(self, code):
        """Weave inline code references"""
        if self.inline_code:
            if self.inline_indent:
                self.code += ' '*self.indents(self.code) + code + '\n'
            else:
                self.code += code + '\n'
        return super(Code, self).codespan(code)
    
    @staticmethod
    def indents(code):
        """Determine the indent length of the last line."""
        if code:
            str = list(filter(lambda s: s.strip(), code.splitlines()))
            if str:  
                return len(str[-1])-len(str[-1].lstrip())
        return 0


class Tangle(Markdown):
    """A mistune.Markdown processor for literate programming."""
    def render(self, text, **kwargs):
        self.renderer.code = """"""
        super(Tangle, self).render(text, **kwargs)
        code = exporter.from_notebook_node(
            new_notebook(cells=[new_code_cell(self.renderer.code)]))[0]
        return code

    __call__ = render

literate = Tangle(renderer=Code(), escape=False)


# In[5]:


Identity = identity(lambda x: x)


# In[6]:


class IdentityTransformer(UserList, InputTransformer):
    weave = staticmethod(Identity)
    tangle = staticmethod(Identity)
    macro = staticmethod(Identity)
    push = UserList.append
    
    def register_transforms(self):
        self.shell.input_transformer_manager.logical_line_transforms =         self.shell.input_transformer_manager.physical_line_transforms = []
        self.shell.input_transformer_manager.python_line_transforms = [self]

    def register_magic(self):
        self.shell.register_magic_function(self.run_code, 'cell', self.name)
        
    @classmethod
    def instance(cls, *args, **kwargs):
        self = cls(*args, **kwargs)
        self.shell  = get_ipython() or InteractiveShell.instance()
        return self

    @property
    def name(self):
        return type(self).__name__.replace('Transformer', '').lower()

    def display(self, body):
        if self and self[0].strip():
            display.display(display.Markdown(body))
        else:
            display.display(*self.macro(body))
            
    def reset(self, display=True):
        body = self.weave('\n'.join(self))
        display and self.display(body)
        self.data = []
        return filters.ipython2python(self.tangle(body))
    
    def run(self, display, line="""""", body=None):
        self.data = line and [line] or [] + (body or """""").splitlines()
        return self.reset(display)
    
    __call__ = partialmethod(run, False)
    def run_code(self, line="""""", body=None):
        self.shell.run_code(self.run(True, line, body))


# In[7]:


class LiterateTransformer(IdentityTransformer):
    tangle = staticmethod(literate)
    macro = staticmethod(macro)


# In[8]:


class Importer(SourceFileLoader):
    tangle = None            
    def create_module(self, spec):
        return ModuleType(self.name)
    
    def exec_module(self, module):
        nb = reads(Path(self.path).read_text(), 4)
        for cell in nb.cells:
            cell['cell_type'] == 'code' and exec(self.tangle(cell.source), vars(module))
        return module

    def find_spec(self, name, *args):
        spec = FileFinder(name, (Importer, ['.ipynb'])).find_spec(name)
        if not spec:
            path = Path(name).with_suffix('.ipynb')
            if path.exists():
                spec = importlib.util.spec_from_file_location(
                    name, str(path), loader=Importer(name, str(path)))
        return spec


# In[9]:


def extension(transformer):
    def load_ipython_extension(ip=get_ipython()):
        Importer.tangle = staticmethod(transformer)
        transformer.register_transforms(), transformer.register_magic()
        sys.meta_path.append(Importer(None, None)), sys.path_importer_cache.clear()
    return load_ipython_extension

load_ipython_extension = extension(LiterateTransformer.instance())
    
def unload_ipython_extension(ip=get_ipython()):
    sys.meta_path = list(filter(
        lambda x: not isinstance(x, Importer), sys.meta_path))


# In[10]:


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python literate.ipynb')

