
# __literacy__ - Computable documents in natural language.

> __literacy__ allows [literate programming](roxygen.org/knuth-literate-programming.pdf)-like concepts to work in the notebook. 

---

<code>pip install git+https://github.com/tonyfast/literacy</code>

# __magic__ally load __literacy__


```python
        %load_ext literacy
```


        %load_ext literacy



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


    The literacy.imports extension is already loaded. To reload it, use:
      %reload_ext literacy.imports



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
[pd:_version]: https://github.com/pandas/pandas#_version
[pd:expanding_quantile]: https://github.com/pandas/pandas#expanding_quantile
[pd:__doc__]: https://github.com/pandas/pandas#__doc__
[pd:ewmcov]: https://github.com/pandas/pandas#ewmcov
[pd:factorize]: https://github.com/pandas/pandas#factorize
[pd:MultiIndex]: https://github.com/pandas/pandas#MultiIndex
[pd:fama_macbeth]: https://github.com/pandas/pandas#fama_macbeth
[pd:core]: https://github.com/pandas/pandas#core
[pd:RangeIndex]: https://github.com/pandas/pandas#RangeIndex
[pd:read_sql_query]: https://github.com/pandas/pandas#read_sql_query
[pd:set_option]: https://github.com/pandas/pandas#set_option
[pd:Panel4D]: https://github.com/pandas/pandas#Panel4D
[pd:tseries]: https://github.com/pandas/pandas#tseries
[pd:show_versions]: https://github.com/pandas/pandas#show_versions
[pd:ExcelFile]: https://github.com/pandas/pandas#ExcelFile
[pd:plot_params]: https://github.com/pandas/pandas#plot_params
[pd:Float64Index]: https://github.com/pandas/pandas#Float64Index
[pd:rolling_kurt]: https://github.com/pandas/pandas#rolling_kurt
[pd:DatetimeIndex]: https://github.com/pandas/pandas#DatetimeIndex
[pd:rolling_max]: https://github.com/pandas/pandas#rolling_max
[pd:reset_option]: https://github.com/pandas/pandas#reset_option
[pd:SparseDataFrame]: https://github.com/pandas/pandas#SparseDataFrame
[pd:bdate_range]: https://github.com/pandas/pandas#bdate_range
[pd:rolling_median]: https://github.com/pandas/pandas#rolling_median
[pd:__docformat__]: https://github.com/pandas/pandas#__docformat__
[pd:rolling_window]: https://github.com/pandas/pandas#rolling_window
[pd:expanding_max]: https://github.com/pandas/pandas#expanding_max
[pd:to_datetime]: https://github.com/pandas/pandas#to_datetime
[pd:ewmcorr]: https://github.com/pandas/pandas#ewmcorr
[pd:Series]: https://github.com/pandas/pandas#Series
[pd:expanding_corr]: https://github.com/pandas/pandas#expanding_corr
[pd:SparseSeries]: https://github.com/pandas/pandas#SparseSeries
[pd:Int64Index]: https://github.com/pandas/pandas#Int64Index
[pd:Grouper]: https://github.com/pandas/pandas#Grouper
[pd:rolling_corr]: https://github.com/pandas/pandas#rolling_corr
[pd:to_msgpack]: https://github.com/pandas/pandas#to_msgpack
[pd:test]: https://github.com/pandas/pandas#test
[pd:get_option]: https://github.com/pandas/pandas#get_option
[pd:read_html]: https://github.com/pandas/pandas#read_html
[pd:read_stata]: https://github.com/pandas/pandas#read_stata
[pd:SparseTimeSeries]: https://github.com/pandas/pandas#SparseTimeSeries
[pd:CategoricalIndex]: https://github.com/pandas/pandas#CategoricalIndex
[pd:ols]: https://github.com/pandas/pandas#ols
[pd:get_dummies]: https://github.com/pandas/pandas#get_dummies
[pd:set_eng_float_format]: https://github.com/pandas/pandas#set_eng_float_format
[pd:rolling_skew]: https://github.com/pandas/pandas#rolling_skew
[pd:scatter_matrix]: https://github.com/pandas/pandas#scatter_matrix
[pd:ordered_merge]: https://github.com/pandas/pandas#ordered_merge
[pd:_np_version_under1p10]: https://github.com/pandas/pandas#_np_version_under1p10
[pd:rolling_apply]: https://github.com/pandas/pandas#rolling_apply
[pd:TimeGrouper]: https://github.com/pandas/pandas#TimeGrouper
[pd:_period]: https://github.com/pandas/pandas#_period
[pd:read_gbq]: https://github.com/pandas/pandas#read_gbq
[pd:_join]: https://github.com/pandas/pandas#_join
[pd:_np_version_under1p8]: https://github.com/pandas/pandas#_np_version_under1p8
[pd:index]: https://github.com/pandas/pandas#index
[pd:__name__]: https://github.com/pandas/pandas#__name__
[pd:__spec__]: https://github.com/pandas/pandas#__spec__
[pd:SparseArray]: https://github.com/pandas/pandas#SparseArray
[pd:read_excel]: https://github.com/pandas/pandas#read_excel
[pd:lib]: https://github.com/pandas/pandas#lib
[pd:Timedelta]: https://github.com/pandas/pandas#Timedelta
[pd:DataFrame]: https://github.com/pandas/pandas#DataFrame
[pd:lreshape]: https://github.com/pandas/pandas#lreshape
[pd:read_json]: https://github.com/pandas/pandas#read_json
[pd:read_sas]: https://github.com/pandas/pandas#read_sas
[pd:compat]: https://github.com/pandas/pandas#compat
[pd:wide_to_long]: https://github.com/pandas/pandas#wide_to_long
[pd:Term]: https://github.com/pandas/pandas#Term
[pd:ewma]: https://github.com/pandas/pandas#ewma
[pd:rolling_var]: https://github.com/pandas/pandas#rolling_var
[pd:io]: https://github.com/pandas/pandas#io
[pd:_sparse]: https://github.com/pandas/pandas#_sparse
[pd:pivot_table]: https://github.com/pandas/pandas#pivot_table
[pd:read_msgpack]: https://github.com/pandas/pandas#read_msgpack
[pd:HDFStore]: https://github.com/pandas/pandas#HDFStore
[pd:read_sql]: https://github.com/pandas/pandas#read_sql
[pd:_np_version_under1p11]: https://github.com/pandas/pandas#_np_version_under1p11
[pd:expanding_kurt]: https://github.com/pandas/pandas#expanding_kurt
[pd:__cached__]: https://github.com/pandas/pandas#__cached__
[pd:read_pickle]: https://github.com/pandas/pandas#read_pickle
[pd:rolling_count]: https://github.com/pandas/pandas#rolling_count
[pd:expanding_skew]: https://github.com/pandas/pandas#expanding_skew
[pd:rolling_cov]: https://github.com/pandas/pandas#rolling_cov
[pd:expanding_cov]: https://github.com/pandas/pandas#expanding_cov
[pd:expanding_median]: https://github.com/pandas/pandas#expanding_median
[pd:_np_version_under1p12]: https://github.com/pandas/pandas#_np_version_under1p12
[pd:SparseList]: https://github.com/pandas/pandas#SparseList
[pd:concat]: https://github.com/pandas/pandas#concat
[pd:match]: https://github.com/pandas/pandas#match
[pd:pivot]: https://github.com/pandas/pandas#pivot
[pd:get_store]: https://github.com/pandas/pandas#get_store
[pd:rolling_mean]: https://github.com/pandas/pandas#rolling_mean
[pd:infer_freq]: https://github.com/pandas/pandas#infer_freq
[pd:__path__]: https://github.com/pandas/pandas#__path__
[pd:merge_ordered]: https://github.com/pandas/pandas#merge_ordered
[pd:timedelta_range]: https://github.com/pandas/pandas#timedelta_range
[pd:describe_option]: https://github.com/pandas/pandas#describe_option
[pd:melt]: https://github.com/pandas/pandas#melt
[pd:merge]: https://github.com/pandas/pandas#merge
[pd:groupby]: https://github.com/pandas/pandas#groupby
[pd:read_hdf]: https://github.com/pandas/pandas#read_hdf
[pd:__file__]: https://github.com/pandas/pandas#__file__
[pd:notnull]: https://github.com/pandas/pandas#notnull
[pd:Timestamp]: https://github.com/pandas/pandas#Timestamp
[pd:Period]: https://github.com/pandas/pandas#Period
[pd:algos]: https://github.com/pandas/pandas#algos
[pd:TimeSeries]: https://github.com/pandas/pandas#TimeSeries
[pd:_np_version_under1p9]: https://github.com/pandas/pandas#_np_version_under1p9
[pd:ewmvar]: https://github.com/pandas/pandas#ewmvar
[pd:Categorical]: https://github.com/pandas/pandas#Categorical
[pd:DateOffset]: https://github.com/pandas/pandas#DateOffset
[pd:types]: https://github.com/pandas/pandas#types
[pd:_window]: https://github.com/pandas/pandas#_window
[pd:datetools]: https://github.com/pandas/pandas#datetools
[pd:unique]: https://github.com/pandas/pandas#unique
[pd:pandas]: https://github.com/pandas/pandas#pandas
[pd:isnull]: https://github.com/pandas/pandas#isnull
[pd:expanding_sum]: https://github.com/pandas/pandas#expanding_sum
[pd:to_pickle]: https://github.com/pandas/pandas#to_pickle
[pd:Panel]: https://github.com/pandas/pandas#Panel
[pd:datetime]: https://github.com/pandas/pandas#datetime
[pd:util]: https://github.com/pandas/pandas#util
[pd:rolling_sum]: https://github.com/pandas/pandas#rolling_sum
[pd:msgpack]: https://github.com/pandas/pandas#msgpack
[pd:json]: https://github.com/pandas/pandas#json
[pd:cut]: https://github.com/pandas/pandas#cut
[pd:qcut]: https://github.com/pandas/pandas#qcut
[pd:__version__]: https://github.com/pandas/pandas#__version__
[pd:computation]: https://github.com/pandas/pandas#computation
[pd:NaT]: https://github.com/pandas/pandas#NaT
[pd:pnow]: https://github.com/pandas/pandas#pnow
[pd:stats]: https://github.com/pandas/pandas#stats
[pd:WidePanel]: https://github.com/pandas/pandas#WidePanel
[pd:read_sql_table]: https://github.com/pandas/pandas#read_sql_table
[pd:Index]: https://github.com/pandas/pandas#Index
[pd:PeriodIndex]: https://github.com/pandas/pandas#PeriodIndex
[pd:ewmstd]: https://github.com/pandas/pandas#ewmstd
[pd:tools]: https://github.com/pandas/pandas#tools
[pd:expanding_apply]: https://github.com/pandas/pandas#expanding_apply
[pd:rolling_quantile]: https://github.com/pandas/pandas#rolling_quantile
[pd:value_counts]: https://github.com/pandas/pandas#value_counts
[pd:_testing]: https://github.com/pandas/pandas#_testing
[pd:formats]: https://github.com/pandas/pandas#formats
[pd:to_numeric]: https://github.com/pandas/pandas#to_numeric
[pd:option_context]: https://github.com/pandas/pandas#option_context
[pd:crosstab]: https://github.com/pandas/pandas#crosstab
[pd:api]: https://github.com/pandas/pandas#api
[pd:expanding_var]: https://github.com/pandas/pandas#expanding_var
[pd:expanding_min]: https://github.com/pandas/pandas#expanding_min
[pd:read_fwf]: https://github.com/pandas/pandas#read_fwf
[pd:ewmvol]: https://github.com/pandas/pandas#ewmvol
[pd:IndexSlice]: https://github.com/pandas/pandas#IndexSlice
[pd:to_timedelta]: https://github.com/pandas/pandas#to_timedelta
[pd:__loader__]: https://github.com/pandas/pandas#__loader__
[pd:expanding_mean]: https://github.com/pandas/pandas#expanding_mean
[pd:read_table]: https://github.com/pandas/pandas#read_table
[pd:parser]: https://github.com/pandas/pandas#parser
[pd:eval]: https://github.com/pandas/pandas#eval
[pd:__package__]: https://github.com/pandas/pandas#__package__
[pd:rolling_std]: https://github.com/pandas/pandas#rolling_std
[pd:rolling_min]: https://github.com/pandas/pandas#rolling_min
[pd:read_csv]: https://github.com/pandas/pandas#read_csv
[pd:offsets]: https://github.com/pandas/pandas#offsets
[pd:info]: https://github.com/pandas/pandas#info
[pd:hashtable]: https://github.com/pandas/pandas#hashtable
[pd:Expr]: https://github.com/pandas/pandas#Expr
[pd:tslib]: https://github.com/pandas/pandas#tslib
[pd:options]: https://github.com/pandas/pandas#options
[pd:date_range]: https://github.com/pandas/pandas#date_range
[pd:expanding_std]: https://github.com/pandas/pandas#expanding_std
[pd:period_range]: https://github.com/pandas/pandas#period_range
[pd:expanding_count]: https://github.com/pandas/pandas#expanding_count
[pd:np]: https://github.com/pandas/pandas#np
[pd:ExcelWriter]: https://github.com/pandas/pandas#ExcelWriter
[pd:sparse]: https://github.com/pandas/pandas#sparse
[pd:read_clipboard]: https://github.com/pandas/pandas#read_clipboard
[pd:TimedeltaIndex]: https://github.com/pandas/pandas#TimedeltaIndex
[pd:merge_asof]: https://github.com/pandas/pandas#merge_asof
[pd:__builtins__]: https://github.com/pandas/pandas#__builtins__
[pd:indexes]: https://github.com/pandas/pandas#indexes
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
      <th>kPz5KNKIPm</th>
      <td>-0.333185</td>
      <td>0.008006</td>
      <td>0.116703</td>
      <td>-0.043573</td>
    </tr>
    <tr>
      <th>8Yju66u21A</th>
      <td>1.911384</td>
      <td>1.846572</td>
      <td>-0.159875</td>
      <td>-0.702220</td>
    </tr>
    <tr>
      <th>3Kv009AezS</th>
      <td>-0.542921</td>
      <td>0.401224</td>
      <td>1.442336</td>
      <td>-0.112092</td>
    </tr>
    <tr>
      <th>XCGSyRGB4W</th>
      <td>-0.210745</td>
      <td>-0.145298</td>
      <td>0.791950</td>
      <td>0.077314</td>
    </tr>
    <tr>
      <th>8ukSYuhCVV</th>
      <td>0.305186</td>
      <td>-1.466496</td>
      <td>-0.286745</td>
      <td>-0.300308</td>
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
      <td>0.050096</td>
      <td>-0.197880</td>
      <td>-0.053030</td>
      <td>-0.320474</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.912821</td>
      <td>1.048938</td>
      <td>0.875320</td>
      <td>1.106429</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-1.527188</td>
      <td>-2.143377</td>
      <td>-2.718607</td>
      <td>-2.609820</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.537088</td>
      <td>-1.194501</td>
      <td>-0.283396</td>
      <td>-0.747590</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-0.004867</td>
      <td>-0.073056</td>
      <td>0.035302</td>
      <td>-0.350338</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.448884</td>
      <td>0.331297</td>
      <td>0.516889</td>
      <td>0.309658</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.911384</td>
      <td>1.983712</td>
      <td>1.442336</td>
      <td>2.808144</td>
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
    [NbConvertApp] Writing 31880 bytes to readme.md



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
       

[pd:_version]: https://github.com/pandas/pandas#_version

[pd:expanding_quantile]: https://github.com/pandas/pandas#expanding_quantile

[pd:__doc__]: https://github.com/pandas/pandas#__doc__

[pd:ewmcov]: https://github.com/pandas/pandas#ewmcov

[pd:factorize]: https://github.com/pandas/pandas#factorize

[pd:MultiIndex]: https://github.com/pandas/pandas#MultiIndex

[pd:fama_macbeth]: https://github.com/pandas/pandas#fama_macbeth

[pd:core]: https://github.com/pandas/pandas#core

[pd:RangeIndex]: https://github.com/pandas/pandas#RangeIndex

[pd:read_sql_query]: https://github.com/pandas/pandas#read_sql_query

[pd:set_option]: https://github.com/pandas/pandas#set_option

[pd:Panel4D]: https://github.com/pandas/pandas#Panel4D

[pd:tseries]: https://github.com/pandas/pandas#tseries

[pd:show_versions]: https://github.com/pandas/pandas#show_versions

[pd:ExcelFile]: https://github.com/pandas/pandas#ExcelFile

[pd:plot_params]: https://github.com/pandas/pandas#plot_params

[pd:Float64Index]: https://github.com/pandas/pandas#Float64Index

[pd:rolling_kurt]: https://github.com/pandas/pandas#rolling_kurt

[pd:DatetimeIndex]: https://github.com/pandas/pandas#DatetimeIndex

[pd:rolling_max]: https://github.com/pandas/pandas#rolling_max

[pd:reset_option]: https://github.com/pandas/pandas#reset_option

[pd:SparseDataFrame]: https://github.com/pandas/pandas#SparseDataFrame

[pd:bdate_range]: https://github.com/pandas/pandas#bdate_range

[pd:rolling_median]: https://github.com/pandas/pandas#rolling_median

[pd:__docformat__]: https://github.com/pandas/pandas#__docformat__

[pd:rolling_window]: https://github.com/pandas/pandas#rolling_window

[pd:expanding_max]: https://github.com/pandas/pandas#expanding_max

[pd:to_datetime]: https://github.com/pandas/pandas#to_datetime

[pd:ewmcorr]: https://github.com/pandas/pandas#ewmcorr

[pd:Series]: https://github.com/pandas/pandas#Series

[pd:expanding_corr]: https://github.com/pandas/pandas#expanding_corr

[pd:SparseSeries]: https://github.com/pandas/pandas#SparseSeries

[pd:Int64Index]: https://github.com/pandas/pandas#Int64Index

[pd:Grouper]: https://github.com/pandas/pandas#Grouper

[pd:rolling_corr]: https://github.com/pandas/pandas#rolling_corr

[pd:to_msgpack]: https://github.com/pandas/pandas#to_msgpack

[pd:test]: https://github.com/pandas/pandas#test

[pd:get_option]: https://github.com/pandas/pandas#get_option

[pd:read_html]: https://github.com/pandas/pandas#read_html

[pd:read_stata]: https://github.com/pandas/pandas#read_stata

[pd:SparseTimeSeries]: https://github.com/pandas/pandas#SparseTimeSeries

[pd:CategoricalIndex]: https://github.com/pandas/pandas#CategoricalIndex

[pd:ols]: https://github.com/pandas/pandas#ols

[pd:get_dummies]: https://github.com/pandas/pandas#get_dummies

[pd:set_eng_float_format]: https://github.com/pandas/pandas#set_eng_float_format

[pd:rolling_skew]: https://github.com/pandas/pandas#rolling_skew

[pd:scatter_matrix]: https://github.com/pandas/pandas#scatter_matrix

[pd:ordered_merge]: https://github.com/pandas/pandas#ordered_merge

[pd:_np_version_under1p10]: https://github.com/pandas/pandas#_np_version_under1p10

[pd:rolling_apply]: https://github.com/pandas/pandas#rolling_apply

[pd:TimeGrouper]: https://github.com/pandas/pandas#TimeGrouper

[pd:_period]: https://github.com/pandas/pandas#_period

[pd:read_gbq]: https://github.com/pandas/pandas#read_gbq

[pd:_join]: https://github.com/pandas/pandas#_join

[pd:_np_version_under1p8]: https://github.com/pandas/pandas#_np_version_under1p8

[pd:index]: https://github.com/pandas/pandas#index

[pd:__name__]: https://github.com/pandas/pandas#__name__

[pd:__spec__]: https://github.com/pandas/pandas#__spec__

[pd:SparseArray]: https://github.com/pandas/pandas#SparseArray

[pd:read_excel]: https://github.com/pandas/pandas#read_excel

[pd:lib]: https://github.com/pandas/pandas#lib

[pd:Timedelta]: https://github.com/pandas/pandas#Timedelta

[pd:DataFrame]: https://github.com/pandas/pandas#DataFrame

[pd:lreshape]: https://github.com/pandas/pandas#lreshape

[pd:read_json]: https://github.com/pandas/pandas#read_json

[pd:read_sas]: https://github.com/pandas/pandas#read_sas

[pd:compat]: https://github.com/pandas/pandas#compat

[pd:wide_to_long]: https://github.com/pandas/pandas#wide_to_long

[pd:Term]: https://github.com/pandas/pandas#Term

[pd:ewma]: https://github.com/pandas/pandas#ewma

[pd:rolling_var]: https://github.com/pandas/pandas#rolling_var

[pd:io]: https://github.com/pandas/pandas#io

[pd:_sparse]: https://github.com/pandas/pandas#_sparse

[pd:pivot_table]: https://github.com/pandas/pandas#pivot_table

[pd:read_msgpack]: https://github.com/pandas/pandas#read_msgpack

[pd:HDFStore]: https://github.com/pandas/pandas#HDFStore

[pd:read_sql]: https://github.com/pandas/pandas#read_sql

[pd:_np_version_under1p11]: https://github.com/pandas/pandas#_np_version_under1p11

[pd:expanding_kurt]: https://github.com/pandas/pandas#expanding_kurt

[pd:__cached__]: https://github.com/pandas/pandas#__cached__

[pd:read_pickle]: https://github.com/pandas/pandas#read_pickle

[pd:rolling_count]: https://github.com/pandas/pandas#rolling_count

[pd:expanding_skew]: https://github.com/pandas/pandas#expanding_skew

[pd:rolling_cov]: https://github.com/pandas/pandas#rolling_cov

[pd:expanding_cov]: https://github.com/pandas/pandas#expanding_cov

[pd:expanding_median]: https://github.com/pandas/pandas#expanding_median

[pd:_np_version_under1p12]: https://github.com/pandas/pandas#_np_version_under1p12

[pd:SparseList]: https://github.com/pandas/pandas#SparseList

[pd:concat]: https://github.com/pandas/pandas#concat

[pd:match]: https://github.com/pandas/pandas#match

[pd:pivot]: https://github.com/pandas/pandas#pivot

[pd:get_store]: https://github.com/pandas/pandas#get_store

[pd:rolling_mean]: https://github.com/pandas/pandas#rolling_mean

[pd:infer_freq]: https://github.com/pandas/pandas#infer_freq

[pd:__path__]: https://github.com/pandas/pandas#__path__

[pd:merge_ordered]: https://github.com/pandas/pandas#merge_ordered

[pd:timedelta_range]: https://github.com/pandas/pandas#timedelta_range

[pd:describe_option]: https://github.com/pandas/pandas#describe_option

[pd:melt]: https://github.com/pandas/pandas#melt

[pd:merge]: https://github.com/pandas/pandas#merge

[pd:groupby]: https://github.com/pandas/pandas#groupby

[pd:read_hdf]: https://github.com/pandas/pandas#read_hdf

[pd:__file__]: https://github.com/pandas/pandas#__file__

[pd:notnull]: https://github.com/pandas/pandas#notnull

[pd:Timestamp]: https://github.com/pandas/pandas#Timestamp

[pd:Period]: https://github.com/pandas/pandas#Period

[pd:algos]: https://github.com/pandas/pandas#algos

[pd:TimeSeries]: https://github.com/pandas/pandas#TimeSeries

[pd:_np_version_under1p9]: https://github.com/pandas/pandas#_np_version_under1p9

[pd:ewmvar]: https://github.com/pandas/pandas#ewmvar

[pd:Categorical]: https://github.com/pandas/pandas#Categorical

[pd:DateOffset]: https://github.com/pandas/pandas#DateOffset

[pd:types]: https://github.com/pandas/pandas#types

[pd:_window]: https://github.com/pandas/pandas#_window

[pd:datetools]: https://github.com/pandas/pandas#datetools

[pd:unique]: https://github.com/pandas/pandas#unique

[pd:pandas]: https://github.com/pandas/pandas#pandas

[pd:isnull]: https://github.com/pandas/pandas#isnull

[pd:expanding_sum]: https://github.com/pandas/pandas#expanding_sum

[pd:to_pickle]: https://github.com/pandas/pandas#to_pickle

[pd:Panel]: https://github.com/pandas/pandas#Panel

[pd:datetime]: https://github.com/pandas/pandas#datetime

[pd:util]: https://github.com/pandas/pandas#util

[pd:rolling_sum]: https://github.com/pandas/pandas#rolling_sum

[pd:msgpack]: https://github.com/pandas/pandas#msgpack

[pd:json]: https://github.com/pandas/pandas#json

[pd:cut]: https://github.com/pandas/pandas#cut

[pd:qcut]: https://github.com/pandas/pandas#qcut

[pd:__version__]: https://github.com/pandas/pandas#__version__

[pd:computation]: https://github.com/pandas/pandas#computation

[pd:NaT]: https://github.com/pandas/pandas#NaT

[pd:pnow]: https://github.com/pandas/pandas#pnow

[pd:stats]: https://github.com/pandas/pandas#stats

[pd:WidePanel]: https://github.com/pandas/pandas#WidePanel

[pd:read_sql_table]: https://github.com/pandas/pandas#read_sql_table

[pd:Index]: https://github.com/pandas/pandas#Index

[pd:PeriodIndex]: https://github.com/pandas/pandas#PeriodIndex

[pd:ewmstd]: https://github.com/pandas/pandas#ewmstd

[pd:tools]: https://github.com/pandas/pandas#tools

[pd:expanding_apply]: https://github.com/pandas/pandas#expanding_apply

[pd:rolling_quantile]: https://github.com/pandas/pandas#rolling_quantile

[pd:value_counts]: https://github.com/pandas/pandas#value_counts

[pd:_testing]: https://github.com/pandas/pandas#_testing

[pd:formats]: https://github.com/pandas/pandas#formats

[pd:to_numeric]: https://github.com/pandas/pandas#to_numeric

[pd:option_context]: https://github.com/pandas/pandas#option_context

[pd:crosstab]: https://github.com/pandas/pandas#crosstab

[pd:api]: https://github.com/pandas/pandas#api

[pd:expanding_var]: https://github.com/pandas/pandas#expanding_var

[pd:expanding_min]: https://github.com/pandas/pandas#expanding_min

[pd:read_fwf]: https://github.com/pandas/pandas#read_fwf

[pd:ewmvol]: https://github.com/pandas/pandas#ewmvol

[pd:IndexSlice]: https://github.com/pandas/pandas#IndexSlice

[pd:to_timedelta]: https://github.com/pandas/pandas#to_timedelta

[pd:__loader__]: https://github.com/pandas/pandas#__loader__

[pd:expanding_mean]: https://github.com/pandas/pandas#expanding_mean

[pd:read_table]: https://github.com/pandas/pandas#read_table

[pd:parser]: https://github.com/pandas/pandas#parser

[pd:eval]: https://github.com/pandas/pandas#eval

[pd:__package__]: https://github.com/pandas/pandas#__package__

[pd:rolling_std]: https://github.com/pandas/pandas#rolling_std

[pd:rolling_min]: https://github.com/pandas/pandas#rolling_min

[pd:read_csv]: https://github.com/pandas/pandas#read_csv

[pd:offsets]: https://github.com/pandas/pandas#offsets

[pd:info]: https://github.com/pandas/pandas#info

[pd:hashtable]: https://github.com/pandas/pandas#hashtable

[pd:Expr]: https://github.com/pandas/pandas#Expr

[pd:tslib]: https://github.com/pandas/pandas#tslib

[pd:options]: https://github.com/pandas/pandas#options

[pd:date_range]: https://github.com/pandas/pandas#date_range

[pd:expanding_std]: https://github.com/pandas/pandas#expanding_std

[pd:period_range]: https://github.com/pandas/pandas#period_range

[pd:expanding_count]: https://github.com/pandas/pandas#expanding_count

[pd:np]: https://github.com/pandas/pandas#np

[pd:ExcelWriter]: https://github.com/pandas/pandas#ExcelWriter

[pd:sparse]: https://github.com/pandas/pandas#sparse

[pd:read_clipboard]: https://github.com/pandas/pandas#read_clipboard

[pd:TimedeltaIndex]: https://github.com/pandas/pandas#TimedeltaIndex

[pd:merge_asof]: https://github.com/pandas/pandas#merge_asof

[pd:__builtins__]: https://github.com/pandas/pandas#__builtins__

[pd:indexes]: https://github.com/pandas/pandas#indexes

Now you can talk about [pd:DataFrame][], [pd:io][] or [pd:Series][].

