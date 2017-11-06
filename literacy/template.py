
# coding: utf-8

try:
    from .literate import Literate, extension
except:
    from literate import Literate, extension
from nbconvert.exporters.python import PythonExporter    
exporter = PythonExporter()


class Template(Literate):
    def weave(self, code):
        return exporter.environment.from_string(code).render(
            getattr(self.shell, 'user_ns', dict()))


load_ipython_extension = extension(Template)


if __name__ == '__main__':
    load_ipython_extension()
    get_ipython().system('jupyter nbconvert --to python --TemplateExporter.exclude_input_prompt=True template.ipynb')


a = 100


