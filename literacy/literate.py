
# coding: utf-8

from types import ModuleType
from importlib.machinery import SourceFileLoader
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
from nbformat import reads
from toolz.curried import identity as identity_, partial
from mimetypes import MimeTypes; mimetypes = MimeTypes()


identity = identity_(lambda x: x)


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


class Code(mistune.Renderer):
    """A mistune.Renderer to accumulate lines of code in a Markdown document."""
    code = """"""
    
    def block_code(self, code, lang=""):
        if not lang:
            self.code += code + '\n'
        if lang and lang.startswith('%%'):
            self.code = lang + '\n' + code
        return super(Code, self).block_code(code, lang)

    def codespan(self, code):
        self.code += textwrap.indent(code, ' '*self._indent(code)) + '\n'
        return super(Code, self).codespan(code)
    
    @staticmethod
    def _indent(code):
        """Determine the indent length of the last line."""
        if code:  return len(code[-1])-len(code[-1].lstrip())
        return 0


class Tangle(mistune.Markdown):
    """A mistune.Markdown processor for literate programming."""
    def render(self, text, **kwargs):
        self.renderer.code = """"""
        super(Tangle, self).render(text, **kwargs)
        return self.renderer.code

    __call__ = render

literate = Tangle(renderer=Code(), escape=False)


class Transformer(UserList, InputTransformer):
    """weave --> macro --> tangle"""
    push = UserList.append
    
    tangle = staticmethod(identity)
    macro = staticmethod(identity)
    weave = staticmethod(identity)
    
    def register_transforms(self):
        self.shell.input_transformer_manager.logical_line_transforms = []
        self.shell.input_transformer_manager.physical_line_transforms = []
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
        if self and self[0].strip(): display.display(*(
            len(self) is 1 and self.macro(body) or [display.Markdown(body)]
        ))
            
    def reset(self, display=True, *, ns=None):
        """This function must complete or IPython hangs."""
        source = '\n'.join(self)
        try:
            source = self.weave(source)
        except:
            warnings.warn("""Unable to weave the source.""")
        display and self.display(source)
        self.data = []
        try:
            source = self.tangle(source, ns=ns or self.shell.user_ns)
        except:
            warnings.warn("""Unable to tangle the source.""")
        return source
    
    def run_code(self, line="""""", body=None):
        self.shell.run_code(self.parse(True, line, body))
        
    def parse(self, display, line="""""", body=None, *, ns=None):
        self.data = line and [line] or [] + (body or """""").splitlines()
        return self.reset(display, ns=ns)
    
    __call__ = partialmethod(parse, False)
    
    __repr__ = InputTransformer.__repr__


def literate_yaml(source, ns={}):
    import yaml
    source = literate(source)
    if source.lstrip().startswith('---'):
        for stream in yaml.safe_load_all(textwrap.dedent(source)):
            if not isinstance(stream, dict): 
                raise SyntaxError("""Each yaml stream must be a dictionary.""")
            ns.update(stream)
        source = """"""
    return filters.ipython2python(source)


class Markdown(Transformer):
    tangle = staticmethod(literate_yaml)
    macro = staticmethod(macro)


class Importer(SourceFileLoader):
    def create_module(self, spec):  
        return ModuleType(self.name)
    
    def exec_module(self, module):
        for cell in reads(Path(self.path).read_text(), 4).cells:
            try:
                if cell['cell_type'] == 'code': exec(
                    self.tangle(cell.source, ns=module.__dict__), module.__dict__)
            except: 
                raise ImportError(cell.source)
        return module

    def find_spec(self, name, paths, target=None):
        loader =  self.find_module(name, paths, target)
        return loader and spec_from_loader(name, loader)

    def find_module(self, name, paths, target=None):
        for path in paths or [Path()]:
            path = (path/Path(name.split('.')[-1])).with_suffix('.ipynb')
            if path.exists(): return Importer(name, str(path))
        return None


def skip(line, code):...


def extension(transformer):
    def load_ipython_extension(ip=get_ipython()):
        nonlocal transformer
        transformer = transformer.instance()
        Importer.tangle = staticmethod(transformer)
        transformer.register_transforms(), transformer.register_magic()
        ip.register_magic_function(skip, 'cell')
        sys.meta_path.append(Importer(None, None)), sys.path_importer_cache.clear()
    return load_ipython_extension

load_ipython_extension = extension(Markdown)
    
def unload_ipython_extension(ip=get_ipython()):
    sys.meta_path = list(filter(
        lambda x: not isinstance(x, Importer), sys.meta_path))
    sys.path_importer_cache.clear()


if __name__ == '__main__':
    load_ipython_extension()
    get_ipython().system('jupyter nbconvert --to python --TemplateExporter.exclude_input_prompt=True literate.ipynb')

