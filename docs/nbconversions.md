
# *nbconvert* Entry Points


## ExecutePreprocessors

__literacy__ changes the behavior of the run cell method.  As a result it is not compatable 
the standard `nbconvert.preprocessors.execute.ExecutePreprocessor`; instead 
we use `literacy.literate.Execute` and `literacy.template.Execute;` to execute markdown or jinja markdown, respectively.



### Configuration

1. Use a config file to format our converter.

        %%file config.py

2. Exclude the code cell inputs.
        
        c.TemplateExporter.exclude_input = True

3. Use a custom literacy.Execute to template and run the codes.

        c.Exporter.preprocessors = ['literacy.Execute']
    
    > When using __literacy.template__ rely on.
    
        #c.Exporter.preprocessors = ['literacy.template.Execute']


    Overwriting config.py


#### Approach 1: Exploding and Executing

Originally we tried exploding the markdown and code cells into a single notebook then applying the standard __ExecutePreprocessor__.  This did not work because of the `literacy` logic that displays files and urls.

## Usage

> Toggle the cell below to convert this document.

    !jupyter nbconvert --config config.py --to markdown nbconversions.ipynb
