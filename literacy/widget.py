
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
    md = Any()
    @observe('template')
    def _change_render(self, change=dict()):
        try:
            source = self.template.render(**self.ns)
            self.value = """"""
            for output in literate.macro(source):
                self.value += (
                    markdown(output.data, True)
                    if isinstance(output, display.Markdown)
                    else output._repr_html_() )+ '\n'
        except Exception as e: ...


class Interact(template.Jinja2):
    def weave(self, body, *, ns=dict(), disp=True):
        disp and display.display(Template(template=body, ns=ns))
        return body.render(**ns)


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

