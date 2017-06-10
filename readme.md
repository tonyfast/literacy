
# `literacy`

`%load literacy` to activate literate `code_cell`s in the `Jupyter` notebook; all Markdown code blocks and spans are evaluated by python.


```
        %load literacy
```


```
# Literate code cells

When __literacy__ is loaded all code cells in the notebook use markdown syntax.  All code elements 
discovered in Markdown are executed by __IPython__ ...

* Inline code spans are evaluated in serialize.  Define `foo=42` and 
`print("from an inline codespan __foo__ is '{}'".format(foo))`
* Block code
    *  __*Double* Indented Code Blocks__
    
            foo*=10
            print("foo is equal to {}".format(foo))
        
    * __*Ticks*__

        ```python
        foo*=10
        print("foo got bigger again 👉 {}".format(foo))
        ```
```


# Literate code cells

When __literacy__ is loaded all code cells in the notebook use markdown syntax.  All code elements 
discovered in Markdown are executed by __IPython__ ...

* Inline code spans are evaluated in serialize.  Define `foo=42` and 
`print("from an inline codespan __foo__ is '{}'".format(foo))`
* Block code
    *  __*Double* Indented Code Blocks__
    
            foo*=10
            print("foo is equal to {}".format(foo))
        
    * __*Ticks*__

        ```python
        foo*=10
        print("foo got bigger again 👉 {}".format(foo))
        ```

---



    from an inline codespan __foo__ is '42'
    foo is equal to 420
    foo got bigger again 👉 4200



```
## Magics

Since the codespans always evaluated as python they accept magics.

### Line

Initialize `%autocall 1` to remove the required for parenthesis so `print foo` works.

### Cell - `rm new.txt`

        %%file new.txt
        This content is written to a file.
        
`assert __import__('os').path.exists('new.txt')` ⅋ `print "This message only if the file exists."`
```


## Magics

Since the codespans always evaluated as python they accept magics.

### Line

Initialize `%autocall 1` to remove the required for parenthesis so `print foo` works.

### Cell - `rm new.txt`

        %%file new.txt
        This content is written to a file.
        
`assert __import__('os').path.exists('new.txt')` ⅋ `print "This message only if the file exists."`

---



    Automatic calling is: Smart
    ------> print(foo)
    4200
    Writing new.txt
    ------> print("This message only if the file exists.")
    This message only if the file exists.



```
## Usage

Convert this document to the readme file.

            if __name__ == '__main__':
                !jupyter nbconvert --to markdown readme.ipynb
```


## Usage

Convert this document to the readme file.

            if __name__ == '__main__':
                !jupyter nbconvert --to markdown readme.ipynb

---




```

```
