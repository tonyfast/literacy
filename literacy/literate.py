
# coding: utf-8

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
from toolz.curried import compose, do, identity as identity_, merge, second, partial, drop
from mimetypes import MimeTypes; mimetypes = MimeTypes()

import textwrap 


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


exporter = PythonExporter()





class Code(Renderer):
    """A mistune.Renderer to accumulate lines of code in a Markdown document."""
    code = """"""
    inline_code = True
    inline_indent = True
    
    def block_code(self, code, lang=None):
        self.code += code + '\n'
        return super(Code, self).block_code(code, lang)

    def codespan(self, code):
        if self.inline_code:
            if self.inline_indent:
                self.code += textwrap.indent(code, ' '*self._indent(code)) + '\n'
            else:
                self.code += code + '\n'
        return super(Code, self).codespan(code)
    
    @staticmethod
    def _indent(code):
        """Determine the indent length of the last line."""
        if str:  return len(str[-1])-len(str[-1].lstrip())
        return 0


class Tangle(Markdown):
    """A mistune.Markdown processor for literate programming."""
    def render(self, text, **kwargs):
        code = self.renderer.code = """"""
        super(Tangle, self).render(text, **kwargs)
        if self.renderer.code.lstrip().startswith('---'): 
            return self.renderer.code
        code = exporter.from_notebook_node(
            new_notebook(cells=[new_code_cell(self.renderer.code)]))[0]
        return self.renderer.code

    __call__ = render

literate = Tangle(renderer=Code(), escape=False)


identity = identity_(lambda x: x)


class Transformer(UserList, InputTransformer):
    """weave --> macro --> tangle"""
    push = UserList.append
    
    tangle = staticmethod(identity)
    macro = staticmethod(identity)
    weave = staticmethod(identity)
    
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
            
    def reset(self, display=True, *, ns=None):
        body = self.weave('\n'.join(self))
        display and self.display(body)
        self.data = []
        return (
            body.lstrip().startswith('---') and identity or filters.ipython2python
        )(self.tangle(body, ns=ns or self.shell.user_ns))
    
    def parse(self, display, line="""""", body=None, *, ns=None):
        self.data = line and [line] or [] + (body or """""").splitlines()
        return self.reset(display, ns=ns)
    
    __call__ = partialmethod(parse, False)
    def run_code(self, line="""""", body=None):
        self.shell.run_code(self.parse(True, line, body))


def literate_yaml(source, ns={}):
    import yaml
    if source.lstrip().startswith('---'):
        [ns.update(stream) for stream in yaml.safe_load_all(textwrap.dedent(source))]
        return """"""
    return literate(source)


class Literate(Transformer):
    tangle = staticmethod(literate_yaml)
    macro = staticmethod(macro)


class Importer(SourceFileLoader):
    """"""
    tranformer = None            
    
    def create_module(self, spec): 
        return ModuleType(self.name)
    
    def exec_module(self, module):
        nb = reads(Path(self.path).read_text(), 4)
        for cell in nb.cells:
            if cell['cell_type'] == 'code':
                try:
                    source = self.tangle(cell.source, ns=module.__dict__)
                    exec(source, module.__dict__)
                except:
                    raise Exception('in ```\n{}```'.format(cell.source))
        return module

    def find_spec(self, name, paths, target=None):
        loader =  self.find_module(name, paths, target)
        return loader and importlib.util.spec_from_loader(name, loader)

    def find_module(self, name, paths, target=None):
        for path in paths or [Path()]:
            path = (path/Path(name.split('.')[-1])).with_suffix('.ipynb')
            if path.exists(): 
                return Importer(name, str(path))
        return None


def extension(transformer):
    def load_ipython_extension(ip=get_ipython()):
        nonlocal transformer
        transformer = transformer.instance()
        Importer.tangle = staticmethod(transformer)
        transformer.register_transforms(), transformer.register_magic()
        sys.meta_path.append(Importer(None, None)), sys.path_importer_cache.clear()
    return load_ipython_extension

load_ipython_extension = extension(Literate)
    
def unload_ipython_extension(ip=get_ipython()):
    sys.meta_path = list(filter(
        lambda x: not isinstance(x, Importer), sys.meta_path))


if __name__ == '__main__':
    load_ipython_extension()
    get_ipython().system('jupyter nbconvert --to python --TemplateExporter.exclude_input_prompt=True literate.ipynb')

