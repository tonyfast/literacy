
# __literacy__ - interactive literate programming in markdown

> [`...`](http://roxygen.org/knuth-literate-programming.pdf) considering programs to works of literature. 
> _- Donald Knuth - **Literate Programming** 

## Installation


    %%bash
    pip install git+https://github.com/tonyfast/literacy

# Literate programming mode


```python
        %load_ext literacy
```


```python
__literacy__ allows code cells in the Jupyter notebook to execute code objects within markdown.
All inline code objects are executed like, `print('inline')`
```


__literacy__ allows code cells in the Jupyter notebook to execute code objects within markdown.
All inline code objects are executed like, `print('inline')`


    inline



```python
### Stuff

* Anything that is a file should be importable.  Literacy has rules for markdown and ipynb.
* Merging cell makes more sense.  
* Code and Markdown cells toggle the ability to execute.
* Code prediction works in code cells
* Normal error messages for single cell executions.

# References
```


### Stuff

* Anything that is a file should be importable.  Literacy has rules for markdown and ipynb.
* Merging cell makes more sense.  
* Code and Markdown cells toggle the ability to execute.
* Code prediction works in code cells
* Normal error messages for single cell executions.

# References



```python
        if True and __name__ == '__main__':
            !jupyter nbconvert --to markdown readme.ipynb
            !jupyter nbconvert --to markdown --config docs/tconfig.py docs/*.ipynb
```


        if True and __name__ == '__main__':
            !jupyter nbconvert --to markdown readme.ipynb
            !jupyter nbconvert --to markdown --config docs/tconfig.py docs/*.ipynb


    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 2064 bytes to readme.md
    [NbConvertApp] Converting notebook docs/display-objects.ipynb to markdown
    [NbConvertApp] Executing notebook with kernel: python3
    [NbConvertApp] Writing 1701 bytes to docs/display-objects.md
    [NbConvertApp] Converting notebook docs/imports.ipynb to markdown
    [NbConvertApp] Executing notebook with kernel: python3
    [NbConvertApp] Writing 1549 bytes to docs/imports.md
    [NbConvertApp] Converting notebook docs/nbconversions.ipynb to markdown
    [NbConvertApp] Executing notebook with kernel: python3
    [NbConvertApp] Writing 1201 bytes to docs/nbconversions.md



```python
        !jupyter nbconvert --config config.py literacy/template.ipynb
```

    [NbConvertApp] Converting notebook literacy/template.ipynb to html
    [NbConvertApp] Executing notebook with kernel: python3
    [NbConvertApp] Writing 255087 bytes to literacy/template.html



```python

```
