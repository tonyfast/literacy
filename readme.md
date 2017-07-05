
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


[pd:datetools]: https://github.com/pandas/pandas#datetools
[pd:ols]: https://github.com/pandas/pandas#ols
[pd:Index]: https://github.com/pandas/pandas#Index
[pd:_period]: https://github.com/pandas/pandas#_period
[pd:melt]: https://github.com/pandas/pandas#melt
[pd:compat]: https://github.com/pandas/pandas#compat
[pd:rolling_max]: https://github.com/pandas/pandas#rolling_max
[pd:read_html]: https://github.com/pandas/pandas#read_html
[pd:lib]: https://github.com/pandas/pandas#lib
[pd:parser]: https://github.com/pandas/pandas#parser
[pd:ExcelFile]: https://github.com/pandas/pandas#ExcelFile
[pd:computation]: https://github.com/pandas/pandas#computation
[pd:Panel4D]: https://github.com/pandas/pandas#Panel4D
[pd:ordered_merge]: https://github.com/pandas/pandas#ordered_merge
[pd:timedelta_range]: https://github.com/pandas/pandas#timedelta_range
[pd:core]: https://github.com/pandas/pandas#core
[pd:__spec__]: https://github.com/pandas/pandas#__spec__
[pd:rolling_window]: https://github.com/pandas/pandas#rolling_window
[pd:PeriodIndex]: https://github.com/pandas/pandas#PeriodIndex
[pd:__package__]: https://github.com/pandas/pandas#__package__
[pd:fama_macbeth]: https://github.com/pandas/pandas#fama_macbeth
[pd:__cached__]: https://github.com/pandas/pandas#__cached__
[pd:SparseTimeSeries]: https://github.com/pandas/pandas#SparseTimeSeries
[pd:rolling_cov]: https://github.com/pandas/pandas#rolling_cov
[pd:ewmvol]: https://github.com/pandas/pandas#ewmvol
[pd:date_range]: https://github.com/pandas/pandas#date_range
[pd:expanding_corr]: https://github.com/pandas/pandas#expanding_corr
[pd:expanding_std]: https://github.com/pandas/pandas#expanding_std
[pd:ExcelWriter]: https://github.com/pandas/pandas#ExcelWriter
[pd:_np_version_under1p9]: https://github.com/pandas/pandas#_np_version_under1p9
[pd:hashtable]: https://github.com/pandas/pandas#hashtable
[pd:cut]: https://github.com/pandas/pandas#cut
[pd:get_option]: https://github.com/pandas/pandas#get_option
[pd:read_gbq]: https://github.com/pandas/pandas#read_gbq
[pd:ewmvar]: https://github.com/pandas/pandas#ewmvar
[pd:tools]: https://github.com/pandas/pandas#tools
[pd:pivot_table]: https://github.com/pandas/pandas#pivot_table
[pd:sparse]: https://github.com/pandas/pandas#sparse
[pd:NaT]: https://github.com/pandas/pandas#NaT
[pd:msgpack]: https://github.com/pandas/pandas#msgpack
[pd:expanding_kurt]: https://github.com/pandas/pandas#expanding_kurt
[pd:expanding_max]: https://github.com/pandas/pandas#expanding_max
[pd:_np_version_under1p11]: https://github.com/pandas/pandas#_np_version_under1p11
[pd:np]: https://github.com/pandas/pandas#np
[pd:set_eng_float_format]: https://github.com/pandas/pandas#set_eng_float_format
[pd:io]: https://github.com/pandas/pandas#io
[pd:TimedeltaIndex]: https://github.com/pandas/pandas#TimedeltaIndex
[pd:MultiIndex]: https://github.com/pandas/pandas#MultiIndex
[pd:_np_version_under1p12]: https://github.com/pandas/pandas#_np_version_under1p12
[pd:Categorical]: https://github.com/pandas/pandas#Categorical
[pd:TimeGrouper]: https://github.com/pandas/pandas#TimeGrouper
[pd:expanding_cov]: https://github.com/pandas/pandas#expanding_cov
[pd:isnull]: https://github.com/pandas/pandas#isnull
[pd:read_excel]: https://github.com/pandas/pandas#read_excel
[pd:_version]: https://github.com/pandas/pandas#_version
[pd:expanding_count]: https://github.com/pandas/pandas#expanding_count
[pd:read_csv]: https://github.com/pandas/pandas#read_csv
[pd:rolling_var]: https://github.com/pandas/pandas#rolling_var
[pd:to_timedelta]: https://github.com/pandas/pandas#to_timedelta
[pd:eval]: https://github.com/pandas/pandas#eval
[pd:SparseList]: https://github.com/pandas/pandas#SparseList
[pd:_np_version_under1p8]: https://github.com/pandas/pandas#_np_version_under1p8
[pd:algos]: https://github.com/pandas/pandas#algos
[pd:__loader__]: https://github.com/pandas/pandas#__loader__
[pd:Timedelta]: https://github.com/pandas/pandas#Timedelta
[pd:expanding_min]: https://github.com/pandas/pandas#expanding_min
[pd:crosstab]: https://github.com/pandas/pandas#crosstab
[pd:__version__]: https://github.com/pandas/pandas#__version__
[pd:get_dummies]: https://github.com/pandas/pandas#get_dummies
[pd:to_pickle]: https://github.com/pandas/pandas#to_pickle
[pd:SparseSeries]: https://github.com/pandas/pandas#SparseSeries
[pd:info]: https://github.com/pandas/pandas#info
[pd:read_sql]: https://github.com/pandas/pandas#read_sql
[pd:rolling_apply]: https://github.com/pandas/pandas#rolling_apply
[pd:qcut]: https://github.com/pandas/pandas#qcut
[pd:__path__]: https://github.com/pandas/pandas#__path__
[pd:ewmcorr]: https://github.com/pandas/pandas#ewmcorr
[pd:expanding_var]: https://github.com/pandas/pandas#expanding_var
[pd:rolling_std]: https://github.com/pandas/pandas#rolling_std
[pd:groupby]: https://github.com/pandas/pandas#groupby
[pd:read_pickle]: https://github.com/pandas/pandas#read_pickle
[pd:SparseDataFrame]: https://github.com/pandas/pandas#SparseDataFrame
[pd:rolling_kurt]: https://github.com/pandas/pandas#rolling_kurt
[pd:to_numeric]: https://github.com/pandas/pandas#to_numeric
[pd:expanding_mean]: https://github.com/pandas/pandas#expanding_mean
[pd:read_stata]: https://github.com/pandas/pandas#read_stata
[pd:_window]: https://github.com/pandas/pandas#_window
[pd:rolling_mean]: https://github.com/pandas/pandas#rolling_mean
[pd:period_range]: https://github.com/pandas/pandas#period_range
[pd:__builtins__]: https://github.com/pandas/pandas#__builtins__
[pd:show_versions]: https://github.com/pandas/pandas#show_versions
[pd:Float64Index]: https://github.com/pandas/pandas#Float64Index
[pd:CategoricalIndex]: https://github.com/pandas/pandas#CategoricalIndex
[pd:options]: https://github.com/pandas/pandas#options
[pd:rolling_min]: https://github.com/pandas/pandas#rolling_min
[pd:infer_freq]: https://github.com/pandas/pandas#infer_freq
[pd:IndexSlice]: https://github.com/pandas/pandas#IndexSlice
[pd:to_datetime]: https://github.com/pandas/pandas#to_datetime
[pd:test]: https://github.com/pandas/pandas#test
[pd:index]: https://github.com/pandas/pandas#index
[pd:match]: https://github.com/pandas/pandas#match
[pd:json]: https://github.com/pandas/pandas#json
[pd:_testing]: https://github.com/pandas/pandas#_testing
[pd:read_table]: https://github.com/pandas/pandas#read_table
[pd:__docformat__]: https://github.com/pandas/pandas#__docformat__
[pd:read_hdf]: https://github.com/pandas/pandas#read_hdf
[pd:SparseArray]: https://github.com/pandas/pandas#SparseArray
[pd:option_context]: https://github.com/pandas/pandas#option_context
[pd:formats]: https://github.com/pandas/pandas#formats
[pd:read_clipboard]: https://github.com/pandas/pandas#read_clipboard
[pd:Series]: https://github.com/pandas/pandas#Series
[pd:expanding_apply]: https://github.com/pandas/pandas#expanding_apply
[pd:expanding_median]: https://github.com/pandas/pandas#expanding_median
[pd:wide_to_long]: https://github.com/pandas/pandas#wide_to_long
[pd:tseries]: https://github.com/pandas/pandas#tseries
[pd:WidePanel]: https://github.com/pandas/pandas#WidePanel
[pd:Panel]: https://github.com/pandas/pandas#Panel
[pd:stats]: https://github.com/pandas/pandas#stats
[pd:read_sql_query]: https://github.com/pandas/pandas#read_sql_query
[pd:value_counts]: https://github.com/pandas/pandas#value_counts
[pd:read_msgpack]: https://github.com/pandas/pandas#read_msgpack
[pd:ewmcov]: https://github.com/pandas/pandas#ewmcov
[pd:Timestamp]: https://github.com/pandas/pandas#Timestamp
[pd:set_option]: https://github.com/pandas/pandas#set_option
[pd:get_store]: https://github.com/pandas/pandas#get_store
[pd:describe_option]: https://github.com/pandas/pandas#describe_option
[pd:read_json]: https://github.com/pandas/pandas#read_json
[pd:plot_params]: https://github.com/pandas/pandas#plot_params
[pd:Grouper]: https://github.com/pandas/pandas#Grouper
[pd:DatetimeIndex]: https://github.com/pandas/pandas#DatetimeIndex
[pd:_sparse]: https://github.com/pandas/pandas#_sparse
[pd:to_msgpack]: https://github.com/pandas/pandas#to_msgpack
[pd:rolling_median]: https://github.com/pandas/pandas#rolling_median
[pd:Expr]: https://github.com/pandas/pandas#Expr
[pd:datetime]: https://github.com/pandas/pandas#datetime
[pd:concat]: https://github.com/pandas/pandas#concat
[pd:tslib]: https://github.com/pandas/pandas#tslib
[pd:rolling_sum]: https://github.com/pandas/pandas#rolling_sum
[pd:Term]: https://github.com/pandas/pandas#Term
[pd:merge_asof]: https://github.com/pandas/pandas#merge_asof
[pd:Int64Index]: https://github.com/pandas/pandas#Int64Index
[pd:lreshape]: https://github.com/pandas/pandas#lreshape
[pd:indexes]: https://github.com/pandas/pandas#indexes
[pd:rolling_skew]: https://github.com/pandas/pandas#rolling_skew
[pd:_np_version_under1p10]: https://github.com/pandas/pandas#_np_version_under1p10
[pd:rolling_count]: https://github.com/pandas/pandas#rolling_count
[pd:scatter_matrix]: https://github.com/pandas/pandas#scatter_matrix
[pd:DataFrame]: https://github.com/pandas/pandas#DataFrame
[pd:pnow]: https://github.com/pandas/pandas#pnow
[pd:read_sql_table]: https://github.com/pandas/pandas#read_sql_table
[pd:factorize]: https://github.com/pandas/pandas#factorize
[pd:bdate_range]: https://github.com/pandas/pandas#bdate_range
[pd:__doc__]: https://github.com/pandas/pandas#__doc__
[pd:_join]: https://github.com/pandas/pandas#_join
[pd:TimeSeries]: https://github.com/pandas/pandas#TimeSeries
[pd:HDFStore]: https://github.com/pandas/pandas#HDFStore
[pd:rolling_quantile]: https://github.com/pandas/pandas#rolling_quantile
[pd:unique]: https://github.com/pandas/pandas#unique
[pd:expanding_skew]: https://github.com/pandas/pandas#expanding_skew
[pd:merge]: https://github.com/pandas/pandas#merge
[pd:expanding_quantile]: https://github.com/pandas/pandas#expanding_quantile
[pd:util]: https://github.com/pandas/pandas#util
[pd:DateOffset]: https://github.com/pandas/pandas#DateOffset
[pd:RangeIndex]: https://github.com/pandas/pandas#RangeIndex
[pd:notnull]: https://github.com/pandas/pandas#notnull
[pd:pivot]: https://github.com/pandas/pandas#pivot
[pd:read_sas]: https://github.com/pandas/pandas#read_sas
[pd:ewma]: https://github.com/pandas/pandas#ewma
[pd:types]: https://github.com/pandas/pandas#types
[pd:reset_option]: https://github.com/pandas/pandas#reset_option
[pd:Period]: https://github.com/pandas/pandas#Period
[pd:read_fwf]: https://github.com/pandas/pandas#read_fwf
[pd:rolling_corr]: https://github.com/pandas/pandas#rolling_corr
[pd:__name__]: https://github.com/pandas/pandas#__name__
[pd:offsets]: https://github.com/pandas/pandas#offsets
[pd:expanding_sum]: https://github.com/pandas/pandas#expanding_sum
[pd:ewmstd]: https://github.com/pandas/pandas#ewmstd
[pd:__file__]: https://github.com/pandas/pandas#__file__
[pd:api]: https://github.com/pandas/pandas#api
[pd:pandas]: https://github.com/pandas/pandas#pandas
[pd:merge_ordered]: https://github.com/pandas/pandas#merge_ordered





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
      <th>qpmaTfeOVi</th>
      <td>0.865243</td>
      <td>1.092412</td>
      <td>0.214716</td>
      <td>0.924166</td>
    </tr>
    <tr>
      <th>9f2MtCeaRC</th>
      <td>0.279306</td>
      <td>-0.827952</td>
      <td>-1.136781</td>
      <td>0.452437</td>
    </tr>
    <tr>
      <th>DL8XIIVl6x</th>
      <td>1.169054</td>
      <td>0.789950</td>
      <td>0.131367</td>
      <td>-0.153040</td>
    </tr>
    <tr>
      <th>wUyLXHkgpJ</th>
      <td>-0.288867</td>
      <td>-2.172063</td>
      <td>-2.901560</td>
      <td>0.234229</td>
    </tr>
    <tr>
      <th>AIgbVxzsIP</th>
      <td>1.309793</td>
      <td>-0.401172</td>
      <td>-0.248805</td>
      <td>0.725979</td>
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
      <td>0.111058</td>
      <td>-0.012172</td>
      <td>0.022822</td>
      <td>-0.126050</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.976539</td>
      <td>0.902385</td>
      <td>1.019374</td>
      <td>1.121299</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-1.383609</td>
      <td>-2.172063</td>
      <td>-2.901560</td>
      <td>-2.488829</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.564556</td>
      <td>-0.743084</td>
      <td>-0.569463</td>
      <td>-0.764867</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-0.026636</td>
      <td>0.015372</td>
      <td>0.064171</td>
      <td>-0.129140</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.838785</td>
      <td>0.693731</td>
      <td>0.604977</td>
      <td>0.711671</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2.243202</td>
      <td>1.595759</td>
      <td>1.824063</td>
      <td>2.127853</td>
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
    [NbConvertApp] Writing 18195 bytes to readme.md

