
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


[pd:read_stata]: https://github.com/pandas/pandas#read_stata
[pd:Int64Index]: https://github.com/pandas/pandas#Int64Index
[pd:read_gbq]: https://github.com/pandas/pandas#read_gbq
[pd:read_clipboard]: https://github.com/pandas/pandas#read_clipboard
[pd:read_sql]: https://github.com/pandas/pandas#read_sql
[pd:SparseDataFrame]: https://github.com/pandas/pandas#SparseDataFrame
[pd:rolling_max]: https://github.com/pandas/pandas#rolling_max
[pd:computation]: https://github.com/pandas/pandas#computation
[pd:groupby]: https://github.com/pandas/pandas#groupby
[pd:pivot]: https://github.com/pandas/pandas#pivot
[pd:_np_version_under1p8]: https://github.com/pandas/pandas#_np_version_under1p8
[pd:wide_to_long]: https://github.com/pandas/pandas#wide_to_long
[pd:SparseSeries]: https://github.com/pandas/pandas#SparseSeries
[pd:SparseTimeSeries]: https://github.com/pandas/pandas#SparseTimeSeries
[pd:__path__]: https://github.com/pandas/pandas#__path__
[pd:merge]: https://github.com/pandas/pandas#merge
[pd:expanding_skew]: https://github.com/pandas/pandas#expanding_skew
[pd:describe_option]: https://github.com/pandas/pandas#describe_option
[pd:__cached__]: https://github.com/pandas/pandas#__cached__
[pd:rolling_corr]: https://github.com/pandas/pandas#rolling_corr
[pd:read_excel]: https://github.com/pandas/pandas#read_excel
[pd:__version__]: https://github.com/pandas/pandas#__version__
[pd:factorize]: https://github.com/pandas/pandas#factorize
[pd:expanding_min]: https://github.com/pandas/pandas#expanding_min
[pd:concat]: https://github.com/pandas/pandas#concat
[pd:json]: https://github.com/pandas/pandas#json
[pd:read_sql_query]: https://github.com/pandas/pandas#read_sql_query
[pd:HDFStore]: https://github.com/pandas/pandas#HDFStore
[pd:_np_version_under1p12]: https://github.com/pandas/pandas#_np_version_under1p12
[pd:_version]: https://github.com/pandas/pandas#_version
[pd:compat]: https://github.com/pandas/pandas#compat
[pd:expanding_std]: https://github.com/pandas/pandas#expanding_std
[pd:reset_option]: https://github.com/pandas/pandas#reset_option
[pd:infer_freq]: https://github.com/pandas/pandas#infer_freq
[pd:__name__]: https://github.com/pandas/pandas#__name__
[pd:set_option]: https://github.com/pandas/pandas#set_option
[pd:to_msgpack]: https://github.com/pandas/pandas#to_msgpack
[pd:_window]: https://github.com/pandas/pandas#_window
[pd:core]: https://github.com/pandas/pandas#core
[pd:TimedeltaIndex]: https://github.com/pandas/pandas#TimedeltaIndex
[pd:merge_ordered]: https://github.com/pandas/pandas#merge_ordered
[pd:option_context]: https://github.com/pandas/pandas#option_context
[pd:__doc__]: https://github.com/pandas/pandas#__doc__
[pd:__spec__]: https://github.com/pandas/pandas#__spec__
[pd:offsets]: https://github.com/pandas/pandas#offsets
[pd:tseries]: https://github.com/pandas/pandas#tseries
[pd:read_hdf]: https://github.com/pandas/pandas#read_hdf
[pd:SparseArray]: https://github.com/pandas/pandas#SparseArray
[pd:read_fwf]: https://github.com/pandas/pandas#read_fwf
[pd:sparse]: https://github.com/pandas/pandas#sparse
[pd:eval]: https://github.com/pandas/pandas#eval
[pd:stats]: https://github.com/pandas/pandas#stats
[pd:timedelta_range]: https://github.com/pandas/pandas#timedelta_range
[pd:to_datetime]: https://github.com/pandas/pandas#to_datetime
[pd:read_html]: https://github.com/pandas/pandas#read_html
[pd:expanding_kurt]: https://github.com/pandas/pandas#expanding_kurt
[pd:get_dummies]: https://github.com/pandas/pandas#get_dummies
[pd:expanding_max]: https://github.com/pandas/pandas#expanding_max
[pd:_join]: https://github.com/pandas/pandas#_join
[pd:to_numeric]: https://github.com/pandas/pandas#to_numeric
[pd:Expr]: https://github.com/pandas/pandas#Expr
[pd:hashtable]: https://github.com/pandas/pandas#hashtable
[pd:np]: https://github.com/pandas/pandas#np
[pd:__package__]: https://github.com/pandas/pandas#__package__
[pd:read_sas]: https://github.com/pandas/pandas#read_sas
[pd:ewmstd]: https://github.com/pandas/pandas#ewmstd
[pd:expanding_sum]: https://github.com/pandas/pandas#expanding_sum
[pd:msgpack]: https://github.com/pandas/pandas#msgpack
[pd:plot_params]: https://github.com/pandas/pandas#plot_params
[pd:Panel4D]: https://github.com/pandas/pandas#Panel4D
[pd:Grouper]: https://github.com/pandas/pandas#Grouper
[pd:cut]: https://github.com/pandas/pandas#cut
[pd:Period]: https://github.com/pandas/pandas#Period
[pd:expanding_count]: https://github.com/pandas/pandas#expanding_count
[pd:ExcelFile]: https://github.com/pandas/pandas#ExcelFile
[pd:RangeIndex]: https://github.com/pandas/pandas#RangeIndex
[pd:read_pickle]: https://github.com/pandas/pandas#read_pickle
[pd:options]: https://github.com/pandas/pandas#options
[pd:_np_version_under1p10]: https://github.com/pandas/pandas#_np_version_under1p10
[pd:qcut]: https://github.com/pandas/pandas#qcut
[pd:test]: https://github.com/pandas/pandas#test
[pd:ordered_merge]: https://github.com/pandas/pandas#ordered_merge
[pd:rolling_mean]: https://github.com/pandas/pandas#rolling_mean
[pd:_np_version_under1p11]: https://github.com/pandas/pandas#_np_version_under1p11
[pd:formats]: https://github.com/pandas/pandas#formats
[pd:expanding_apply]: https://github.com/pandas/pandas#expanding_apply
[pd:read_json]: https://github.com/pandas/pandas#read_json
[pd:crosstab]: https://github.com/pandas/pandas#crosstab
[pd:ewmcov]: https://github.com/pandas/pandas#ewmcov
[pd:DateOffset]: https://github.com/pandas/pandas#DateOffset
[pd:algos]: https://github.com/pandas/pandas#algos
[pd:bdate_range]: https://github.com/pandas/pandas#bdate_range
[pd:show_versions]: https://github.com/pandas/pandas#show_versions
[pd:_sparse]: https://github.com/pandas/pandas#_sparse
[pd:_period]: https://github.com/pandas/pandas#_period
[pd:scatter_matrix]: https://github.com/pandas/pandas#scatter_matrix
[pd:rolling_quantile]: https://github.com/pandas/pandas#rolling_quantile
[pd:indexes]: https://github.com/pandas/pandas#indexes
[pd:__file__]: https://github.com/pandas/pandas#__file__
[pd:melt]: https://github.com/pandas/pandas#melt
[pd:pandas]: https://github.com/pandas/pandas#pandas
[pd:set_eng_float_format]: https://github.com/pandas/pandas#set_eng_float_format
[pd:expanding_mean]: https://github.com/pandas/pandas#expanding_mean
[pd:merge_asof]: https://github.com/pandas/pandas#merge_asof
[pd:DatetimeIndex]: https://github.com/pandas/pandas#DatetimeIndex
[pd:parser]: https://github.com/pandas/pandas#parser
[pd:ewmvar]: https://github.com/pandas/pandas#ewmvar
[pd:index]: https://github.com/pandas/pandas#index
[pd:read_sql_table]: https://github.com/pandas/pandas#read_sql_table
[pd:lreshape]: https://github.com/pandas/pandas#lreshape
[pd:expanding_cov]: https://github.com/pandas/pandas#expanding_cov
[pd:pivot_table]: https://github.com/pandas/pandas#pivot_table
[pd:isnull]: https://github.com/pandas/pandas#isnull
[pd:TimeGrouper]: https://github.com/pandas/pandas#TimeGrouper
[pd:api]: https://github.com/pandas/pandas#api
[pd:PeriodIndex]: https://github.com/pandas/pandas#PeriodIndex
[pd:util]: https://github.com/pandas/pandas#util
[pd:Timestamp]: https://github.com/pandas/pandas#Timestamp
[pd:MultiIndex]: https://github.com/pandas/pandas#MultiIndex
[pd:CategoricalIndex]: https://github.com/pandas/pandas#CategoricalIndex
[pd:_np_version_under1p9]: https://github.com/pandas/pandas#_np_version_under1p9
[pd:ols]: https://github.com/pandas/pandas#ols
[pd:rolling_kurt]: https://github.com/pandas/pandas#rolling_kurt
[pd:_testing]: https://github.com/pandas/pandas#_testing
[pd:Index]: https://github.com/pandas/pandas#Index
[pd:WidePanel]: https://github.com/pandas/pandas#WidePanel
[pd:SparseList]: https://github.com/pandas/pandas#SparseList
[pd:get_store]: https://github.com/pandas/pandas#get_store
[pd:rolling_var]: https://github.com/pandas/pandas#rolling_var
[pd:io]: https://github.com/pandas/pandas#io
[pd:rolling_apply]: https://github.com/pandas/pandas#rolling_apply
[pd:rolling_std]: https://github.com/pandas/pandas#rolling_std
[pd:Categorical]: https://github.com/pandas/pandas#Categorical
[pd:__docformat__]: https://github.com/pandas/pandas#__docformat__
[pd:NaT]: https://github.com/pandas/pandas#NaT
[pd:to_pickle]: https://github.com/pandas/pandas#to_pickle
[pd:ewma]: https://github.com/pandas/pandas#ewma
[pd:datetools]: https://github.com/pandas/pandas#datetools
[pd:to_timedelta]: https://github.com/pandas/pandas#to_timedelta
[pd:ewmcorr]: https://github.com/pandas/pandas#ewmcorr
[pd:rolling_window]: https://github.com/pandas/pandas#rolling_window
[pd:lib]: https://github.com/pandas/pandas#lib
[pd:expanding_quantile]: https://github.com/pandas/pandas#expanding_quantile
[pd:period_range]: https://github.com/pandas/pandas#period_range
[pd:rolling_sum]: https://github.com/pandas/pandas#rolling_sum
[pd:Float64Index]: https://github.com/pandas/pandas#Float64Index
[pd:tslib]: https://github.com/pandas/pandas#tslib
[pd:notnull]: https://github.com/pandas/pandas#notnull
[pd:rolling_min]: https://github.com/pandas/pandas#rolling_min
[pd:unique]: https://github.com/pandas/pandas#unique
[pd:read_csv]: https://github.com/pandas/pandas#read_csv
[pd:types]: https://github.com/pandas/pandas#types
[pd:Panel]: https://github.com/pandas/pandas#Panel
[pd:pnow]: https://github.com/pandas/pandas#pnow
[pd:match]: https://github.com/pandas/pandas#match
[pd:datetime]: https://github.com/pandas/pandas#datetime
[pd:info]: https://github.com/pandas/pandas#info
[pd:read_table]: https://github.com/pandas/pandas#read_table
[pd:ewmvol]: https://github.com/pandas/pandas#ewmvol
[pd:expanding_median]: https://github.com/pandas/pandas#expanding_median
[pd:value_counts]: https://github.com/pandas/pandas#value_counts
[pd:IndexSlice]: https://github.com/pandas/pandas#IndexSlice
[pd:Term]: https://github.com/pandas/pandas#Term
[pd:__loader__]: https://github.com/pandas/pandas#__loader__
[pd:__builtins__]: https://github.com/pandas/pandas#__builtins__
[pd:ExcelWriter]: https://github.com/pandas/pandas#ExcelWriter
[pd:rolling_cov]: https://github.com/pandas/pandas#rolling_cov
[pd:tools]: https://github.com/pandas/pandas#tools
[pd:rolling_skew]: https://github.com/pandas/pandas#rolling_skew
[pd:Series]: https://github.com/pandas/pandas#Series
[pd:date_range]: https://github.com/pandas/pandas#date_range
[pd:fama_macbeth]: https://github.com/pandas/pandas#fama_macbeth
[pd:DataFrame]: https://github.com/pandas/pandas#DataFrame
[pd:get_option]: https://github.com/pandas/pandas#get_option
[pd:expanding_var]: https://github.com/pandas/pandas#expanding_var
[pd:expanding_corr]: https://github.com/pandas/pandas#expanding_corr
[pd:Timedelta]: https://github.com/pandas/pandas#Timedelta
[pd:rolling_count]: https://github.com/pandas/pandas#rolling_count
[pd:TimeSeries]: https://github.com/pandas/pandas#TimeSeries
[pd:rolling_median]: https://github.com/pandas/pandas#rolling_median
[pd:read_msgpack]: https://github.com/pandas/pandas#read_msgpack





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
      <th>SDf1BTNg2H</th>
      <td>0.047172</td>
      <td>-1.852776</td>
      <td>0.603858</td>
      <td>0.430012</td>
    </tr>
    <tr>
      <th>wG76qV7W9y</th>
      <td>-0.274920</td>
      <td>-0.454935</td>
      <td>1.288556</td>
      <td>1.598037</td>
    </tr>
    <tr>
      <th>OSIrokOIi3</th>
      <td>-0.432110</td>
      <td>0.382211</td>
      <td>1.238428</td>
      <td>-0.557180</td>
    </tr>
    <tr>
      <th>pKqJo9rQhe</th>
      <td>-0.146874</td>
      <td>-2.869897</td>
      <td>1.617484</td>
      <td>0.066000</td>
    </tr>
    <tr>
      <th>0LKZFRmxRW</th>
      <td>0.751461</td>
      <td>0.501270</td>
      <td>2.123044</td>
      <td>-0.924629</td>
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
      <td>-0.017317</td>
      <td>-0.237950</td>
      <td>0.254655</td>
      <td>-0.010835</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.953377</td>
      <td>0.944980</td>
      <td>0.999442</td>
      <td>0.981480</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-1.699766</td>
      <td>-2.869897</td>
      <td>-2.113209</td>
      <td>-2.146972</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.576941</td>
      <td>-0.897749</td>
      <td>-0.454231</td>
      <td>-0.567761</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.016629</td>
      <td>-0.221985</td>
      <td>0.176629</td>
      <td>-0.007592</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.447102</td>
      <td>0.426445</td>
      <td>1.122386</td>
      <td>0.755851</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.825131</td>
      <td>1.747997</td>
      <td>2.123044</td>
      <td>1.598037</td>
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
    [NbConvertApp] Writing 18189 bytes to readme.md

