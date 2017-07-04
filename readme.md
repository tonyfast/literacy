
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


[pd:merge_ordered]: https://github.com/pandas/pandas#merge_ordered
[pd:compat]: https://github.com/pandas/pandas#compat
[pd:rolling_kurt]: https://github.com/pandas/pandas#rolling_kurt
[pd:match]: https://github.com/pandas/pandas#match
[pd:expanding_sum]: https://github.com/pandas/pandas#expanding_sum
[pd:factorize]: https://github.com/pandas/pandas#factorize
[pd:MultiIndex]: https://github.com/pandas/pandas#MultiIndex
[pd:hashtable]: https://github.com/pandas/pandas#hashtable
[pd:core]: https://github.com/pandas/pandas#core
[pd:tools]: https://github.com/pandas/pandas#tools
[pd:Term]: https://github.com/pandas/pandas#Term
[pd:_testing]: https://github.com/pandas/pandas#_testing
[pd:fama_macbeth]: https://github.com/pandas/pandas#fama_macbeth
[pd:rolling_skew]: https://github.com/pandas/pandas#rolling_skew
[pd:SparseTimeSeries]: https://github.com/pandas/pandas#SparseTimeSeries
[pd:ExcelFile]: https://github.com/pandas/pandas#ExcelFile
[pd:offsets]: https://github.com/pandas/pandas#offsets
[pd:Int64Index]: https://github.com/pandas/pandas#Int64Index
[pd:_np_version_under1p9]: https://github.com/pandas/pandas#_np_version_under1p9
[pd:read_sql]: https://github.com/pandas/pandas#read_sql
[pd:ewmvol]: https://github.com/pandas/pandas#ewmvol
[pd:__file__]: https://github.com/pandas/pandas#__file__
[pd:sparse]: https://github.com/pandas/pandas#sparse
[pd:groupby]: https://github.com/pandas/pandas#groupby
[pd:to_timedelta]: https://github.com/pandas/pandas#to_timedelta
[pd:bdate_range]: https://github.com/pandas/pandas#bdate_range
[pd:Grouper]: https://github.com/pandas/pandas#Grouper
[pd:ols]: https://github.com/pandas/pandas#ols
[pd:tslib]: https://github.com/pandas/pandas#tslib
[pd:read_sql_query]: https://github.com/pandas/pandas#read_sql_query
[pd:_join]: https://github.com/pandas/pandas#_join
[pd:WidePanel]: https://github.com/pandas/pandas#WidePanel
[pd:read_sql_table]: https://github.com/pandas/pandas#read_sql_table
[pd:expanding_kurt]: https://github.com/pandas/pandas#expanding_kurt
[pd:Expr]: https://github.com/pandas/pandas#Expr
[pd:SparseDataFrame]: https://github.com/pandas/pandas#SparseDataFrame
[pd:HDFStore]: https://github.com/pandas/pandas#HDFStore
[pd:timedelta_range]: https://github.com/pandas/pandas#timedelta_range
[pd:_sparse]: https://github.com/pandas/pandas#_sparse
[pd:to_datetime]: https://github.com/pandas/pandas#to_datetime
[pd:rolling_corr]: https://github.com/pandas/pandas#rolling_corr
[pd:lreshape]: https://github.com/pandas/pandas#lreshape
[pd:IndexSlice]: https://github.com/pandas/pandas#IndexSlice
[pd:parser]: https://github.com/pandas/pandas#parser
[pd:rolling_window]: https://github.com/pandas/pandas#rolling_window
[pd:expanding_std]: https://github.com/pandas/pandas#expanding_std
[pd:types]: https://github.com/pandas/pandas#types
[pd:expanding_var]: https://github.com/pandas/pandas#expanding_var
[pd:msgpack]: https://github.com/pandas/pandas#msgpack
[pd:read_excel]: https://github.com/pandas/pandas#read_excel
[pd:value_counts]: https://github.com/pandas/pandas#value_counts
[pd:__builtins__]: https://github.com/pandas/pandas#__builtins__
[pd:wide_to_long]: https://github.com/pandas/pandas#wide_to_long
[pd:NaT]: https://github.com/pandas/pandas#NaT
[pd:Timedelta]: https://github.com/pandas/pandas#Timedelta
[pd:lib]: https://github.com/pandas/pandas#lib
[pd:stats]: https://github.com/pandas/pandas#stats
[pd:_np_version_under1p8]: https://github.com/pandas/pandas#_np_version_under1p8
[pd:rolling_min]: https://github.com/pandas/pandas#rolling_min
[pd:__package__]: https://github.com/pandas/pandas#__package__
[pd:RangeIndex]: https://github.com/pandas/pandas#RangeIndex
[pd:read_html]: https://github.com/pandas/pandas#read_html
[pd:expanding_apply]: https://github.com/pandas/pandas#expanding_apply
[pd:TimeGrouper]: https://github.com/pandas/pandas#TimeGrouper
[pd:to_numeric]: https://github.com/pandas/pandas#to_numeric
[pd:ewma]: https://github.com/pandas/pandas#ewma
[pd:notnull]: https://github.com/pandas/pandas#notnull
[pd:__loader__]: https://github.com/pandas/pandas#__loader__
[pd:get_option]: https://github.com/pandas/pandas#get_option
[pd:melt]: https://github.com/pandas/pandas#melt
[pd:read_stata]: https://github.com/pandas/pandas#read_stata
[pd:crosstab]: https://github.com/pandas/pandas#crosstab
[pd:get_dummies]: https://github.com/pandas/pandas#get_dummies
[pd:_np_version_under1p12]: https://github.com/pandas/pandas#_np_version_under1p12
[pd:expanding_min]: https://github.com/pandas/pandas#expanding_min
[pd:rolling_sum]: https://github.com/pandas/pandas#rolling_sum
[pd:set_eng_float_format]: https://github.com/pandas/pandas#set_eng_float_format
[pd:ewmcov]: https://github.com/pandas/pandas#ewmcov
[pd:expanding_skew]: https://github.com/pandas/pandas#expanding_skew
[pd:__cached__]: https://github.com/pandas/pandas#__cached__
[pd:read_hdf]: https://github.com/pandas/pandas#read_hdf
[pd:np]: https://github.com/pandas/pandas#np
[pd:Index]: https://github.com/pandas/pandas#Index
[pd:read_pickle]: https://github.com/pandas/pandas#read_pickle
[pd:__doc__]: https://github.com/pandas/pandas#__doc__
[pd:rolling_apply]: https://github.com/pandas/pandas#rolling_apply
[pd:read_csv]: https://github.com/pandas/pandas#read_csv
[pd:__path__]: https://github.com/pandas/pandas#__path__
[pd:ordered_merge]: https://github.com/pandas/pandas#ordered_merge
[pd:unique]: https://github.com/pandas/pandas#unique
[pd:SparseList]: https://github.com/pandas/pandas#SparseList
[pd:api]: https://github.com/pandas/pandas#api
[pd:expanding_mean]: https://github.com/pandas/pandas#expanding_mean
[pd:Series]: https://github.com/pandas/pandas#Series
[pd:_period]: https://github.com/pandas/pandas#_period
[pd:Timestamp]: https://github.com/pandas/pandas#Timestamp
[pd:get_store]: https://github.com/pandas/pandas#get_store
[pd:info]: https://github.com/pandas/pandas#info
[pd:__name__]: https://github.com/pandas/pandas#__name__
[pd:pivot_table]: https://github.com/pandas/pandas#pivot_table
[pd:show_versions]: https://github.com/pandas/pandas#show_versions
[pd:merge_asof]: https://github.com/pandas/pandas#merge_asof
[pd:plot_params]: https://github.com/pandas/pandas#plot_params
[pd:ExcelWriter]: https://github.com/pandas/pandas#ExcelWriter
[pd:rolling_mean]: https://github.com/pandas/pandas#rolling_mean
[pd:to_pickle]: https://github.com/pandas/pandas#to_pickle
[pd:Panel4D]: https://github.com/pandas/pandas#Panel4D
[pd:SparseSeries]: https://github.com/pandas/pandas#SparseSeries
[pd:ewmstd]: https://github.com/pandas/pandas#ewmstd
[pd:read_table]: https://github.com/pandas/pandas#read_table
[pd:__docformat__]: https://github.com/pandas/pandas#__docformat__
[pd:__spec__]: https://github.com/pandas/pandas#__spec__
[pd:rolling_count]: https://github.com/pandas/pandas#rolling_count
[pd:tseries]: https://github.com/pandas/pandas#tseries
[pd:date_range]: https://github.com/pandas/pandas#date_range
[pd:to_msgpack]: https://github.com/pandas/pandas#to_msgpack
[pd:option_context]: https://github.com/pandas/pandas#option_context
[pd:util]: https://github.com/pandas/pandas#util
[pd:isnull]: https://github.com/pandas/pandas#isnull
[pd:PeriodIndex]: https://github.com/pandas/pandas#PeriodIndex
[pd:Float64Index]: https://github.com/pandas/pandas#Float64Index
[pd:eval]: https://github.com/pandas/pandas#eval
[pd:reset_option]: https://github.com/pandas/pandas#reset_option
[pd:read_gbq]: https://github.com/pandas/pandas#read_gbq
[pd:index]: https://github.com/pandas/pandas#index
[pd:rolling_std]: https://github.com/pandas/pandas#rolling_std
[pd:qcut]: https://github.com/pandas/pandas#qcut
[pd:indexes]: https://github.com/pandas/pandas#indexes
[pd:rolling_max]: https://github.com/pandas/pandas#rolling_max
[pd:computation]: https://github.com/pandas/pandas#computation
[pd:period_range]: https://github.com/pandas/pandas#period_range
[pd:set_option]: https://github.com/pandas/pandas#set_option
[pd:expanding_median]: https://github.com/pandas/pandas#expanding_median
[pd:pnow]: https://github.com/pandas/pandas#pnow
[pd:merge]: https://github.com/pandas/pandas#merge
[pd:read_msgpack]: https://github.com/pandas/pandas#read_msgpack
[pd:algos]: https://github.com/pandas/pandas#algos
[pd:_np_version_under1p10]: https://github.com/pandas/pandas#_np_version_under1p10
[pd:test]: https://github.com/pandas/pandas#test
[pd:_np_version_under1p11]: https://github.com/pandas/pandas#_np_version_under1p11
[pd:DateOffset]: https://github.com/pandas/pandas#DateOffset
[pd:_window]: https://github.com/pandas/pandas#_window
[pd:Panel]: https://github.com/pandas/pandas#Panel
[pd:formats]: https://github.com/pandas/pandas#formats
[pd:rolling_var]: https://github.com/pandas/pandas#rolling_var
[pd:SparseArray]: https://github.com/pandas/pandas#SparseArray
[pd:infer_freq]: https://github.com/pandas/pandas#infer_freq
[pd:Period]: https://github.com/pandas/pandas#Period
[pd:datetime]: https://github.com/pandas/pandas#datetime
[pd:expanding_quantile]: https://github.com/pandas/pandas#expanding_quantile
[pd:expanding_count]: https://github.com/pandas/pandas#expanding_count
[pd:scatter_matrix]: https://github.com/pandas/pandas#scatter_matrix
[pd:options]: https://github.com/pandas/pandas#options
[pd:ewmvar]: https://github.com/pandas/pandas#ewmvar
[pd:expanding_max]: https://github.com/pandas/pandas#expanding_max
[pd:concat]: https://github.com/pandas/pandas#concat
[pd:read_sas]: https://github.com/pandas/pandas#read_sas
[pd:describe_option]: https://github.com/pandas/pandas#describe_option
[pd:datetools]: https://github.com/pandas/pandas#datetools
[pd:pandas]: https://github.com/pandas/pandas#pandas
[pd:io]: https://github.com/pandas/pandas#io
[pd:_version]: https://github.com/pandas/pandas#_version
[pd:DataFrame]: https://github.com/pandas/pandas#DataFrame
[pd:read_clipboard]: https://github.com/pandas/pandas#read_clipboard
[pd:rolling_quantile]: https://github.com/pandas/pandas#rolling_quantile
[pd:CategoricalIndex]: https://github.com/pandas/pandas#CategoricalIndex
[pd:rolling_median]: https://github.com/pandas/pandas#rolling_median
[pd:read_json]: https://github.com/pandas/pandas#read_json
[pd:expanding_cov]: https://github.com/pandas/pandas#expanding_cov
[pd:Categorical]: https://github.com/pandas/pandas#Categorical
[pd:read_fwf]: https://github.com/pandas/pandas#read_fwf
[pd:DatetimeIndex]: https://github.com/pandas/pandas#DatetimeIndex
[pd:TimeSeries]: https://github.com/pandas/pandas#TimeSeries
[pd:__version__]: https://github.com/pandas/pandas#__version__
[pd:TimedeltaIndex]: https://github.com/pandas/pandas#TimedeltaIndex
[pd:rolling_cov]: https://github.com/pandas/pandas#rolling_cov
[pd:cut]: https://github.com/pandas/pandas#cut
[pd:json]: https://github.com/pandas/pandas#json
[pd:expanding_corr]: https://github.com/pandas/pandas#expanding_corr
[pd:ewmcorr]: https://github.com/pandas/pandas#ewmcorr
[pd:pivot]: https://github.com/pandas/pandas#pivot





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
      <th>8Ljn0SGMo5</th>
      <td>0.146886</td>
      <td>0.322416</td>
      <td>0.044168</td>
      <td>0.352853</td>
    </tr>
    <tr>
      <th>z0FwGbiyUd</th>
      <td>-1.018506</td>
      <td>0.471733</td>
      <td>-1.205537</td>
      <td>-0.698043</td>
    </tr>
    <tr>
      <th>DUC2ZJepio</th>
      <td>-0.276977</td>
      <td>-0.941129</td>
      <td>1.486763</td>
      <td>0.442387</td>
    </tr>
    <tr>
      <th>uVxQrDvSKO</th>
      <td>-1.915858</td>
      <td>0.512783</td>
      <td>-1.454368</td>
      <td>-0.850423</td>
    </tr>
    <tr>
      <th>91XcXqBoQZ</th>
      <td>-0.319190</td>
      <td>1.118365</td>
      <td>1.978914</td>
      <td>0.703926</td>
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
      <td>-0.167767</td>
      <td>0.094383</td>
      <td>-0.089906</td>
      <td>0.209136</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.804183</td>
      <td>0.991608</td>
      <td>1.134586</td>
      <td>1.027796</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-1.915858</td>
      <td>-2.158519</td>
      <td>-1.902018</td>
      <td>-2.109670</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.711773</td>
      <td>-0.842485</td>
      <td>-1.092959</td>
      <td>-0.520564</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-0.058032</td>
      <td>0.261942</td>
      <td>-0.206085</td>
      <td>0.142370</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.409570</td>
      <td>0.655962</td>
      <td>0.810606</td>
      <td>0.827205</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.418127</td>
      <td>1.933278</td>
      <td>1.991167</td>
      <td>2.466091</td>
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

