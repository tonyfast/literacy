
# __literacy__ - interactive literate programming in markdown

> [`...`](http://roxygen.org/knuth-literate-programming.pdf) considering programs to be works of literature. `...`  surely nobody wants to admit writing an _illiterate_ program.
> - _Donald Knuth_ - **Literate Programming** 

## Installation


    %%bash
    pip install git+https://github.com/tonyfast/literacy
    


# Literacy Programming Mode

```python
%reload_ext literacy
```

`assert literacy` accepts Markdown as source; the inline and indented code objects are concatenated into a single block of __python__ source code.

    foo = 42
    print(foo)


    42



# Templating Mode

    %reload_ext literacy.template

Template mode users `__import__('jinja2');` to weave variables in scope into the markdown source.



## More readable

Use the templating system to explicitly write source, rather than implicit <code>for</code> loops.

    print(0); print(1); print(2); print(3); 


    0
    1
    2
    3



# Macros

## yaml magic

Being an indented code block with <code>---</code> to invoke yaml syntax as valid data input.  _This is great for taking notes._

    ---
    refs:
    - roxygen.org/knuth-literate-programming.pdf
    - https://en.wikipedia.org/wiki/Literate_programming



    assert 'refs' in globals()



    import readme
    assert readme.__file__ == 'readme.ipynb'
    assert readme.foo is foo
    foo = 3.14
    assert readme.foo is not foo



    !jupyter nbconvert --to markdown --TemplateExporter.exclude_input=True readme.ipynb

