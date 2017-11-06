
# __literacy__ - interactive literate programming in markdown

> [`...`](http://roxygen.org/knuth-literate-programming.pdf) considering programs to be works of literature. `...`  surely nobody wants to admit writing an _illiterate_ program.
> - _Donald Knuth_ - **Literate Programming** 

## Installation


    %%bash
    pip install git+https://github.com/tonyfast/literacy
    


```python
    %reload_ext literacy
    import literacy
```


```python
# Literacy Programming Mode

```python
%reload_ext literacy
```

`assert literacy` accepts Markdown as source; the inline and indented code objects are concatenated into a single block of __python__ source code.

    foo = 42
    print(foo)
```


# Literacy Programming Mode

```python
%reload_ext literacy
```

`assert literacy` accepts Markdown as source; the inline and indented code objects are concatenated into a single block of __python__ source code.

    foo = 42
    print(foo)


    42



```python
# Templating Mode

    %reload_ext literacy.template

Template mode users `__import__('jinja2');` to weave variables in scope into the markdown source.
```


# Templating Mode

    %reload_ext literacy.template

Template mode users `__import__('jinja2');` to weave variables in scope into the markdown source.



```python
## More readable

Use the templating system to explicitly write source, rather than implicit <code>for</code> loops.

    {% for i in range(4) %}print({{i}}); {% endfor %}
```


## More readable

Use the templating system to explicitly write source, rather than implicit <code>for</code> loops.

    print(0); print(1); print(2); print(3); 


    0
    1
    2
    3



```python
# Macros

## yaml magic

Being an indented code block with <code>---</code> to invoke yaml syntax as valid data input.  _This is great for taking notes._

    ---
    refs:
    - roxygen.org/knuth-literate-programming.pdf
    - https://en.wikipedia.org/wiki/Literate_programming
```


# Macros

## yaml magic

Being an indented code block with <code>---</code> to invoke yaml syntax as valid data input.  _This is great for taking notes._

    ---
    refs:
    - roxygen.org/knuth-literate-programming.pdf
    - https://en.wikipedia.org/wiki/Literate_programming



```python
    assert 'refs' in globals() 
```


    assert 'refs' in globals() 



```python
    if __name__ == '__main__':
        import readme
        assert readme.__file__ == 'readme.ipynb'
        assert readme.foo is foo
        foo = 3.14
        assert readme.foo is not foo
```


    import readme
    assert readme.__file__ == 'readme.ipynb'
    assert readme.foo is foo
    foo = 3.14
    assert readme.foo is not foo


    42
    0
    1
    2
    3



    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    ~/literacy2/literacy/literate.py in exec_module(self, module)
        158                 if cell['cell_type'] == 'code': exec(
    --> 159                     self.tangle(cell.source, ns=module.__dict__), module.__dict__)
        160             except:


    ~/literacy2/readme.ipynb in <module>()


    AssertionError: 

    
    During handling of the above exception, another exception occurred:


    ImportError                               Traceback (most recent call last)

    <ipython-input-7-dae75a05d818> in <module>()
    ----> 1 import readme
          2 assert readme.__file__ == 'readme.ipynb'
          3 assert readme.foo is foo
          4 foo = 3.14
          5 assert readme.foo is not foo


    ~/literacy2/literacy/literate.py in exec_module(self, module)
        159                     self.tangle(cell.source, ns=module.__dict__), module.__dict__)
        160             except:
    --> 161                 raise ImportError(cell.source)
        162         return module
        163 


    ImportError:     import readme
        assert readme.__file__ == 'readme.ipynb'
        assert readme.foo is foo
        foo = 3.14
        assert readme.foo is not foo



```python
# Nbconvert

`literacy;` complies with the __nbconvert__ converters.  A successful use of literate programming will require the input cells to be suppressed

```python
!jupyter nbconvert --to markdown --TemplateExporter.exclude_input=True readme.ipynb
```

add the <code>--execute</code> flag to execute the notebook before it is converted.
```


# Nbconvert

`literacy;` complies with the __nbconvert__ converters.  A successful use of literate programming will require the input cells to be suppressed

```python
!jupyter nbconvert --to markdown --TemplateExporter.exclude_input=True readme.ipynb
```

add the <code>--execute</code> flag to execute the notebook before it is converted.



```python
    !jupyter nbconvert --to markdown readme.ipynb
```


    !jupyter nbconvert --to markdown --TemplateExporter.exclude_input=True readme.ipynb


    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 1531 bytes to readme.md

