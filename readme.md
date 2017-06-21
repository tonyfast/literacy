
# __literacy__ - Computable documents in natural language.

> __literacy__ allows [literate programming](roxygen.org/knuth-literate-programming.pdf)-like concepts to work in the notebook. 

---

<code>pip install git+https://github.com/tonyfast/literacy</code>

# __magic__ally load __literacy__


```python
        %load_ext literacy
```


```python
# Literate programming mode

All cells in the notebook accept __Markdown__ as syntax; each code fragment is evaluated as an individual cell. Every 
cell will display a markdown copy of itself before the output. 

> There is no code in this cell, the execution number next to <code>In</code> will _not_ increment.

## Writing code

### Indented code

The cell below looks like state python code
```


# Literate programming mode

All cells in the notebook accept __Markdown__ as syntax; each code fragment is evaluated as an individual cell. Every 
cell will display a markdown copy of itself before the output. 

> There is no code in this cell, the execution number next to <code>In</code> will _not_ increment.

## Writing code

### Indented code

The cell below looks like state python code



```python
        foo = 42
        print(foo)
```


        foo = 42
        print(foo)


    42



```python
Of course, we can now mix plain text into the cell - then code can be injected
    
        print("This evaluated to: {}".format(foo*10))
        
> There are more ways to write code!
```


Of course, we can now mix plain text into the cell - then code can be injected
    
        print("This evaluated to: {}".format(foo*10))
        
> There are more ways to write code!


    This evaluated to: 420



```python
### Inline Code 👉 `print('Say what ❓👂')`

Code can be executed anywhere by wrapping statements in markdown ticks - __`__.
```


### Inline Code 👉 `print('Say what ❓👂')`

Code can be executed anywhere by wrapping statements in markdown ticks - __`__.


    Say what ❓👂



```python
### Code Fences

Pop open the console to see the magic.

        %%javascript 
        console.log("Yo, I can holla hear too.")
```


### Code Fences

Pop open the console to see the magic.

        %%javascript 
        console.log("Yo, I can holla hear too.")



    <IPython.core.display.Javascript object>



```python
## Imports

We must be able to reuse notebooks; __literacy__ provides a system for that.

        %load_ext literacy.imports
    
Now, notebooks and markdown files can be imported.
```


## Imports

We must be able to reuse notebooks; __literacy__ provides a system for that.

        %load_ext literacy.imports
    
Now, notebooks and markdown files can be imported.



```python
### Importing a __Markdown__ file

All code in the document is evaluated; `%rm testfile.md`.

        %%file testfile.md
        This is a text and `pi=3.14`.
        
---

        import testfile
        print("pi = {} from {}.md".format(testfile.pi, testfile.__name__))
```


### Importing a __Markdown__ file

All code in the document is evaluated; `%rm testfile.md`.

        %%file testfile.md
        This is a text and `pi=3.14`.
        
---

        import testfile
        print("pi = {} from {}.md".format(testfile.pi, testfile.__name__))


    Writing testfile.md
    pi = 3.14 from testfile.md



```python
        import readme
```


        import readme


    The literacy extension is already loaded. To reload it, use:
      %reload_ext literacy
    42
    This evaluated to: 420
    Say what ❓👂



    <IPython.core.display.Javascript object>


    The literacy.imports extension is already loaded. To reload it, use:
      %reload_ext literacy.imports
    Writing testfile.md
    pi = 3.14 from testfile.md
    {{foo}}



```python
## Templated code blocks.

Use __jinja2__ template syntax anywhere in the document after loading `%reload_ext literacy.template` 
```


## Templated code blocks.

Use __jinja2__ template syntax anywhere in the document after loading `%reload_ext literacy.template` 



```python
__*{{foo}}*__ can be placed directly into markdown _and_ even used to generate code.

    print("{{foo}}")
    
Full jinja syntaxes are available

{% for i in range(4) %}
0. List item {{i+1}}{% endfor %}

---

Outputs below
```


__*42*__ can be placed directly into markdown _and_ even used to generate code.

    print("42")
    
Full jinja syntaxes are available


0. List item 1
0. List item 2
0. List item 3
0. List item 4

---

Outputs below


    42



```python
##### Unload literacy anytime 
        if __name__ == '__main__': 
            %unload_ext literacy
```


##### Unload literacy anytime 
        if __name__ == '__main__': 
            %unload_ext literacy



```python
            %reload_ext literacy.template
```


```python
        import pandas as pd
```


        import pandas as pd



```python
## Data Science

This tool was designed to tell stories about real data.  Since every code block is just python,
`df=__import__('pandas').util.testing.makeDataFrame();df.head()` to make a __[pd:DataFrame][]__. 

{ {% for key in pd.__dict__ %}
[pd:{{ key }}]: https://github.com/pandas/pandas#{{ key }}{% endfor %}
}
```


## Data Science

This tool was designed to tell stories about real data.  Since every code block is just python,
`df=__import__('pandas').util.testing.makeDataFrame();df.head()` to make a __[pd:DataFrame][]__. 

{ 
[pd:read_sas]: https://github.com/pandas/pandas#read_sas
[pd:tseries]: https://github.com/pandas/pandas#tseries
[pd:read_table]: https://github.com/pandas/pandas#read_table
[pd:concat]: https://github.com/pandas/pandas#concat
[pd:parser]: https://github.com/pandas/pandas#parser
[pd:_version]: https://github.com/pandas/pandas#_version
[pd:tools]: https://github.com/pandas/pandas#tools
[pd:ewmcov]: https://github.com/pandas/pandas#ewmcov
[pd:groupby]: https://github.com/pandas/pandas#groupby
[pd:_window]: https://github.com/pandas/pandas#_window
[pd:rolling_max]: https://github.com/pandas/pandas#rolling_max
[pd:index]: https://github.com/pandas/pandas#index
[pd:test]: https://github.com/pandas/pandas#test
[pd:describe_option]: https://github.com/pandas/pandas#describe_option
[pd:__file__]: https://github.com/pandas/pandas#__file__
[pd:Panel4D]: https://github.com/pandas/pandas#Panel4D
[pd:read_stata]: https://github.com/pandas/pandas#read_stata
[pd:rolling_kurt]: https://github.com/pandas/pandas#rolling_kurt
[pd:read_json]: https://github.com/pandas/pandas#read_json
[pd:expanding_std]: https://github.com/pandas/pandas#expanding_std
[pd:__builtins__]: https://github.com/pandas/pandas#__builtins__
[pd:ewmstd]: https://github.com/pandas/pandas#ewmstd
[pd:Panel]: https://github.com/pandas/pandas#Panel
[pd:DataFrame]: https://github.com/pandas/pandas#DataFrame
[pd:__docformat__]: https://github.com/pandas/pandas#__docformat__
[pd:SparseSeries]: https://github.com/pandas/pandas#SparseSeries
[pd:IndexSlice]: https://github.com/pandas/pandas#IndexSlice
[pd:pivot]: https://github.com/pandas/pandas#pivot
[pd:_np_version_under1p8]: https://github.com/pandas/pandas#_np_version_under1p8
[pd:__cached__]: https://github.com/pandas/pandas#__cached__
[pd:Grouper]: https://github.com/pandas/pandas#Grouper
[pd:info]: https://github.com/pandas/pandas#info
[pd:computation]: https://github.com/pandas/pandas#computation
[pd:__version__]: https://github.com/pandas/pandas#__version__
[pd:NaT]: https://github.com/pandas/pandas#NaT
[pd:ewmcorr]: https://github.com/pandas/pandas#ewmcorr
[pd:_join]: https://github.com/pandas/pandas#_join
[pd:CategoricalIndex]: https://github.com/pandas/pandas#CategoricalIndex
[pd:tslib]: https://github.com/pandas/pandas#tslib
[pd:infer_freq]: https://github.com/pandas/pandas#infer_freq
[pd:ewmvol]: https://github.com/pandas/pandas#ewmvol
[pd:rolling_count]: https://github.com/pandas/pandas#rolling_count
[pd:hashtable]: https://github.com/pandas/pandas#hashtable
[pd:set_eng_float_format]: https://github.com/pandas/pandas#set_eng_float_format
[pd:TimedeltaIndex]: https://github.com/pandas/pandas#TimedeltaIndex
[pd:option_context]: https://github.com/pandas/pandas#option_context
[pd:show_versions]: https://github.com/pandas/pandas#show_versions
[pd:to_pickle]: https://github.com/pandas/pandas#to_pickle
[pd:bdate_range]: https://github.com/pandas/pandas#bdate_range
[pd:rolling_median]: https://github.com/pandas/pandas#rolling_median
[pd:melt]: https://github.com/pandas/pandas#melt
[pd:read_sql]: https://github.com/pandas/pandas#read_sql
[pd:lib]: https://github.com/pandas/pandas#lib
[pd:expanding_sum]: https://github.com/pandas/pandas#expanding_sum
[pd:pnow]: https://github.com/pandas/pandas#pnow
[pd:_np_version_under1p10]: https://github.com/pandas/pandas#_np_version_under1p10
[pd:ewmvar]: https://github.com/pandas/pandas#ewmvar
[pd:ewma]: https://github.com/pandas/pandas#ewma
[pd:to_datetime]: https://github.com/pandas/pandas#to_datetime
[pd:expanding_apply]: https://github.com/pandas/pandas#expanding_apply
[pd:read_html]: https://github.com/pandas/pandas#read_html
[pd:rolling_cov]: https://github.com/pandas/pandas#rolling_cov
[pd:read_msgpack]: https://github.com/pandas/pandas#read_msgpack
[pd:__path__]: https://github.com/pandas/pandas#__path__
[pd:util]: https://github.com/pandas/pandas#util
[pd:HDFStore]: https://github.com/pandas/pandas#HDFStore
[pd:DatetimeIndex]: https://github.com/pandas/pandas#DatetimeIndex
[pd:rolling_apply]: https://github.com/pandas/pandas#rolling_apply
[pd:__doc__]: https://github.com/pandas/pandas#__doc__
[pd:offsets]: https://github.com/pandas/pandas#offsets
[pd:ExcelWriter]: https://github.com/pandas/pandas#ExcelWriter
[pd:to_msgpack]: https://github.com/pandas/pandas#to_msgpack
[pd:indexes]: https://github.com/pandas/pandas#indexes
[pd:TimeSeries]: https://github.com/pandas/pandas#TimeSeries
[pd:pivot_table]: https://github.com/pandas/pandas#pivot_table
[pd:TimeGrouper]: https://github.com/pandas/pandas#TimeGrouper
[pd:__spec__]: https://github.com/pandas/pandas#__spec__
[pd:eval]: https://github.com/pandas/pandas#eval
[pd:SparseTimeSeries]: https://github.com/pandas/pandas#SparseTimeSeries
[pd:api]: https://github.com/pandas/pandas#api
[pd:merge_asof]: https://github.com/pandas/pandas#merge_asof
[pd:match]: https://github.com/pandas/pandas#match
[pd:_np_version_under1p9]: https://github.com/pandas/pandas#_np_version_under1p9
[pd:ExcelFile]: https://github.com/pandas/pandas#ExcelFile
[pd:rolling_skew]: https://github.com/pandas/pandas#rolling_skew
[pd:read_hdf]: https://github.com/pandas/pandas#read_hdf
[pd:scatter_matrix]: https://github.com/pandas/pandas#scatter_matrix
[pd:Index]: https://github.com/pandas/pandas#Index
[pd:isnull]: https://github.com/pandas/pandas#isnull
[pd:read_fwf]: https://github.com/pandas/pandas#read_fwf
[pd:read_gbq]: https://github.com/pandas/pandas#read_gbq
[pd:pandas]: https://github.com/pandas/pandas#pandas
[pd:core]: https://github.com/pandas/pandas#core
[pd:DateOffset]: https://github.com/pandas/pandas#DateOffset
[pd:expanding_min]: https://github.com/pandas/pandas#expanding_min
[pd:factorize]: https://github.com/pandas/pandas#factorize
[pd:get_dummies]: https://github.com/pandas/pandas#get_dummies
[pd:RangeIndex]: https://github.com/pandas/pandas#RangeIndex
[pd:expanding_quantile]: https://github.com/pandas/pandas#expanding_quantile
[pd:np]: https://github.com/pandas/pandas#np
[pd:rolling_std]: https://github.com/pandas/pandas#rolling_std
[pd:reset_option]: https://github.com/pandas/pandas#reset_option
[pd:_testing]: https://github.com/pandas/pandas#_testing
[pd:Period]: https://github.com/pandas/pandas#Period
[pd:_np_version_under1p12]: https://github.com/pandas/pandas#_np_version_under1p12
[pd:stats]: https://github.com/pandas/pandas#stats
[pd:unique]: https://github.com/pandas/pandas#unique
[pd:read_csv]: https://github.com/pandas/pandas#read_csv
[pd:expanding_kurt]: https://github.com/pandas/pandas#expanding_kurt
[pd:expanding_skew]: https://github.com/pandas/pandas#expanding_skew
[pd:types]: https://github.com/pandas/pandas#types
[pd:expanding_var]: https://github.com/pandas/pandas#expanding_var
[pd:ordered_merge]: https://github.com/pandas/pandas#ordered_merge
[pd:expanding_count]: https://github.com/pandas/pandas#expanding_count
[pd:merge]: https://github.com/pandas/pandas#merge
[pd:Timestamp]: https://github.com/pandas/pandas#Timestamp
[pd:ols]: https://github.com/pandas/pandas#ols
[pd:period_range]: https://github.com/pandas/pandas#period_range
[pd:rolling_mean]: https://github.com/pandas/pandas#rolling_mean
[pd:__loader__]: https://github.com/pandas/pandas#__loader__
[pd:MultiIndex]: https://github.com/pandas/pandas#MultiIndex
[pd:get_store]: https://github.com/pandas/pandas#get_store
[pd:crosstab]: https://github.com/pandas/pandas#crosstab
[pd:qcut]: https://github.com/pandas/pandas#qcut
[pd:WidePanel]: https://github.com/pandas/pandas#WidePanel
[pd:to_numeric]: https://github.com/pandas/pandas#to_numeric
[pd:SparseArray]: https://github.com/pandas/pandas#SparseArray
[pd:wide_to_long]: https://github.com/pandas/pandas#wide_to_long
[pd:Categorical]: https://github.com/pandas/pandas#Categorical
[pd:cut]: https://github.com/pandas/pandas#cut
[pd:Term]: https://github.com/pandas/pandas#Term
[pd:msgpack]: https://github.com/pandas/pandas#msgpack
[pd:rolling_window]: https://github.com/pandas/pandas#rolling_window
[pd:plot_params]: https://github.com/pandas/pandas#plot_params
[pd:expanding_cov]: https://github.com/pandas/pandas#expanding_cov
[pd:datetools]: https://github.com/pandas/pandas#datetools
[pd:read_clipboard]: https://github.com/pandas/pandas#read_clipboard
[pd:Int64Index]: https://github.com/pandas/pandas#Int64Index
[pd:read_pickle]: https://github.com/pandas/pandas#read_pickle
[pd:rolling_min]: https://github.com/pandas/pandas#rolling_min
[pd:_np_version_under1p11]: https://github.com/pandas/pandas#_np_version_under1p11
[pd:compat]: https://github.com/pandas/pandas#compat
[pd:expanding_mean]: https://github.com/pandas/pandas#expanding_mean
[pd:lreshape]: https://github.com/pandas/pandas#lreshape
[pd:read_sql_table]: https://github.com/pandas/pandas#read_sql_table
[pd:set_option]: https://github.com/pandas/pandas#set_option
[pd:Series]: https://github.com/pandas/pandas#Series
[pd:options]: https://github.com/pandas/pandas#options
[pd:notnull]: https://github.com/pandas/pandas#notnull
[pd:rolling_sum]: https://github.com/pandas/pandas#rolling_sum
[pd:formats]: https://github.com/pandas/pandas#formats
[pd:PeriodIndex]: https://github.com/pandas/pandas#PeriodIndex
[pd:value_counts]: https://github.com/pandas/pandas#value_counts
[pd:date_range]: https://github.com/pandas/pandas#date_range
[pd:to_timedelta]: https://github.com/pandas/pandas#to_timedelta
[pd:expanding_corr]: https://github.com/pandas/pandas#expanding_corr
[pd:rolling_corr]: https://github.com/pandas/pandas#rolling_corr
[pd:expanding_median]: https://github.com/pandas/pandas#expanding_median
[pd:json]: https://github.com/pandas/pandas#json
[pd:__package__]: https://github.com/pandas/pandas#__package__
[pd:merge_ordered]: https://github.com/pandas/pandas#merge_ordered
[pd:sparse]: https://github.com/pandas/pandas#sparse
[pd:_sparse]: https://github.com/pandas/pandas#_sparse
[pd:SparseList]: https://github.com/pandas/pandas#SparseList
[pd:Float64Index]: https://github.com/pandas/pandas#Float64Index
[pd:read_excel]: https://github.com/pandas/pandas#read_excel
[pd:SparseDataFrame]: https://github.com/pandas/pandas#SparseDataFrame
[pd:Expr]: https://github.com/pandas/pandas#Expr
[pd:io]: https://github.com/pandas/pandas#io
[pd:read_sql_query]: https://github.com/pandas/pandas#read_sql_query
[pd:rolling_var]: https://github.com/pandas/pandas#rolling_var
[pd:rolling_quantile]: https://github.com/pandas/pandas#rolling_quantile
[pd:Timedelta]: https://github.com/pandas/pandas#Timedelta
[pd:timedelta_range]: https://github.com/pandas/pandas#timedelta_range
[pd:_period]: https://github.com/pandas/pandas#_period
[pd:get_option]: https://github.com/pandas/pandas#get_option
[pd:algos]: https://github.com/pandas/pandas#algos
[pd:expanding_max]: https://github.com/pandas/pandas#expanding_max
[pd:__name__]: https://github.com/pandas/pandas#__name__
[pd:fama_macbeth]: https://github.com/pandas/pandas#fama_macbeth
[pd:datetime]: https://github.com/pandas/pandas#datetime
}





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AEKehuhpqD</th>
      <td>0.154174</td>
      <td>-1.000882</td>
      <td>-0.444685</td>
      <td>0.972402</td>
    </tr>
    <tr>
      <th>QQpQfXKjbZ</th>
      <td>-2.272473</td>
      <td>-0.704628</td>
      <td>0.814562</td>
      <td>-0.267862</td>
    </tr>
    <tr>
      <th>zv9TRraOm0</th>
      <td>0.761776</td>
      <td>0.478759</td>
      <td>0.707707</td>
      <td>0.661124</td>
    </tr>
    <tr>
      <th>3uZDo4LXaT</th>
      <td>-1.260420</td>
      <td>-0.735254</td>
      <td>1.049160</td>
      <td>-0.023495</td>
    </tr>
    <tr>
      <th>3wEPOVwnND</th>
      <td>0.997103</td>
      <td>0.284196</td>
      <td>0.913750</td>
      <td>0.825015</td>
    </tr>
  </tbody>
</table>
</div>




```python
`df;` has the following statistical properties `df.describe()`
```


`df;` has the following statistical properties `df.describe()`





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>30.000000</td>
      <td>30.000000</td>
      <td>30.000000</td>
      <td>30.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.266381</td>
      <td>-0.048996</td>
      <td>0.325366</td>
      <td>0.264582</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.179553</td>
      <td>0.886420</td>
      <td>0.997763</td>
      <td>0.585235</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-2.272473</td>
      <td>-1.641722</td>
      <td>-2.090608</td>
      <td>-0.682045</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.578083</td>
      <td>-0.727199</td>
      <td>-0.173506</td>
      <td>-0.212337</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.285519</td>
      <td>-0.107565</td>
      <td>0.536775</td>
      <td>0.195980</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.980661</td>
      <td>0.527109</td>
      <td>1.036832</td>
      <td>0.701554</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2.647800</td>
      <td>1.804646</td>
      <td>1.931856</td>
      <td>1.497927</td>
    </tr>
  </tbody>
</table>
</div>




```python
* Anything that is a file should be importable.  Literacy has rules for markdown and ipynb.
* Merging cell makes more sense.  
* Code and Markdown cells toggle the ability to execute.
* Code prediction works in code cells
* Normal error messages for single cell executions.

# References
```


* Anything that is a file should be importable.  Literacy has rules for markdown and ipynb.
* Merging cell makes more sense.  
* Code and Markdown cells toggle the ability to execute.
* Code prediction works in code cells
* Normal error messages for single cell executions.

# References



```python
        if True and __name__ == '__main__':
            !jupyter nbconvert --to markdown readme.ipynb
```


        if True and __name__ == '__main__':
            !jupyter nbconvert --to markdown readme.ipynb


    [NbConvertApp] Converting notebook readme.ipynb to markdown
    [NbConvertApp] Writing 31763 bytes to readme.md



```python

```


```python
# Markdown [Reference Style][] Links
[Reference Style]: http://daringfireball.com/markdown#reference-links

Unlike a regular link of the pattern `();`
><code>
[Example](http://example.com/path?q=uery#fragment)
</code>

A reference link is of the form `[];`:
><code>
[Example][example]
[example][]
[example]: http://example.com/path?q=uery#fragment
</code>

 

Usually, you have to write out each URL someplace. However, it can be useful to import a whole __namespace__.
       
{% for key in pd.__dict__ %}
[pd:{{ key }}]: https://github.com/pandas/pandas#{{ key }}
{% endfor %}
Now you can talk about [pd:DataFrame][], [pd:io][] or [pd:Series][].
```


# Markdown [Reference Style][] Links
[Reference Style]: http://daringfireball.com/markdown#reference-links

Unlike a regular link of the pattern `();`
><code>
[Example](http://example.com/path?q=uery#fragment)
</code>

A reference link is of the form `[];`:
><code>
[Example][example]
[example][]
[example]: http://example.com/path?q=uery#fragment
</code>

 

Usually, you have to write out each URL someplace. However, it can be useful to import a whole __namespace__.
       

[pd:read_sas]: https://github.com/pandas/pandas#read_sas

[pd:tseries]: https://github.com/pandas/pandas#tseries

[pd:read_table]: https://github.com/pandas/pandas#read_table

[pd:concat]: https://github.com/pandas/pandas#concat

[pd:parser]: https://github.com/pandas/pandas#parser

[pd:_version]: https://github.com/pandas/pandas#_version

[pd:tools]: https://github.com/pandas/pandas#tools

[pd:ewmcov]: https://github.com/pandas/pandas#ewmcov

[pd:groupby]: https://github.com/pandas/pandas#groupby

[pd:_window]: https://github.com/pandas/pandas#_window

[pd:rolling_max]: https://github.com/pandas/pandas#rolling_max

[pd:index]: https://github.com/pandas/pandas#index

[pd:test]: https://github.com/pandas/pandas#test

[pd:describe_option]: https://github.com/pandas/pandas#describe_option

[pd:__file__]: https://github.com/pandas/pandas#__file__

[pd:Panel4D]: https://github.com/pandas/pandas#Panel4D

[pd:read_stata]: https://github.com/pandas/pandas#read_stata

[pd:rolling_kurt]: https://github.com/pandas/pandas#rolling_kurt

[pd:read_json]: https://github.com/pandas/pandas#read_json

[pd:expanding_std]: https://github.com/pandas/pandas#expanding_std

[pd:__builtins__]: https://github.com/pandas/pandas#__builtins__

[pd:ewmstd]: https://github.com/pandas/pandas#ewmstd

[pd:Panel]: https://github.com/pandas/pandas#Panel

[pd:DataFrame]: https://github.com/pandas/pandas#DataFrame

[pd:__docformat__]: https://github.com/pandas/pandas#__docformat__

[pd:SparseSeries]: https://github.com/pandas/pandas#SparseSeries

[pd:IndexSlice]: https://github.com/pandas/pandas#IndexSlice

[pd:pivot]: https://github.com/pandas/pandas#pivot

[pd:_np_version_under1p8]: https://github.com/pandas/pandas#_np_version_under1p8

[pd:__cached__]: https://github.com/pandas/pandas#__cached__

[pd:Grouper]: https://github.com/pandas/pandas#Grouper

[pd:info]: https://github.com/pandas/pandas#info

[pd:computation]: https://github.com/pandas/pandas#computation

[pd:__version__]: https://github.com/pandas/pandas#__version__

[pd:NaT]: https://github.com/pandas/pandas#NaT

[pd:ewmcorr]: https://github.com/pandas/pandas#ewmcorr

[pd:_join]: https://github.com/pandas/pandas#_join

[pd:CategoricalIndex]: https://github.com/pandas/pandas#CategoricalIndex

[pd:tslib]: https://github.com/pandas/pandas#tslib

[pd:infer_freq]: https://github.com/pandas/pandas#infer_freq

[pd:ewmvol]: https://github.com/pandas/pandas#ewmvol

[pd:rolling_count]: https://github.com/pandas/pandas#rolling_count

[pd:hashtable]: https://github.com/pandas/pandas#hashtable

[pd:set_eng_float_format]: https://github.com/pandas/pandas#set_eng_float_format

[pd:TimedeltaIndex]: https://github.com/pandas/pandas#TimedeltaIndex

[pd:option_context]: https://github.com/pandas/pandas#option_context

[pd:show_versions]: https://github.com/pandas/pandas#show_versions

[pd:to_pickle]: https://github.com/pandas/pandas#to_pickle

[pd:bdate_range]: https://github.com/pandas/pandas#bdate_range

[pd:rolling_median]: https://github.com/pandas/pandas#rolling_median

[pd:melt]: https://github.com/pandas/pandas#melt

[pd:read_sql]: https://github.com/pandas/pandas#read_sql

[pd:lib]: https://github.com/pandas/pandas#lib

[pd:expanding_sum]: https://github.com/pandas/pandas#expanding_sum

[pd:pnow]: https://github.com/pandas/pandas#pnow

[pd:_np_version_under1p10]: https://github.com/pandas/pandas#_np_version_under1p10

[pd:ewmvar]: https://github.com/pandas/pandas#ewmvar

[pd:ewma]: https://github.com/pandas/pandas#ewma

[pd:to_datetime]: https://github.com/pandas/pandas#to_datetime

[pd:expanding_apply]: https://github.com/pandas/pandas#expanding_apply

[pd:read_html]: https://github.com/pandas/pandas#read_html

[pd:rolling_cov]: https://github.com/pandas/pandas#rolling_cov

[pd:read_msgpack]: https://github.com/pandas/pandas#read_msgpack

[pd:__path__]: https://github.com/pandas/pandas#__path__

[pd:util]: https://github.com/pandas/pandas#util

[pd:HDFStore]: https://github.com/pandas/pandas#HDFStore

[pd:DatetimeIndex]: https://github.com/pandas/pandas#DatetimeIndex

[pd:rolling_apply]: https://github.com/pandas/pandas#rolling_apply

[pd:__doc__]: https://github.com/pandas/pandas#__doc__

[pd:offsets]: https://github.com/pandas/pandas#offsets

[pd:ExcelWriter]: https://github.com/pandas/pandas#ExcelWriter

[pd:to_msgpack]: https://github.com/pandas/pandas#to_msgpack

[pd:indexes]: https://github.com/pandas/pandas#indexes

[pd:TimeSeries]: https://github.com/pandas/pandas#TimeSeries

[pd:pivot_table]: https://github.com/pandas/pandas#pivot_table

[pd:TimeGrouper]: https://github.com/pandas/pandas#TimeGrouper

[pd:__spec__]: https://github.com/pandas/pandas#__spec__

[pd:eval]: https://github.com/pandas/pandas#eval

[pd:SparseTimeSeries]: https://github.com/pandas/pandas#SparseTimeSeries

[pd:api]: https://github.com/pandas/pandas#api

[pd:merge_asof]: https://github.com/pandas/pandas#merge_asof

[pd:match]: https://github.com/pandas/pandas#match

[pd:_np_version_under1p9]: https://github.com/pandas/pandas#_np_version_under1p9

[pd:ExcelFile]: https://github.com/pandas/pandas#ExcelFile

[pd:rolling_skew]: https://github.com/pandas/pandas#rolling_skew

[pd:read_hdf]: https://github.com/pandas/pandas#read_hdf

[pd:scatter_matrix]: https://github.com/pandas/pandas#scatter_matrix

[pd:Index]: https://github.com/pandas/pandas#Index

[pd:isnull]: https://github.com/pandas/pandas#isnull

[pd:read_fwf]: https://github.com/pandas/pandas#read_fwf

[pd:read_gbq]: https://github.com/pandas/pandas#read_gbq

[pd:pandas]: https://github.com/pandas/pandas#pandas

[pd:core]: https://github.com/pandas/pandas#core

[pd:DateOffset]: https://github.com/pandas/pandas#DateOffset

[pd:expanding_min]: https://github.com/pandas/pandas#expanding_min

[pd:factorize]: https://github.com/pandas/pandas#factorize

[pd:get_dummies]: https://github.com/pandas/pandas#get_dummies

[pd:RangeIndex]: https://github.com/pandas/pandas#RangeIndex

[pd:expanding_quantile]: https://github.com/pandas/pandas#expanding_quantile

[pd:np]: https://github.com/pandas/pandas#np

[pd:rolling_std]: https://github.com/pandas/pandas#rolling_std

[pd:reset_option]: https://github.com/pandas/pandas#reset_option

[pd:_testing]: https://github.com/pandas/pandas#_testing

[pd:Period]: https://github.com/pandas/pandas#Period

[pd:_np_version_under1p12]: https://github.com/pandas/pandas#_np_version_under1p12

[pd:stats]: https://github.com/pandas/pandas#stats

[pd:unique]: https://github.com/pandas/pandas#unique

[pd:read_csv]: https://github.com/pandas/pandas#read_csv

[pd:expanding_kurt]: https://github.com/pandas/pandas#expanding_kurt

[pd:expanding_skew]: https://github.com/pandas/pandas#expanding_skew

[pd:types]: https://github.com/pandas/pandas#types

[pd:expanding_var]: https://github.com/pandas/pandas#expanding_var

[pd:ordered_merge]: https://github.com/pandas/pandas#ordered_merge

[pd:expanding_count]: https://github.com/pandas/pandas#expanding_count

[pd:merge]: https://github.com/pandas/pandas#merge

[pd:Timestamp]: https://github.com/pandas/pandas#Timestamp

[pd:ols]: https://github.com/pandas/pandas#ols

[pd:period_range]: https://github.com/pandas/pandas#period_range

[pd:rolling_mean]: https://github.com/pandas/pandas#rolling_mean

[pd:__loader__]: https://github.com/pandas/pandas#__loader__

[pd:MultiIndex]: https://github.com/pandas/pandas#MultiIndex

[pd:get_store]: https://github.com/pandas/pandas#get_store

[pd:crosstab]: https://github.com/pandas/pandas#crosstab

[pd:qcut]: https://github.com/pandas/pandas#qcut

[pd:WidePanel]: https://github.com/pandas/pandas#WidePanel

[pd:to_numeric]: https://github.com/pandas/pandas#to_numeric

[pd:SparseArray]: https://github.com/pandas/pandas#SparseArray

[pd:wide_to_long]: https://github.com/pandas/pandas#wide_to_long

[pd:Categorical]: https://github.com/pandas/pandas#Categorical

[pd:cut]: https://github.com/pandas/pandas#cut

[pd:Term]: https://github.com/pandas/pandas#Term

[pd:msgpack]: https://github.com/pandas/pandas#msgpack

[pd:rolling_window]: https://github.com/pandas/pandas#rolling_window

[pd:plot_params]: https://github.com/pandas/pandas#plot_params

[pd:expanding_cov]: https://github.com/pandas/pandas#expanding_cov

[pd:datetools]: https://github.com/pandas/pandas#datetools

[pd:read_clipboard]: https://github.com/pandas/pandas#read_clipboard

[pd:Int64Index]: https://github.com/pandas/pandas#Int64Index

[pd:read_pickle]: https://github.com/pandas/pandas#read_pickle

[pd:rolling_min]: https://github.com/pandas/pandas#rolling_min

[pd:_np_version_under1p11]: https://github.com/pandas/pandas#_np_version_under1p11

[pd:compat]: https://github.com/pandas/pandas#compat

[pd:expanding_mean]: https://github.com/pandas/pandas#expanding_mean

[pd:lreshape]: https://github.com/pandas/pandas#lreshape

[pd:read_sql_table]: https://github.com/pandas/pandas#read_sql_table

[pd:set_option]: https://github.com/pandas/pandas#set_option

[pd:Series]: https://github.com/pandas/pandas#Series

[pd:options]: https://github.com/pandas/pandas#options

[pd:notnull]: https://github.com/pandas/pandas#notnull

[pd:rolling_sum]: https://github.com/pandas/pandas#rolling_sum

[pd:formats]: https://github.com/pandas/pandas#formats

[pd:PeriodIndex]: https://github.com/pandas/pandas#PeriodIndex

[pd:value_counts]: https://github.com/pandas/pandas#value_counts

[pd:date_range]: https://github.com/pandas/pandas#date_range

[pd:to_timedelta]: https://github.com/pandas/pandas#to_timedelta

[pd:expanding_corr]: https://github.com/pandas/pandas#expanding_corr

[pd:rolling_corr]: https://github.com/pandas/pandas#rolling_corr

[pd:expanding_median]: https://github.com/pandas/pandas#expanding_median

[pd:json]: https://github.com/pandas/pandas#json

[pd:__package__]: https://github.com/pandas/pandas#__package__

[pd:merge_ordered]: https://github.com/pandas/pandas#merge_ordered

[pd:sparse]: https://github.com/pandas/pandas#sparse

[pd:_sparse]: https://github.com/pandas/pandas#_sparse

[pd:SparseList]: https://github.com/pandas/pandas#SparseList

[pd:Float64Index]: https://github.com/pandas/pandas#Float64Index

[pd:read_excel]: https://github.com/pandas/pandas#read_excel

[pd:SparseDataFrame]: https://github.com/pandas/pandas#SparseDataFrame

[pd:Expr]: https://github.com/pandas/pandas#Expr

[pd:io]: https://github.com/pandas/pandas#io

[pd:read_sql_query]: https://github.com/pandas/pandas#read_sql_query

[pd:rolling_var]: https://github.com/pandas/pandas#rolling_var

[pd:rolling_quantile]: https://github.com/pandas/pandas#rolling_quantile

[pd:Timedelta]: https://github.com/pandas/pandas#Timedelta

[pd:timedelta_range]: https://github.com/pandas/pandas#timedelta_range

[pd:_period]: https://github.com/pandas/pandas#_period

[pd:get_option]: https://github.com/pandas/pandas#get_option

[pd:algos]: https://github.com/pandas/pandas#algos

[pd:expanding_max]: https://github.com/pandas/pandas#expanding_max

[pd:__name__]: https://github.com/pandas/pandas#__name__

[pd:fama_macbeth]: https://github.com/pandas/pandas#fama_macbeth

[pd:datetime]: https://github.com/pandas/pandas#datetime

Now you can talk about [pd:DataFrame][], [pd:io][] or [pd:Series][].

