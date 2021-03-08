---
layout: default
title: Data Classification
nav_order: 5
---

# Data Classification: Histograms, Classification Schemes & Choropleth Mapping

# Data Types
There are two kinds of data, that both have two sub-types.  Qualitative (descriptive) data includes Nominal and Ordinal Data types.  Nominal data is categorical data with no inherent ranking.  Ordinal data is categorical data that does have a rank.  Quantitative (numeric) data includes Ratio and Interval Data.  Interval data is similar to ratio data, but it lacks an absolute zero point.  Ratio data has an absolute zero point and the difference between values is meaningful.  PKR is ratio data, it can't be negative and a PKR of 2 is twice as high as a PKR of 1.


<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="DataTypes.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="DataTypes.png" target="_blank">View Image in New Tab</a>

# Rates by Province/State
We can normalize our data by demographic information at different administrative levels (eg. Province, Municipality) because PKR varies by administrative divisions.  If we want to classify rates, the first step is to look at a histogram.  A Histogram shows us the frequency distribution of a given variable.  Data is grouped into a set of bins and counted.


<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="Combined_Rate_Hist.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="Combined_Rate_Hist.png" target="_blank">View Image in New Tab</a>

# Outliers
Histograms can be useful for spotting outliers in a dataset.  The Indigenous Police Killing rate histogram for the US shows an outlier.  Vermont has a rate many times higher than the nearest value.  This is because the at 1743 individuals, the Indigenoous population of Vermont only makes up 0.3% of the states population.  So one killing diruing this time period leads to a very high PKR.

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="Combined_Hist_by_Race.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="Combined_Hist_by_Race.png" target="_blank">View Image in New Tab</a>

# Classification Methods

We'll cover five classification methods

1) Equal Interval
* Data is split to bins of equal width regardless of distribution

2) Quantiles
* Data is split by percentiles

3) Natural Breaks
* Data is split using the Jenks algorithm

4) Manual Breaks
* We define our own splits

5) Standard Deviation
* Data is split to bins based on distance from the mean

### A note on color choices
Sequential colormaps are the best choice for representing ratio data (eg. PKR).  I suggest you check out [color brewer](https://colorbrewer2.org/#type=sequential&scheme=OrRd&n=5) for help picking out color schemes. 

# Equal Interval
The simplest classification scheme is to just break the data into classes of equal sizes e.g. The minimum is 0.3 and the maximum is 10.6, so we can split that into four bins 2.6 units wide.

### Nunavut has the highest Police Killing Rate of any administrative sub-division in Canada or the United States.   The numbers presented here are contradicted by the [CBC's own reporting](https://www.cbc.ca/news/canada/north/nunavut-police-related-death-rate-high-data-1.5645619).  This article suggests the death rates may be much higher across the north than presented here.

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="EqualInterval_Map.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="EqualInterval_Map.png" target="_blank">View Image in New Tab</a>


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
<a href="EqualInterval_Hist.png" target="_blank">View Image in New Tab</a>




# Quantiles
The simplest classification scheme that is based of nthe data distribution.  The data is ranked and broken up by percentiles:
  * class 1 contains 0-20%, class 2 is 20-40%, class 3 is 40-60%, class 4 is 60-80%, & class 5 is 80-100%


<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="Quantile_Map.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="Quantile_Map.png" target="_blank">View Image in New Tab</a>


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
<a href="Quantiled_Hist.png" target="_blank">View Image in New Tab</a>

# Natural Breaks
Data is split using the [Jenks algorithm](http://wiki.gis.com/wiki/index.php/Jenks_Natural_Breaks_Classification).  This algorithm optimizes the data split into "Natural" classes.  The algorithm maximizes within group similarity and between group dissimilarity


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
<a href="NaturalBreaks_Map.png" target="_blank">View Image in New Tab</a>



<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="NaturalBreaks_Hist.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="NaturalBreaks_Hist.png" target="_blank">View Image in New Tab</a>

# Manual Breaks
We can define our own break values to classify data.  This allows us to choose more meaningful break values if necessary (round numbers, clean fractions, etc.  The choice of manual breaks can influence the way the data is perceived.

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="ManualBreaks_Map.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="ManualBreaks_Map.png" target="_blank">View Image in New Tab</a>


<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="ManualBreaks_Hist.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="ManualBreaks_Hist.png" target="_blank">View Image in New Tab</a>

# Standard Deviation
This distribution-based classification method shows how far a value is from the mean in standard deviations.  It can be very informative to a knowledgeable user, but it is not particularly accessible for the general public.  The standard deviation classification method converts the data to interval data (deviations above/below the mean).  [Diverging colormaps](https://colorbrewer2.org/#type=diverging&scheme=RdBu&n=5) are a better choice for interval data in many instances, as they can better highlight what values are above or below the zero point.


<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="STDBreaks_Map.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="STDBreaks_Map.png" target="_blank">View Image in New Tab</a>


<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="STDBreaks_Hist.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="STDBreaks_Hist.png" target="_blank">View Image in New Tab</a>


# Poll Questions:

### 9) If you want to highlight the severity of systemic racism in policing, which classification method would be best?
    A) Equal Interval
    B) Quantiles
    C) Natural Breaks
    D) Manual Breaks
    E) Standard Deviation
    
### 10) What classification method might the RCMP choose to minimize the severity of systemic racism in policing?
    A) Equal Interval
    B) Quantiles
    C) Natural Breaks
    D) Manual Breaks
    E) Standard Deviation







