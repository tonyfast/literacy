
# coding: utf-8

from importlib import machinery


try:
    from .literate import LiterateTransformer, extension, exporter
except:
    from literate import LiterateTransformer, extension, exporter
import sys


class TemplateTransformer(LiterateTransformer):
    def weave(self, code):
        return exporter.environment.from_string(code).render(
            getattr(self.shell, 'user_ns', dict))


load_ipython_extension = extension(TemplateTransformer.instance())


if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to python --TemplateExporter.exclude_input_prompt=True template.ipynb')

