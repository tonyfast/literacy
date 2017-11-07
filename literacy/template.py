
# coding: utf-8

try:
    from .literate import Markdown, extension
except:
    from literate import Markdown, extension
from nbconvert.exporters.python import PythonExporter    
exporter = PythonExporter()


class Jinja2(Markdown):
    def weave(self, code):
        return exporter.environment.from_string(code).render(
            getattr(self.shell, 'user_ns', dict()))


load_ipython_extension = extension(Jinja2)


if __name__ == '__main__':
    load_ipython_extension()
    get_ipython().system('jupyter nbconvert --to python --TemplateExporter.exclude_input_prompt=True template.ipynb')

