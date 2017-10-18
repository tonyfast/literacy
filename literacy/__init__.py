__import__('importable').load_ipython_extension()

try:
    from .literate import load_ipython_extension
    from . import literate
    from . import template
except:
    pass

Execute = literate.Execute