
# coding: utf-8

# experimental: i am not even sure why you would use this.

try:
    from . import template, literate
except:
    import template, literate
from traitlets import Any, observe
from types import MethodType
from contextlib import contextmanager
from IPython.core.interactiveshell import InteractiveShell
from IPython import display, get_ipython
from ipywidgets import HTML, Widget
from mistune import markdown
import ipywidgets


class Template(HTML):
    template = Any()
    ns = Any(default_value=dict())
    @observe('template')
    def _change_render(self, change=dict()):
        try:
            source = self.template.render(**self.ns)
            self.value = """"""
            for output in literate.macro(source):
                self.value += (
                    markdown(output.data, True)
                    if isinstance(output, display.Markdown)
                    else output._repr_html_() 
                )+ '\n'
        except Exception as e: ...


class Interact(template.Jinja2):
    def macro(self, body, *, ns=dict(), out=tuple()):
        return Template(template=body, ns=ns),        


@contextmanager
def _run_cell(self, raw_cell, store_history=False, silent=False, shell_futures=True):
    from ipywidgets import Widget
    yield InteractiveShell.run_cell(self, raw_cell, store_history=False, silent=False, shell_futures=True)
    for value in Widget.widgets.values():
        if isinstance(value, Template): value._change_render()

def run_cell(self, raw_cell, store_history=False, silent=False, shell_futures=True):
    with _run_cell(self, raw_cell, store_history=False, silent=False, shell_futures=True) as e:
        ...
    return e


def load_ipython_extension(ip=get_ipython()):
    template.extension(Interact)(ip)
    ip.run_cell = MethodType(run_cell, get_ipython())


def unload_ipython_extension(ip=get_ipython()):
    ip.run_cell = MethodType(InteractiveShell.run_cell, get_ipython())
    template.unload_ipython_extension()


if __name__ == '__main__':
    load_ipython_extension()
    get_ipython().system('jupyter nbconvert --to python --TemplateExporter.exclude_input_prompt=True widget.ipynb')


# ADFasd

asdf


---
sources:
- https://www.codeproject.com/KB/GDI-plus/ImageProcessing2/flip.jpg
- https://www.smashingmagazine.com/wp-content/uploads/2015/06/10-dithering-opt.jpg
- https://camo.mybb.com/e01de90be6012adc1b1701dba899491a9348ae79/687474703a2f2f7777772e6a71756572797363726970742e6e65742f696d616765732f53696d706c6573742d526573706f6e736976652d6a51756572792d496d6167652d4c69676874626f782d506c7567696e2d73696d706c652d6c69676874626f782e6a7067


sources

