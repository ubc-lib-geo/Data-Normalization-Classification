---
layout: default
title: Data Classification
nav_order: 6
---

# Part 3) Data Classification, Histograms, & Cloropleth Mapping


# Rates by Province/State

Police Killing Rates vary by administrative divisions, e.g. (State/Province)
* If we want to compare rates the first step is to look at histograms.
* A Histogram shows us the frequency distribution of a given variable
    * Data is grouped into a set of bins and counted





<a href="US_Rate_Hist.png" target="_blank">View Image in New Tab</a>

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="US_Rate_Hist.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>

    count     13.000000
    mean      41.538462
    std       55.853402
    min        1.000000
    25%        4.000000
    50%        7.000000
    75%       91.000000
    max      175.000000
    Name: Total_Killings, dtype: float64
    

# Outliers
Histograms can be useful for spotting outliers in a dataset
* The Indigenouos Police Killing rate hisogram for the US shows an outlier
    * Vermont has a rate many times higher than the nearest value


<a href="US_State_Hist_by_Race.png" target="_blank">View Image in New Tab</a>

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="US_State_Hist_by_Race.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>


    count    51.000000
    mean      5.912896
    std      11.557095
    min       0.000000
    25%       0.000000
    50%       0.000000
    75%       9.706034
    max      74.706772
    Name: Indigenous_Rate, dtype: float64
    



    count    51.000000
    mean      5.912896
    std      11.557095
    min       0.000000
    25%       0.000000
    50%       0.000000
    75%       9.706034
    max      74.706772
    Name: Indigenous_Rate, dtype: float64
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>STUSPS</th>
      <th>Indigenous_Rate</th>
      <th>Indigenous_Killings</th>
      <th>Indigenous</th>
      <th>Indigenous_Fraction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>VT</td>
      <td>74.707</td>
      <td>1.0</td>
      <td>1743</td>
      <td>0.278</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ND</td>
      <td>18.931</td>
      <td>6.0</td>
      <td>41270</td>
      <td>5.430</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ID</td>
      <td>16.965</td>
      <td>3.0</td>
      <td>23026</td>
      <td>1.313</td>
    </tr>
    <tr>
      <th>3</th>
      <td>WY</td>
      <td>16.091</td>
      <td>2.0</td>
      <td>16185</td>
      <td>2.801</td>
    </tr>
    <tr>
      <th>4</th>
      <td>WA</td>
      <td>16.054</td>
      <td>12.0</td>
      <td>97329</td>
      <td>1.292</td>
    </tr>
  </tbody>
</table>
</div>



# Classification Methods

We'll cover five classification methods

1) Equal Interval
* Data is split to bins of equal width regardless of distribution

2) Quantiles
* Data is split by percentiles

3) Natural Breaks
* Data is split using the Jenks algorithm

4) Standard Deviation
* Data is split to bins based on distance from the mean

5) Manual Breaks
* We define our own splits

# Equal Interval

* The simplest classification scheme is to just break the data into classes of equal sizes
    * e.g. The minimum is .3 and the maximum is 9.8, so we can split that into four bins 2.4 units wide



<a href="EqualInterval_Hist.png" target="_blank">View Image in New Tab</a>

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="EqualInterval_Hist.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>


# Quantiles

<a href="Quantiled_Hist.png" target="_blank">View Image in New Tab</a>

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="Quantiled_Hist.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>






# Natural Breaks


<a href="NaturalBreaks_Map.png" target="_blank">View Image in New Tab</a>

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="NaturalBreaks_Map.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>




# Manual Breaks





# Standard Deviation







# Ratio to Ordinal





# Categorical
