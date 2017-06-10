
# coding: utf-8

# 😵 simple __import__s for notebooks and markdown files.  All code elements are executed in order and imported into sys models.

# In[1]:


__all__ = []


# In[3]:


try: 
    from literacy import renderer
    from config import c
except:
    from .literacy import renderer
    from .config import c


# In[4]:


from importlib.util import spec_from_loader
from importlib.machinery import SourceFileLoader, FileFinder
from nbconvert.exporters.base import export, get_exporter
import nbformat, random, sys
from os.path import sep, curdir, extsep, exists
from nbconvert import get_exporter, export


# In[5]:


class State(object):
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.loader, staticmethod):
            cls.loader = staticmethod(cls.loader)
        return super(State, cls).__new__(cls, *args, **kwargs)


# In[6]:


class ExtensionFinder(State):
    def find_spec(self, name, paths, target=None):
        for path in paths or [curdir]:
            path = extsep.join(
                [sep.join([path, name.split('.')[-1]]), self.ext])
            if exists(path):
                return spec_from_loader(name, self.loader(name, path))
        return None


# In[7]:


class NbLoader(SourceFileLoader):
    def get_code(self, path):
        with open(self.path, 'r') as f:
            nb = nbformat.read(f, 4)
        return export(self.exporter, nb)[0].encode('utf-8')


# In[8]:


class IpynbFinder(ExtensionFinder):
    ext = 'ipynb'
    class loader(NbLoader):
        exporter = get_exporter('python')


# In[9]:


class IpyMdFinder(ExtensionFinder):
    ext = 'md.ipynb'
    class loader(NbLoader):
        exporter = IpynbFinder.loader.exporter(config=c)


# In[8]:


class MdFinder(ExtensionFinder):
    ext = 'md'
    class loader(SourceFileLoader):
        def get_code(self, path):
            with open(self.path, 'r') as f:
                renderer.render(f.read())
            return "\n".join(
                map(lambda x: x[0], renderer.renderer.source))


# In[13]:


def load_ipython_extension(ip=get_ipython()):
    for finder in [MdFinder, IpyMdFinder, IpynbFinder]:
        ext = extsep+finder().ext
        sys.meta_path.append(finder())
        sys.path_hooks.append(FileFinder.path_hook((finder.loader, [ext])))
    sys.path_importer_cache.clear()


# In[ ]:


if __name__ == '__main__': 
    get_ipython().system('jupyter nbconvert --to script imports.ipynb')


# In[ ]:




