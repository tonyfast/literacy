
# coding: utf-8

from typing import Tuple, Callable
from types import ModuleType
from importlib.machinery import SourceFileLoader, ModuleSpec
from pathlib import Path
import sys, textwrap, warnings, mistune
PY2 = sys.version_info.major is 2
from collections import UserList
from importlib.util import spec_from_loader
from IPython.core.inputtransformer import InputTransformer
from fnmatch import fnmatch
from functools import partial, partialmethod
from IPython import get_ipython, display
from IPython.core.interactiveshell import InteractiveShell
from nbconvert import filters
from nbformat import reads, v4, NotebookNode
from toolz.curried import identity as identity_, partial
from mimetypes import MimeTypes; mimetypes = MimeTypes()
from nbconvert.exporters.templateexporter import TemplateExporter
import argparse

exporter = TemplateExporter()
HR = '---'


def identity(*args, **kwargs): return args[0]


def macro(code: str)-> Tuple[display.DisplayObject]:
    """
    >>> url = "https://test.com"
    >>> assert macro(url) and macro(''' {}
    ...
    ... '''.format(url))[0].data.strip() == url
    """
    lines = code.splitlines()
    if lines and lines[0].strip():
        if len(lines) is 1 and lines[0][:1].strip():
            type = mimetypes.guess_type(code)[0]
            is_image = type and type.startswith('image')
            disp = partial(display.Image, embed=True) if is_image else display.Markdown
            if fnmatch(code, "* [[]*[]](*)*"):
                url = code.rsplit(')', 1)[0].rsplit('(',1)[1].split(' ', 1)[0]
                if url and url != '#':
                    return (display.Markdown(data=code), *macro(url))
            if fnmatch(code, 'http*://*'):
                return is_image and display.Image(url=code) or display.IFrame(code, width=600, height=400),
        return display.Markdown(data=code), 
    return tuple()


parser = argparse.ArgumentParser(prog='literate')
parser.add_argument('-i', '--inline', action='store_true', help='Tangle inline code codespans.')
parser.add_argument('-b', '--block', action='store_true', help='Tangle code blocks.')

class Code(mistune.Renderer):
    """A mistune.Renderer to accumulate lines of code in a Markdown document.
    
    the parser configures inline and block modes.
    """
    code = """"""
    block = True
    inline = True
    
    def block_code(self, code: str, lang: str="")->str:
        if self.block:
            if not lang:
                self.code += code + '\n'
            if lang and lang.startswith('%%'):
                self.code = lang + '\n' + code
        return super(Code, self).block_code(code, lang)

    def codespan(self, code: str) -> str:
        if self.inline:
            self.code += textwrap.indent(code, ' '*self._indent(code)) + '\n'
        return super(Code, self).codespan(code)
    
    @staticmethod
    def _indent(code:str)->int:
        """Determine the indent length of the last line."""
        return code and len(code[-1])-len(code[-1].lstrip()) or 0


class Tangle(mistune.Markdown):
    """A mistune.Markdown processor for literate programming."""
    def render(self, text: str, **kwargs)->str:
        self.renderer.code = """"""
        super(Tangle, self).render(text, **kwargs)
        return textwrap.dedent(self.renderer.code)

    __call__ = render

literate = Tangle(renderer=Code(), escape=False)


class Transformer(UserList, InputTransformer):
    """weave --> macro --> tangle"""
    push = UserList.append
    env = exporter.environment
    template = True
    
    tangle = staticmethod(identity)
    
    def register_transforms(self):
        self.shell.input_transformer_manager.logical_line_transforms = []
        self.shell.input_transformer_manager.physical_line_transforms = []
        self.shell.input_transformer_manager.python_line_transforms = [self]

    def register_magic(self):
        self.shell.register_magic_function(self.run_code, 'line_cell', self.name)
        
    @classmethod
    def instance(cls, *args, **kwargs):
        self = cls(*args, **kwargs)
        self.shell  = get_ipython() or InteractiveShell.instance()
        return self

    @property
    def name(self):
        return type(self).__name__.replace('Transformer', '').lower()

    
    # How do you type auxilary display objects?
    def weave(self, body:str, *, ns:dict=dict(), disp:bool=True)->str:
        if isinstance(body, self.env.template_class):
            body = body.render(**ns)
        # display the thing
        disp and display.display(*macro(body))
        return body
    
    def reset(self, disp:bool=True, *, ns:dict=dict())->str:
        """This function must complete or IPython hangs."""
        template = source = '\n'.join(self)
        ns = ns or self.shell.user_ns
        if self and self.template:
            try:
                template = self.env.from_string(source) 
                source = self.weave(template, ns=ns, disp=disp)
            except Exception as e:
                warnings.warn("""Unable to compile the source template.""")
        self.data = []
        try:
            source = self.tangle(source, ns=ns)
        except:
            warnings.warn("""Unable to extract the source.""")
        return source
    
    def run_code(self, line:str="""""", body:str=None):
        self.shell.run_code(self.parse(True, line, body))
        
    def parse(self, disp:bool, line:str="""""", body:str=None, *, ns:dict=dict())->str:
        if line.startswith('-'):
            for key, value in vars(parser.parse_args(line.split())).items(): 
                setattr(Code, key, value)
            line = None
        self.data = line and [line] or []
        self.data += (body or """""").splitlines()
        return self.reset(disp, ns=ns)
    
    __call__ = partialmethod(parse, False)
    
    __repr__ = InputTransformer.__repr__


def literate_yaml(source:str, ns={})->str:
    """"""
    import yaml
    source = literate(source)
    if source.lstrip().startswith(HR):
        for stream in yaml.safe_load_all(source):
            if not isinstance(stream, dict): 
                raise SyntaxError("""Each yaml stream must be a dictionary.""")
            ns.update(stream)
        source = """"""
    return filters.ipython2python(source)


def load_markdown(source:str)->NotebookNode:
    """Convert markdown to a notebook by separately cells with dividers.
    >>> nb = load_markdown('''print(10)\\n---\\nprint(20)''')
    >>> assert len(nb.cells) is 2
    >>> nb.cells # doctest: +SKIP
    """
    nb = v4.new_notebook(cells=[v4.new_code_cell("""""")])
    for line in source.splitlines():
        if line.startswith(HR):
            nb.cells.append(v4.new_code_cell(""""""))
        nb.cells[-1].source += line + '\n'
    return nb


class Markdown(Transformer):
    """
    >>> md = Markdown.instance()
    >>> code = md('''# Test''')
    >>> assert not code.strip()
    >>> md('''    print(10)''')
    'print(10)\\n'
    """
    tangle = staticmethod(literate_yaml)


class Importer(SourceFileLoader):
    """
    Import this module itself 
    >>> i = Importer('literate', 'literate.ipynb')
    >>> i.transformer = Markdown()
    >>> module = i.exec_module(i.create_module(i.find_spec('literate')))
    >>> assert hasattr(module, 'Importer')
    """
    def create_module(self, spec:str)->ModuleType:  return ModuleType(self.name)
    
    def exec_module(self, module:ModuleType)->ModuleType:
        """Exceute each cell in the module attaching everything to the module.
        """
        path = Path(self.path)
        source = path.read_text()
        nb = (
            load_markdown(source)
            if path.suffix in ('.markdown', '.md') 
            else reads(source, 4))
        for cell in nb.cells:
            try:
                if cell['cell_type'] == 'code': exec(
                    self.transformer(cell.source, ns=module.__dict__), module.__dict__)
            except: 
                raise ImportError(cell.source)
        return module

    def find_spec(self, name:str, paths:list=None, target=None)->ModuleSpec:
        loader =  self.find_module(name, paths, target)
        return loader and spec_from_loader(name, loader)
    
def find_module(self, name:str, paths:list=None, target=None)->Importer:
    for ext in ['.ipynb', '.md', '.markdown']:
        for path in paths or [Path()]:
            path = (path/Path(name.split('.')[-1])).with_suffix(ext)
            if path.exists(): return Importer(name, str(path))
    return None

Importer.find_module = find_module


def extension(transformer:Transformer)->Callable:
    """
    >>> import sys
    >>> extension(Markdown)() # load the extension
    >>> assert isinstance(sys.meta_path[-1], Importer)
    """
    def load_ipython_extension(ip:InteractiveShell=get_ipython()):
        nonlocal transformer
        transformer = transformer.instance()
        Importer.transformer = staticmethod(transformer)
        transformer.register_transforms(), transformer.register_magic()
        sys.meta_path.append(Importer(None, None)), sys.path_importer_cache.clear()
    return load_ipython_extension

load_ipython_extension = extension(Markdown)
    
def unload_ipython_extension(ip:InteractiveShell=get_ipython()):
    """
    >>> import sys
    >>> extension(Markdown)() # load the extension
    >>> unload_ipython_extension()
    >>> assert not any(map(lambda x: isinstance(x, Importer), sys.meta_path))
    """        
    
    sys.meta_path = list(filter(
        lambda x: not isinstance(x, Importer), sys.meta_path))
    sys.path_importer_cache.clear()


if __name__ == '__main__':
    load_ipython_extension()
    print(__import__('doctest').testmod())
    get_ipython().system('jupyter nbconvert --to python --TemplateExporter.exclude_input_prompt=True literate.ipynb')

