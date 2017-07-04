
# __literacy__ - Computable documents in natural language.

> [Literate programming](roxygen.org/knuth-literate-programming.pdf) notebooks in 𝗠arkd⬇wn
and py🐍hon.

---

<code>pip install git+https://github.com/tonyfast/literacy</code>

# Literate programming mode

Activate the `literacy` extension.


```python
        %load_ext literacy
```


```python
__Now__, all cells in the notebook accept __Markdown__ as syntax. Each code fragment is evaluated as an individual cell
and every cell will display a markdown copy of itself before the output. 

> There is no code in this cell, the execution number next to <code>In</code> will _not_ increment.
```


__Now__, all cells in the notebook accept __Markdown__ as syntax. Each code fragment is evaluated as an individual cell
and every cell will display a markdown copy of itself before the output. 

> There is no code in this cell, the execution number next to <code>In</code> will _not_ increment.



```python
## Writing code

### Indented code

The cell below looks like normal python code, 
```


## Writing code

### Indented code

The cell below looks like normal python code, 



```python
        foo = 42
        print(foo)
```


        foo = 42
        print(foo)


    42



```python
*the indent triggers code execution*.
```


*the indent triggers code execution*.



```python
Of course, code and plain text can be mixed
    
        print("This evaluated to: {}".format(foo*10))
        
> There are more ways to write code!
```


Of course, code and plain text can be mixed
    
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
## Templates.

All code blocks are __jinja2__ templates.
```


## Templates.

All code blocks are __jinja2__ templates.



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

###### Remove Templates
        
        if __name__ == '__main__': 
            %load_ext literacy
```


##### Unload literacy anytime 

        if __name__ == '__main__': 
            %unload_ext literacy

###### Remove Templates
        
        if __name__ == '__main__': 
            %load_ext literacy



```python
## Data Science with `import pandas as pd`
```


## Data Science with `import pandas as pd`



```python
This tool was designed to tell stories about real data.  Since every code block is just python,
`df=__import__('pandas').util.testing.makeDataFrame();df.head()` to make a __[pd:DataFrame][]__. 

{% for key in pd.__dict__ %}
[pd:{{ key }}]: https://github.com/pandas/pandas#{{ key }}{% endfor %}
```


This tool was designed to tell stories about real data.  Since every code block is just python,
`df=__import__('pandas').util.testing.makeDataFrame();df.head()` to make a __[pd:DataFrame][]__. 


[pd:__file__]: https://github.com/pandas/pandas#__file__
[pd:ewmcov]: https://github.com/pandas/pandas#ewmcov
[pd:expanding_var]: https://github.com/pandas/pandas#expanding_var
[pd:api]: https://github.com/pandas/pandas#api
[pd:rolling_window]: https://github.com/pandas/pandas#rolling_window
[pd:merge_ordered]: https://github.com/pandas/pandas#merge_ordered
[pd:TimedeltaIndex]: https://github.com/pandas/pandas#TimedeltaIndex
[pd:scatter_matrix]: https://github.com/pandas/pandas#scatter_matrix
[pd:WidePanel]: https://github.com/pandas/pandas#WidePanel
[pd:sparse]: https://github.com/pandas/pandas#sparse
[pd:read_html]: https://github.com/pandas/pandas#read_html
[pd:expanding_quantile]: https://github.com/pandas/pandas#expanding_quantile
[pd:read_sql]: https://github.com/pandas/pandas#read_sql
[pd:DatetimeIndex]: https://github.com/pandas/pandas#DatetimeIndex
[pd:Index]: https://github.com/pandas/pandas#Index
[pd:__path__]: https://github.com/pandas/pandas#__path__
[pd:datetime]: https://github.com/pandas/pandas#datetime
[pd:read_excel]: https://github.com/pandas/pandas#read_excel
[pd:__name__]: https://github.com/pandas/pandas#__name__
[pd:core]: https://github.com/pandas/pandas#core
[pd:plot_params]: https://github.com/pandas/pandas#plot_params
[pd:ols]: https://github.com/pandas/pandas#ols
[pd:_period]: https://github.com/pandas/pandas#_period
[pd:ewmvar]: https://github.com/pandas/pandas#ewmvar
[pd:tseries]: https://github.com/pandas/pandas#tseries
[pd:Categorical]: https://github.com/pandas/pandas#Categorical
[pd:expanding_apply]: https://github.com/pandas/pandas#expanding_apply
[pd:msgpack]: https://github.com/pandas/pandas#msgpack
[pd:read_csv]: https://github.com/pandas/pandas#read_csv
[pd:ExcelFile]: https://github.com/pandas/pandas#ExcelFile
[pd:rolling_quantile]: https://github.com/pandas/pandas#rolling_quantile
[pd:rolling_std]: https://github.com/pandas/pandas#rolling_std
[pd:merge_asof]: https://github.com/pandas/pandas#merge_asof
[pd:expanding_min]: https://github.com/pandas/pandas#expanding_min
[pd:_np_version_under1p9]: https://github.com/pandas/pandas#_np_version_under1p9
[pd:Timedelta]: https://github.com/pandas/pandas#Timedelta
[pd:pandas]: https://github.com/pandas/pandas#pandas
[pd:rolling_skew]: https://github.com/pandas/pandas#rolling_skew
[pd:index]: https://github.com/pandas/pandas#index
[pd:rolling_max]: https://github.com/pandas/pandas#rolling_max
[pd:_window]: https://github.com/pandas/pandas#_window
[pd:DataFrame]: https://github.com/pandas/pandas#DataFrame
[pd:expanding_std]: https://github.com/pandas/pandas#expanding_std
[pd:Period]: https://github.com/pandas/pandas#Period
[pd:expanding_count]: https://github.com/pandas/pandas#expanding_count
[pd:parser]: https://github.com/pandas/pandas#parser
[pd:IndexSlice]: https://github.com/pandas/pandas#IndexSlice
[pd:rolling_kurt]: https://github.com/pandas/pandas#rolling_kurt
[pd:__spec__]: https://github.com/pandas/pandas#__spec__
[pd:timedelta_range]: https://github.com/pandas/pandas#timedelta_range
[pd:ewma]: https://github.com/pandas/pandas#ewma
[pd:MultiIndex]: https://github.com/pandas/pandas#MultiIndex
[pd:read_fwf]: https://github.com/pandas/pandas#read_fwf
[pd:rolling_median]: https://github.com/pandas/pandas#rolling_median
[pd:rolling_var]: https://github.com/pandas/pandas#rolling_var
[pd:computation]: https://github.com/pandas/pandas#computation
[pd:rolling_count]: https://github.com/pandas/pandas#rolling_count
[pd:json]: https://github.com/pandas/pandas#json
[pd:Expr]: https://github.com/pandas/pandas#Expr
[pd:RangeIndex]: https://github.com/pandas/pandas#RangeIndex
[pd:isnull]: https://github.com/pandas/pandas#isnull
[pd:DateOffset]: https://github.com/pandas/pandas#DateOffset
[pd:read_hdf]: https://github.com/pandas/pandas#read_hdf
[pd:_sparse]: https://github.com/pandas/pandas#_sparse
[pd:to_msgpack]: https://github.com/pandas/pandas#to_msgpack
[pd:Panel]: https://github.com/pandas/pandas#Panel
[pd:cut]: https://github.com/pandas/pandas#cut
[pd:read_table]: https://github.com/pandas/pandas#read_table
[pd:merge]: https://github.com/pandas/pandas#merge
[pd:_np_version_under1p10]: https://github.com/pandas/pandas#_np_version_under1p10
[pd:rolling_apply]: https://github.com/pandas/pandas#rolling_apply
[pd:Panel4D]: https://github.com/pandas/pandas#Panel4D
[pd:read_gbq]: https://github.com/pandas/pandas#read_gbq
[pd:rolling_mean]: https://github.com/pandas/pandas#rolling_mean
[pd:fama_macbeth]: https://github.com/pandas/pandas#fama_macbeth
[pd:wide_to_long]: https://github.com/pandas/pandas#wide_to_long
[pd:Term]: https://github.com/pandas/pandas#Term
[pd:to_datetime]: https://github.com/pandas/pandas#to_datetime
[pd:notnull]: https://github.com/pandas/pandas#notnull
[pd:read_json]: https://github.com/pandas/pandas#read_json
[pd:read_pickle]: https://github.com/pandas/pandas#read_pickle
[pd:util]: https://github.com/pandas/pandas#util
[pd:groupby]: https://github.com/pandas/pandas#groupby
[pd:factorize]: https://github.com/pandas/pandas#factorize
[pd:_join]: https://github.com/pandas/pandas#_join
[pd:read_sql_table]: https://github.com/pandas/pandas#read_sql_table
[pd:NaT]: https://github.com/pandas/pandas#NaT
[pd:set_option]: https://github.com/pandas/pandas#set_option
[pd:period_range]: https://github.com/pandas/pandas#period_range
[pd:Grouper]: https://github.com/pandas/pandas#Grouper
[pd:SparseArray]: https://github.com/pandas/pandas#SparseArray
[pd:_version]: https://github.com/pandas/pandas#_version
[pd:Float64Index]: https://github.com/pandas/pandas#Float64Index
[pd:ordered_merge]: https://github.com/pandas/pandas#ordered_merge
[pd:reset_option]: https://github.com/pandas/pandas#reset_option
[pd:__doc__]: https://github.com/pandas/pandas#__doc__
[pd:pnow]: https://github.com/pandas/pandas#pnow
[pd:concat]: https://github.com/pandas/pandas#concat
[pd:pivot]: https://github.com/pandas/pandas#pivot
[pd:options]: https://github.com/pandas/pandas#options
[pd:expanding_max]: https://github.com/pandas/pandas#expanding_max
[pd:TimeSeries]: https://github.com/pandas/pandas#TimeSeries
[pd:to_timedelta]: https://github.com/pandas/pandas#to_timedelta
[pd:__builtins__]: https://github.com/pandas/pandas#__builtins__
[pd:types]: https://github.com/pandas/pandas#types
[pd:HDFStore]: https://github.com/pandas/pandas#HDFStore
[pd:to_numeric]: https://github.com/pandas/pandas#to_numeric
[pd:read_sas]: https://github.com/pandas/pandas#read_sas
[pd:CategoricalIndex]: https://github.com/pandas/pandas#CategoricalIndex
[pd:lreshape]: https://github.com/pandas/pandas#lreshape
[pd:read_msgpack]: https://github.com/pandas/pandas#read_msgpack
[pd:lib]: https://github.com/pandas/pandas#lib
[pd:tools]: https://github.com/pandas/pandas#tools
[pd:qcut]: https://github.com/pandas/pandas#qcut
[pd:indexes]: https://github.com/pandas/pandas#indexes
[pd:__loader__]: https://github.com/pandas/pandas#__loader__
[pd:set_eng_float_format]: https://github.com/pandas/pandas#set_eng_float_format
[pd:melt]: https://github.com/pandas/pandas#melt
[pd:rolling_min]: https://github.com/pandas/pandas#rolling_min
[pd:rolling_corr]: https://github.com/pandas/pandas#rolling_corr
[pd:datetools]: https://github.com/pandas/pandas#datetools
[pd:ewmvol]: https://github.com/pandas/pandas#ewmvol
[pd:get_dummies]: https://github.com/pandas/pandas#get_dummies
[pd:ewmcorr]: https://github.com/pandas/pandas#ewmcorr
[pd:pivot_table]: https://github.com/pandas/pandas#pivot_table
[pd:TimeGrouper]: https://github.com/pandas/pandas#TimeGrouper
[pd:infer_freq]: https://github.com/pandas/pandas#infer_freq
[pd:np]: https://github.com/pandas/pandas#np
[pd:match]: https://github.com/pandas/pandas#match
[pd:_np_version_under1p8]: https://github.com/pandas/pandas#_np_version_under1p8
[pd:algos]: https://github.com/pandas/pandas#algos
[pd:read_sql_query]: https://github.com/pandas/pandas#read_sql_query
[pd:_np_version_under1p12]: https://github.com/pandas/pandas#_np_version_under1p12
[pd:expanding_skew]: https://github.com/pandas/pandas#expanding_skew
[pd:read_stata]: https://github.com/pandas/pandas#read_stata
[pd:SparseTimeSeries]: https://github.com/pandas/pandas#SparseTimeSeries
[pd:ewmstd]: https://github.com/pandas/pandas#ewmstd
[pd:tslib]: https://github.com/pandas/pandas#tslib
[pd:option_context]: https://github.com/pandas/pandas#option_context
[pd:compat]: https://github.com/pandas/pandas#compat
[pd:expanding_sum]: https://github.com/pandas/pandas#expanding_sum
[pd:test]: https://github.com/pandas/pandas#test
[pd:formats]: https://github.com/pandas/pandas#formats
[pd:unique]: https://github.com/pandas/pandas#unique
[pd:Timestamp]: https://github.com/pandas/pandas#Timestamp
[pd:show_versions]: https://github.com/pandas/pandas#show_versions
[pd:read_clipboard]: https://github.com/pandas/pandas#read_clipboard
[pd:date_range]: https://github.com/pandas/pandas#date_range
[pd:eval]: https://github.com/pandas/pandas#eval
[pd:bdate_range]: https://github.com/pandas/pandas#bdate_range
[pd:SparseDataFrame]: https://github.com/pandas/pandas#SparseDataFrame
[pd:__cached__]: https://github.com/pandas/pandas#__cached__
[pd:io]: https://github.com/pandas/pandas#io
[pd:rolling_sum]: https://github.com/pandas/pandas#rolling_sum
[pd:_np_version_under1p11]: https://github.com/pandas/pandas#_np_version_under1p11
[pd:describe_option]: https://github.com/pandas/pandas#describe_option
[pd:info]: https://github.com/pandas/pandas#info
[pd:expanding_cov]: https://github.com/pandas/pandas#expanding_cov
[pd:Int64Index]: https://github.com/pandas/pandas#Int64Index
[pd:crosstab]: https://github.com/pandas/pandas#crosstab
[pd:SparseList]: https://github.com/pandas/pandas#SparseList
[pd:Series]: https://github.com/pandas/pandas#Series
[pd:PeriodIndex]: https://github.com/pandas/pandas#PeriodIndex
[pd:expanding_corr]: https://github.com/pandas/pandas#expanding_corr
[pd:expanding_median]: https://github.com/pandas/pandas#expanding_median
[pd:expanding_mean]: https://github.com/pandas/pandas#expanding_mean
[pd:rolling_cov]: https://github.com/pandas/pandas#rolling_cov
[pd:SparseSeries]: https://github.com/pandas/pandas#SparseSeries
[pd:__package__]: https://github.com/pandas/pandas#__package__
[pd:get_store]: https://github.com/pandas/pandas#get_store
[pd:value_counts]: https://github.com/pandas/pandas#value_counts
[pd:to_pickle]: https://github.com/pandas/pandas#to_pickle
[pd:offsets]: https://github.com/pandas/pandas#offsets
[pd:ExcelWriter]: https://github.com/pandas/pandas#ExcelWriter
[pd:expanding_kurt]: https://github.com/pandas/pandas#expanding_kurt
[pd:__docformat__]: https://github.com/pandas/pandas#__docformat__
[pd:hashtable]: https://github.com/pandas/pandas#hashtable
[pd:__version__]: https://github.com/pandas/pandas#__version__
[pd:get_option]: https://github.com/pandas/pandas#get_option
[pd:stats]: https://github.com/pandas/pandas#stats
[pd:_testing]: https://github.com/pandas/pandas#_testing





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
      <th>4UgCMiAJby</th>
      <td>-0.508214</td>
      <td>-1.451444</td>
      <td>-1.111655</td>
      <td>0.664659</td>
    </tr>
    <tr>
      <th>rj4RwWbZYf</th>
      <td>-0.278683</td>
      <td>-0.509930</td>
      <td>-1.128114</td>
      <td>1.077029</td>
    </tr>
    <tr>
      <th>6d6wz9lLy1</th>
      <td>-0.366265</td>
      <td>-0.139493</td>
      <td>-3.222612</td>
      <td>-1.146612</td>
    </tr>
    <tr>
      <th>sHKZI7u9lR</th>
      <td>-1.870186</td>
      <td>0.115140</td>
      <td>-0.808415</td>
      <td>-0.997532</td>
    </tr>
    <tr>
      <th>mqpTYkKxAY</th>
      <td>0.741116</td>
      <td>1.213929</td>
      <td>-0.567442</td>
      <td>-0.136123</td>
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
      <td>0.007215</td>
      <td>-0.243799</td>
      <td>-0.069155</td>
      <td>0.026376</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.847602</td>
      <td>0.785083</td>
      <td>1.117431</td>
      <td>0.994496</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-1.870186</td>
      <td>-1.623560</td>
      <td>-3.222612</td>
      <td>-1.356560</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.501670</td>
      <td>-0.819593</td>
      <td>-0.885969</td>
      <td>-0.958074</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.025378</td>
      <td>-0.198241</td>
      <td>0.122801</td>
      <td>-0.012644</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.408453</td>
      <td>0.278132</td>
      <td>0.565007</td>
      <td>0.664504</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.749782</td>
      <td>1.437650</td>
      <td>1.744815</td>
      <td>2.019288</td>
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
    [NbConvertApp] Writing 18187 bytes to readme.md

