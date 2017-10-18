
# Display Objects


By default, returns the markdown view of the code cell.  All the markdown syntaxes accepted by 
the `__import__('mistune').Renderer;` are understood.


## Suppressing Markdown Output


Sometimes it is desirable to suppress the Markdown input.  Supply a __single blank line__ 
at the beginning of the cell to suppress the output.

> The code cell below illustrates this point.



### Motivation

In IPython, indented code with an empty first like with raise an `Exception;`  Suppressing output
with a single blank removes a mode of failure in executing the code.  It also provides
a single click UX to make this change.


## Dereferencing Objects


The IPython display objects have logic for presenting URLS and filenames.  __literacy__ tweaked these 
opinions slightly to provide a canonical experience with Files and Urls.



### Configuration

1. Use a config file to format our converter.

        %%file config.py

2. Exclude the code cell inputs.
        
        c.TemplateExporter.exclude_input = True

3. Use a custom literacy.Execute to template and run the codes.

        c.Exporter.preprocessors = ['literacy.Execute']
    
    > When using __literacy.template__ rely on.
    
        # c.Exporter.preprocessors = ['literacy.template.Execute']


    Overwriting config.py


#### Approach 1: Exploding and Executing

Originally we tried exploding the markdown and code cells into a single notebook then applying the standard __ExecutePreprocessor__.  This did not work because of the `literacy` logic that displays files and urls.

## Usage

> Toggle the cell below to convert this document.

    !jupyter nbconvert --config config.py --to markdown display-objects.ipynb
