
# __literacy__ - interactive literate programming in markdown

> [`...`](http://roxygen.org/knuth-literate-programming.pdf) considering programs to works of literature. `...`  surely nobody wants to admit writing an _illiterate_ program.
> - _Donald Knuth_ - **Literate Programming** 

## Installation


    %%bash
    pip install git+https://github.com/tonyfast/literacy
    
### Activate literacy

    %load_ext literacy


Literacy transforms all code cells to interactive blocks of markdown.  When a cell is executed:
    
1. The code blocks are __tangled__ from the markdown source.
2. The source code is __woven__, sometimes through a __jinja2__ template, then displayed as a markdown object[]

> Cells without code blocks do not increment the input number.



In iteractive literate mode, all inline code cells, like `print('inline')`, and code blocks

    print('block code')
    
are concatenated as python and executed.
    
Compose functions in markdown...
    
    def foo(a): 
        b = 42*a
and add annotations in between lines of code.
        return 42*a


    inline
    block code



## Templating Mode



## [Importing Literate Notebooks](docs/imports.md).



## [Converting and Executing Literate Notebooks](docs/display-objects.md).



## Macros

__macros__ hide abstractions.  `import literacy` has a few simples __macros__, or rules.



### Files

Simply place a local filename in a code cell to render it as markdown.

    %%file test.md
    ###### I am going to be __*imported*__


    Overwriting test.md



###### I am going to be __*imported*__



### Urls

Place a url in the code cell to show a webiste as an <code>iframe</code>.



### Escaping Output

Begin a code cell with a blank to suppress output.


#### Motivation

Literate programming with Markdown encourages code blocks to have a single indent.  In IPython 
code cells a new line + a tab returns an `IndentationError`:
    
    try:
        eval("""\n\tprint('👎')""")
    except IndentationError:
        
while removing the tab is allowed.
    
        eval("""\nprint('👍')""")
        
        
The blank line opinion makes it more difficult to activate an `IndentationError`.


    👍


    code



    !jupyter nbconvert --to markdown --TemplateExporter.exclude_input=True readme.ipynb
    !jupyter nbconvert --to markdown --config docs/tconfig.py docs/*.ipynb


    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 2785 bytes to readme.md
    [NbConvertApp] Converting notebook docs/display-objects.ipynb to markdown
    [NbConvertApp] Executing notebook with kernel: python3
    [NbConvertApp] Writing 1703 bytes to docs/display-objects.md
    [NbConvertApp] Converting notebook docs/imports.ipynb to markdown
    [NbConvertApp] Executing notebook with kernel: python3
    [NbConvertApp] Writing 1549 bytes to docs/imports.md
    [NbConvertApp] Converting notebook docs/nbconversions.ipynb to markdown
    [NbConvertApp] Executing notebook with kernel: python3
    [NbConvertApp] Writing 1201 bytes to docs/nbconversions.md

