
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


    The literacy extension doesn't define how to unload it.
    The literacy extension is already loaded. To reload it, use:
      %reload_ext literacy



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


[pd:lreshape]: https://github.com/pandas/pandas#lreshape
[pd:expanding_median]: https://github.com/pandas/pandas#expanding_median
[pd:merge_asof]: https://github.com/pandas/pandas#merge_asof
[pd:rolling_sum]: https://github.com/pandas/pandas#rolling_sum
[pd:isnull]: https://github.com/pandas/pandas#isnull
[pd:match]: https://github.com/pandas/pandas#match
[pd:__cached__]: https://github.com/pandas/pandas#__cached__
[pd:merge_ordered]: https://github.com/pandas/pandas#merge_ordered
[pd:rolling_count]: https://github.com/pandas/pandas#rolling_count
[pd:rolling_window]: https://github.com/pandas/pandas#rolling_window
[pd:concat]: https://github.com/pandas/pandas#concat
[pd:parser]: https://github.com/pandas/pandas#parser
[pd:expanding_count]: https://github.com/pandas/pandas#expanding_count
[pd:ExcelFile]: https://github.com/pandas/pandas#ExcelFile
[pd:read_html]: https://github.com/pandas/pandas#read_html
[pd:Term]: https://github.com/pandas/pandas#Term
[pd:get_store]: https://github.com/pandas/pandas#get_store
[pd:msgpack]: https://github.com/pandas/pandas#msgpack
[pd:datetime]: https://github.com/pandas/pandas#datetime
[pd:infer_freq]: https://github.com/pandas/pandas#infer_freq
[pd:rolling_skew]: https://github.com/pandas/pandas#rolling_skew
[pd:expanding_mean]: https://github.com/pandas/pandas#expanding_mean
[pd:Period]: https://github.com/pandas/pandas#Period
[pd:DateOffset]: https://github.com/pandas/pandas#DateOffset
[pd:Float64Index]: https://github.com/pandas/pandas#Float64Index
[pd:option_context]: https://github.com/pandas/pandas#option_context
[pd:SparseSeries]: https://github.com/pandas/pandas#SparseSeries
[pd:indexes]: https://github.com/pandas/pandas#indexes
[pd:expanding_cov]: https://github.com/pandas/pandas#expanding_cov
[pd:tseries]: https://github.com/pandas/pandas#tseries
[pd:ewmcov]: https://github.com/pandas/pandas#ewmcov
[pd:read_csv]: https://github.com/pandas/pandas#read_csv
[pd:scatter_matrix]: https://github.com/pandas/pandas#scatter_matrix
[pd:_np_version_under1p12]: https://github.com/pandas/pandas#_np_version_under1p12
[pd:Categorical]: https://github.com/pandas/pandas#Categorical
[pd:crosstab]: https://github.com/pandas/pandas#crosstab
[pd:SparseDataFrame]: https://github.com/pandas/pandas#SparseDataFrame
[pd:expanding_kurt]: https://github.com/pandas/pandas#expanding_kurt
[pd:WidePanel]: https://github.com/pandas/pandas#WidePanel
[pd:ExcelWriter]: https://github.com/pandas/pandas#ExcelWriter
[pd:to_numeric]: https://github.com/pandas/pandas#to_numeric
[pd:read_fwf]: https://github.com/pandas/pandas#read_fwf
[pd:groupby]: https://github.com/pandas/pandas#groupby
[pd:set_eng_float_format]: https://github.com/pandas/pandas#set_eng_float_format
[pd:Panel]: https://github.com/pandas/pandas#Panel
[pd:offsets]: https://github.com/pandas/pandas#offsets
[pd:rolling_min]: https://github.com/pandas/pandas#rolling_min
[pd:CategoricalIndex]: https://github.com/pandas/pandas#CategoricalIndex
[pd:algos]: https://github.com/pandas/pandas#algos
[pd:read_sql_table]: https://github.com/pandas/pandas#read_sql_table
[pd:api]: https://github.com/pandas/pandas#api
[pd:read_gbq]: https://github.com/pandas/pandas#read_gbq
[pd:expanding_quantile]: https://github.com/pandas/pandas#expanding_quantile
[pd:expanding_std]: https://github.com/pandas/pandas#expanding_std
[pd:to_msgpack]: https://github.com/pandas/pandas#to_msgpack
[pd:_testing]: https://github.com/pandas/pandas#_testing
[pd:__doc__]: https://github.com/pandas/pandas#__doc__
[pd:Panel4D]: https://github.com/pandas/pandas#Panel4D
[pd:rolling_max]: https://github.com/pandas/pandas#rolling_max
[pd:__loader__]: https://github.com/pandas/pandas#__loader__
[pd:notnull]: https://github.com/pandas/pandas#notnull
[pd:__file__]: https://github.com/pandas/pandas#__file__
[pd:read_sql_query]: https://github.com/pandas/pandas#read_sql_query
[pd:TimedeltaIndex]: https://github.com/pandas/pandas#TimedeltaIndex
[pd:Int64Index]: https://github.com/pandas/pandas#Int64Index
[pd:Timedelta]: https://github.com/pandas/pandas#Timedelta
[pd:__package__]: https://github.com/pandas/pandas#__package__
[pd:RangeIndex]: https://github.com/pandas/pandas#RangeIndex
[pd:expanding_max]: https://github.com/pandas/pandas#expanding_max
[pd:compat]: https://github.com/pandas/pandas#compat
[pd:computation]: https://github.com/pandas/pandas#computation
[pd:read_stata]: https://github.com/pandas/pandas#read_stata
[pd:eval]: https://github.com/pandas/pandas#eval
[pd:options]: https://github.com/pandas/pandas#options
[pd:expanding_sum]: https://github.com/pandas/pandas#expanding_sum
[pd:_join]: https://github.com/pandas/pandas#_join
[pd:__spec__]: https://github.com/pandas/pandas#__spec__
[pd:io]: https://github.com/pandas/pandas#io
[pd:to_pickle]: https://github.com/pandas/pandas#to_pickle
[pd:_version]: https://github.com/pandas/pandas#_version
[pd:to_datetime]: https://github.com/pandas/pandas#to_datetime
[pd:Series]: https://github.com/pandas/pandas#Series
[pd:describe_option]: https://github.com/pandas/pandas#describe_option
[pd:IndexSlice]: https://github.com/pandas/pandas#IndexSlice
[pd:TimeSeries]: https://github.com/pandas/pandas#TimeSeries
[pd:rolling_std]: https://github.com/pandas/pandas#rolling_std
[pd:qcut]: https://github.com/pandas/pandas#qcut
[pd:_sparse]: https://github.com/pandas/pandas#_sparse
[pd:__version__]: https://github.com/pandas/pandas#__version__
[pd:period_range]: https://github.com/pandas/pandas#period_range
[pd:unique]: https://github.com/pandas/pandas#unique
[pd:rolling_corr]: https://github.com/pandas/pandas#rolling_corr
[pd:rolling_median]: https://github.com/pandas/pandas#rolling_median
[pd:SparseList]: https://github.com/pandas/pandas#SparseList
[pd:stats]: https://github.com/pandas/pandas#stats
[pd:TimeGrouper]: https://github.com/pandas/pandas#TimeGrouper
[pd:timedelta_range]: https://github.com/pandas/pandas#timedelta_range
[pd:MultiIndex]: https://github.com/pandas/pandas#MultiIndex
[pd:lib]: https://github.com/pandas/pandas#lib
[pd:index]: https://github.com/pandas/pandas#index
[pd:rolling_kurt]: https://github.com/pandas/pandas#rolling_kurt
[pd:__path__]: https://github.com/pandas/pandas#__path__
[pd:_np_version_under1p10]: https://github.com/pandas/pandas#_np_version_under1p10
[pd:read_table]: https://github.com/pandas/pandas#read_table
[pd:tslib]: https://github.com/pandas/pandas#tslib
[pd:json]: https://github.com/pandas/pandas#json
[pd:set_option]: https://github.com/pandas/pandas#set_option
[pd:value_counts]: https://github.com/pandas/pandas#value_counts
[pd:rolling_quantile]: https://github.com/pandas/pandas#rolling_quantile
[pd:tools]: https://github.com/pandas/pandas#tools
[pd:read_json]: https://github.com/pandas/pandas#read_json
[pd:SparseTimeSeries]: https://github.com/pandas/pandas#SparseTimeSeries
[pd:Expr]: https://github.com/pandas/pandas#Expr
[pd:expanding_corr]: https://github.com/pandas/pandas#expanding_corr
[pd:show_versions]: https://github.com/pandas/pandas#show_versions
[pd:__docformat__]: https://github.com/pandas/pandas#__docformat__
[pd:ewmvar]: https://github.com/pandas/pandas#ewmvar
[pd:Timestamp]: https://github.com/pandas/pandas#Timestamp
[pd:_window]: https://github.com/pandas/pandas#_window
[pd:formats]: https://github.com/pandas/pandas#formats
[pd:read_sas]: https://github.com/pandas/pandas#read_sas
[pd:test]: https://github.com/pandas/pandas#test
[pd:util]: https://github.com/pandas/pandas#util
[pd:read_sql]: https://github.com/pandas/pandas#read_sql
[pd:expanding_var]: https://github.com/pandas/pandas#expanding_var
[pd:core]: https://github.com/pandas/pandas#core
[pd:datetools]: https://github.com/pandas/pandas#datetools
[pd:Index]: https://github.com/pandas/pandas#Index
[pd:cut]: https://github.com/pandas/pandas#cut
[pd:pnow]: https://github.com/pandas/pandas#pnow
[pd:ewmcorr]: https://github.com/pandas/pandas#ewmcorr
[pd:ewmvol]: https://github.com/pandas/pandas#ewmvol
[pd:ols]: https://github.com/pandas/pandas#ols
[pd:melt]: https://github.com/pandas/pandas#melt
[pd:pandas]: https://github.com/pandas/pandas#pandas
[pd:read_hdf]: https://github.com/pandas/pandas#read_hdf
[pd:factorize]: https://github.com/pandas/pandas#factorize
[pd:PeriodIndex]: https://github.com/pandas/pandas#PeriodIndex
[pd:hashtable]: https://github.com/pandas/pandas#hashtable
[pd:_period]: https://github.com/pandas/pandas#_period
[pd:read_clipboard]: https://github.com/pandas/pandas#read_clipboard
[pd:fama_macbeth]: https://github.com/pandas/pandas#fama_macbeth
[pd:rolling_var]: https://github.com/pandas/pandas#rolling_var
[pd:types]: https://github.com/pandas/pandas#types
[pd:__builtins__]: https://github.com/pandas/pandas#__builtins__
[pd:DataFrame]: https://github.com/pandas/pandas#DataFrame
[pd:np]: https://github.com/pandas/pandas#np
[pd:read_excel]: https://github.com/pandas/pandas#read_excel
[pd:pivot]: https://github.com/pandas/pandas#pivot
[pd:read_msgpack]: https://github.com/pandas/pandas#read_msgpack
[pd:rolling_mean]: https://github.com/pandas/pandas#rolling_mean
[pd:sparse]: https://github.com/pandas/pandas#sparse
[pd:ordered_merge]: https://github.com/pandas/pandas#ordered_merge
[pd:SparseArray]: https://github.com/pandas/pandas#SparseArray
[pd:get_option]: https://github.com/pandas/pandas#get_option
[pd:ewmstd]: https://github.com/pandas/pandas#ewmstd
[pd:pivot_table]: https://github.com/pandas/pandas#pivot_table
[pd:NaT]: https://github.com/pandas/pandas#NaT
[pd:expanding_apply]: https://github.com/pandas/pandas#expanding_apply
[pd:_np_version_under1p11]: https://github.com/pandas/pandas#_np_version_under1p11
[pd:expanding_skew]: https://github.com/pandas/pandas#expanding_skew
[pd:plot_params]: https://github.com/pandas/pandas#plot_params
[pd:to_timedelta]: https://github.com/pandas/pandas#to_timedelta
[pd:__name__]: https://github.com/pandas/pandas#__name__
[pd:get_dummies]: https://github.com/pandas/pandas#get_dummies
[pd:bdate_range]: https://github.com/pandas/pandas#bdate_range
[pd:_np_version_under1p9]: https://github.com/pandas/pandas#_np_version_under1p9
[pd:info]: https://github.com/pandas/pandas#info
[pd:merge]: https://github.com/pandas/pandas#merge
[pd:DatetimeIndex]: https://github.com/pandas/pandas#DatetimeIndex
[pd:wide_to_long]: https://github.com/pandas/pandas#wide_to_long
[pd:reset_option]: https://github.com/pandas/pandas#reset_option
[pd:ewma]: https://github.com/pandas/pandas#ewma
[pd:rolling_apply]: https://github.com/pandas/pandas#rolling_apply
[pd:Grouper]: https://github.com/pandas/pandas#Grouper
[pd:expanding_min]: https://github.com/pandas/pandas#expanding_min
[pd:rolling_cov]: https://github.com/pandas/pandas#rolling_cov
[pd:read_pickle]: https://github.com/pandas/pandas#read_pickle
[pd:_np_version_under1p8]: https://github.com/pandas/pandas#_np_version_under1p8
[pd:HDFStore]: https://github.com/pandas/pandas#HDFStore
[pd:date_range]: https://github.com/pandas/pandas#date_range





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
      <th>6fHEZuicyv</th>
      <td>-1.164558</td>
      <td>-1.705563</td>
      <td>-0.958202</td>
      <td>0.904970</td>
    </tr>
    <tr>
      <th>Kl8M2wXECP</th>
      <td>0.031830</td>
      <td>0.175336</td>
      <td>-0.499233</td>
      <td>1.532042</td>
    </tr>
    <tr>
      <th>D0L1n4IeTj</th>
      <td>0.430954</td>
      <td>1.105751</td>
      <td>-0.166117</td>
      <td>-0.556662</td>
    </tr>
    <tr>
      <th>UB2E2ueTT2</th>
      <td>1.928141</td>
      <td>-0.233943</td>
      <td>0.357397</td>
      <td>-1.051417</td>
    </tr>
    <tr>
      <th>Sr1wz9yIvT</th>
      <td>1.392489</td>
      <td>0.583714</td>
      <td>-0.110042</td>
      <td>-1.291159</td>
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
      <td>0.126514</td>
      <td>0.001174</td>
      <td>0.016246</td>
      <td>-0.224229</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.072202</td>
      <td>1.242995</td>
      <td>1.222341</td>
      <td>1.067168</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-2.191796</td>
      <td>-2.296738</td>
      <td>-1.924885</td>
      <td>-1.662792</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.661703</td>
      <td>-0.800405</td>
      <td>-0.865513</td>
      <td>-1.099564</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.070228</td>
      <td>0.284665</td>
      <td>-0.116364</td>
      <td>-0.426725</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.846974</td>
      <td>0.879298</td>
      <td>0.734635</td>
      <td>0.427850</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.928141</td>
      <td>2.139305</td>
      <td>2.496402</td>
      <td>2.286156</td>
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
    [NbConvertApp] Writing 18188 bytes to readme.md

