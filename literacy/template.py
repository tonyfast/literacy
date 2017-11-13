
# coding: utf-8

try:
    from .literate import Markdown, extension, unload_ipython_extension
except:
    from literate import Markdown, extension, unload_ipython_extension


class Jinja2(Markdown):
    template = True


load_ipython_extension = extension(Jinja2)


if __name__ == '__main__':
    load_ipython_extension()
    get_ipython().system('jupyter nbconvert --to python --TemplateExporter.exclude_input_prompt=True template.ipynb')

