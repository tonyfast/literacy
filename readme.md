
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

```
%reload_ext literacy
```

`assert literacy` accepts Markdown as source; the inline and indented code objects are concatenated into a single block of __python__ source code.

    foo = 42
    print(foo)
```


# Literacy Programming Mode

```
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


    if __name__ == '__main__':
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



```python
# Nbconvert

`literacy;` complies with the __nbconvert__ converters.  A successful use of literate programming will require the input cells to be suppressed

```bash
jupyter nbconvert --to markdown --TemplateExporter.exclude_input=True readme.ipynb
```

add the <code>--execute</code> flag to execute the notebook before it is converted.
```


# Nbconvert

`literacy;` complies with the __nbconvert__ converters.  A successful use of literate programming will require the input cells to be suppressed

```bash
jupyter nbconvert --to markdown --TemplateExporter.exclude_input=True readme.ipynb
```

add the <code>--execute</code> flag to execute the notebook before it is converted.



```python
# Create this readme.

```%%bash
jupyter nbconvert --to markdown readme.ipynb
```
```


# Create this readme.

```bash
jupyter nbconvert --to markdown readme.ipynb
```

