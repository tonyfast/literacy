
# __literacy__ - interactive literate programming in markdown

> [`...`](http://roxygen.org/knuth-literate-programming.pdf) considering programs to works of literature. `...`  surely nobody wants to admit writing an _illiterate_ program.
> - _Donald Knuth_ - **Literate Programming** 

## Installation


    %%bash
    pip install git+https://github.com/tonyfast/literacy
    
### Activate literacy


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



    !jupyter nbconvert --to markdown --config docs/config.py readme.ipynb
    !jupyter nbconvert --to markdown --config docs/tconfig.py docs/*.ipynb


    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Executing notebook with kernel: python3
    [NbConvertApp] ERROR | Error while converting 'readme.ipynb'
    Traceback (most recent call last):
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/nbconvertapp.py", line 381, in export_single_notebook
        output, resources = self.exporter.from_filename(notebook_filename, resources=resources)
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/exporters/exporter.py", line 172, in from_filename
        return self.from_file(f, resources=resources, **kw)
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/exporters/exporter.py", line 190, in from_file
        return self.from_notebook_node(nbformat.read(file_stream, as_version=4), resources=resources, **kw)
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/exporters/templateexporter.py", line 268, in from_notebook_node
        nb_copy, resources = super(TemplateExporter, self).from_notebook_node(nb, resources, **kw)
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/exporters/exporter.py", line 132, in from_notebook_node
        nb_copy, resources = self._preprocess(nb_copy, resources)
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/exporters/exporter.py", line 309, in _preprocess
        nbc, resc = preprocessor(nbc, resc)
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/preprocessors/base.py", line 47, in __call__
        return self.preprocess(nb,resources)
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/preprocessors/execute.py", line 242, in preprocess
        nb, resources = super(ExecutePreprocessor, self).preprocess(nb, resources)
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/preprocessors/base.py", line 70, in preprocess
        nb.cells[index], resources = self.preprocess_cell(cell, resources, index)
      File "/Users/tonyfast/anaconda/lib/python3.5/site-packages/nbconvert/preprocessors/execute.py", line 275, in preprocess_cell
        raise CellExecutionError(msg)
    nbconvert.preprocessors.execute.CellExecutionError: An error occurred while executing the following cell:
    ------------------
    
    # coding: utf-8
    
    # In[ ]:
    
    
    print('inline')
    print('block code')
    
    
    def foo(a):
        b = 42*a
    
    
        return 42*a
    
    
    ------------------
    
    SyntaxError: 'return' outside function (<ipython-input-2-083e2d18f9c8>, line 7)
    
    [NbConvertApp] Converting notebook docs/display-objects.ipynb to markdown
    [NbConvertApp] Executing notebook with kernel: python3
    [NbConvertApp] Writing 1703 bytes to docs/display-objects.md
    [NbConvertApp] Converting notebook docs/imports.ipynb to markdown
    [NbConvertApp] Executing notebook with kernel: python3
    [NbConvertApp] Writing 1549 bytes to docs/imports.md
    [NbConvertApp] Converting notebook docs/nbconversions.ipynb to markdown
    [NbConvertApp] Executing notebook with kernel: python3
    [NbConvertApp] Writing 1201 bytes to docs/nbconversions.md

