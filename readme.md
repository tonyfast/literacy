
# __literacy__ - interactive literate programming in markdown

> [`...`](http://roxygen.org/knuth-literate-programming.pdf) considering programs to be works of literature. `...`  surely nobody wants to admit writing an _illiterate_ program.
> - _Donald Knuth_ - **Literate Programming** 

## Installation

```bash
pip install git+https://github.com/tonyfast/literacy
```

# Literacy Programming Mode
    


```
    %reload_ext literacy
```

---
    
`import literacy` accepts Markdown as source; the __inline__, __fenced__, __indented__ code objects are concatenated into a single block of __python__ 
source code.  _All code in this block is executed._

    foo = 42
    print(foo)
    assert literacy
    
---


    42



# Templating Mode

    %reload_ext literacy.template

Template mode applies `__import__('jinja2');` to weave variables in scope into the markdown source.



## More readable

Use the templating system to explicitly write source, rather than implicit <code>for</code> loops.

    print(0); print(1); print(2); print(3); 


    0
    1
    2
    3



# Macros

## yaml

Begin a code block with <code>---</code> to invoke yaml syntax as valid data input.  _This is great for taking notes._

    ---
    refs:
    - roxygen.org/knuth-literate-programming.pdf
    - https://en.wikipedia.org/wiki/Literate_programming
        
> _The yaml source must contain named objects at the top level._



    assert 'refs' in globals() 



---
    
    if __name__ == '__main__':
        
# Importable Literate Notebooks

    
        import readme
        
with the following tests 

        assert readme.__file__ == 'readme.ipynb'
        assert readme.foo is foo
        foo = 3.14
        assert readme.foo is not foo
        

---

_`literacy;` makes it possible to import any notebook._

---


    42
    0
    1
    2
    3


    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 2346 bytes to readme.md



# This is literate source



# Inspect Source

In the interactive mode `assert In` exists to store the prior code executed.

It is possible to `def \`ine a function named `foo\` with a body composed below,

Our function __foo__ has parameters __x__ and __y__

    (x=42, y=10):
        """Make sure to have a docstring"""
with the ability to interpose markdown into the code, and
        
        return x*y


    The source code for the previous cell is:
    
     assert In
    def foo(x=42, y=10):
        """Make sure to have a docstring"""
    
        return x*y



# Nbconvert

`literacy;` complies with the __nbconvert__ converters.  A successful use of literate programming will require the input cells to be suppressed

```%%bash
jupyter nbconvert --to markdown --TemplateExporter.exclude_input=True readme.ipynb
```

add the <code>--execute</code> flag to execute the notebook before it is converted.



    %%markdown
    # This is literate source



# This is literate source

