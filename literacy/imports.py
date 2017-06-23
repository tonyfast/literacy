
# coding: utf-8

# 😵 simple __import__s for notebooks and markdown files.  All code elements are executed in order and imported into sys models.

# In[35]:


__all__ = []


# In[36]:


try: 
    from preprocessors import Explode, JoinSource
except:
    from .preprocessors import Explode, JoinSource

from importlib.util import spec_from_loader
from importlib.machinery import SourceFileLoader, FileFinder
from nbconvert.exporters.base import export, get_exporter
import sys
from os.path import sep, curdir, extsep, exists
from nbconvert import get_exporter, export
from nbformat.v4 import  new_notebook, new_code_cell


# In[37]:


class State(object):
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.Loader, staticmethod):
            cls.Loader = staticmethod(cls.Loader)
        return super(State, cls).__new__(cls, *args, **kwargs)

class ExtensionFinder(State):
    def find_spec(self, name, paths, target=None):
        for path in paths or [curdir]:
            path = extsep.join(
                [sep.join([path, name.split('.')[-1]]), self.ext])
            if exists(path):
                return spec_from_loader(name, self.Loader(name, path))
        return None


# In[38]:


exporter = get_exporter('python')(config={'Exporter': {'preprocessors': [Explode(), JoinSource()]}})


# In[39]:


class IpynbFinder(ExtensionFinder):
    ext = 'ipynb'
    class Loader(SourceFileLoader):
        def get_code(self, nb):
            return exporter.from_filename(self.path)[0].encode('utf-8')


# In[40]:


class MdFinder(ExtensionFinder):
    ext = 'md'
    class Loader(SourceFileLoader):
        def get_code(self, path):
            with open(self.path) as f:
                return exporter.from_notebook_node(
                    new_notebook(cells=[new_code_cell(f.read())]))[0].encode('utf-8')


# In[41]:


def load_ipython_extension(ip=get_ipython()):
    for finder in [IpynbFinder, MdFinder]:
        sys.meta_path.append(finder())
        sys.path_hooks.append(FileFinder.path_hook((finder.Loader, [extsep+finder.ext])))
    sys.path_importer_cache.clear()


# In[42]:


if __name__ == '__main__': 
    get_ipython().system('jupyter nbconvert --to script imports.ipynb')


# In[ ]:




