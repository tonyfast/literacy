
> In this example we use `literacy.template` mode.


# Importing literate documents

The `literacy` __import__ system relies on `importable;` a tool that uses nbconvert to load
notebooks with the Python __import__ system.  The proper __import__ behavior is activated when 
calling `literacy.load_ipython_extension;`  This behavior will affect standard notebooks.



## Templated code blocks

Consider the print statements below created with.

    print("The name is " + __name__, "💯", 0)
    print("The name is " + __name__, "💯", 1)
    print("The name is " + __name__, "💯", 2)
    print("The name is " + __name__, "💯", 3)
    print("The name is " + __name__, "💯", 4)
    
    
---

_The output is printed below._


    The name is __main__ 💯 0
    The name is __main__ 💯 1
    The name is __main__ 💯 2
    The name is __main__ 💯 3
    The name is __main__ 💯 4



When we `import imports`, we can `assert imports.__file__.endswith('imports.ipynb')`.  And we 
expect to see the print statements evaluated with a different\_\___name__\_\_.

---

_The imported output is printed below._


    The literacy.template extension is already loaded. To reload it, use:
      %reload_ext literacy.template
    The name is imports 💯 0
    The name is imports 💯 1
    The name is imports 💯 2
    The name is imports 💯 3
    The name is imports 💯 4


## Note

__reload_ext__ only works with `literacy`, not `literacy.template`.

## Usage

> Toggle the cell below to convert this document.

    !jupyter nbconvert --config tconfig.py --to markdown imports.ipynb
