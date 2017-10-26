__import__('importable').load_ipython_extension()

from .literate import load_ipython_extension
from . import literate
from . import template

Execute = literate.Execute