__import__('importable').load_ipython_extension()

try:
    from .template import load_ipython_extension
    from . import literate
    from . import template
    from . import finder
    from . import patch
except:
    import finder
finder.load_ipython_extension()