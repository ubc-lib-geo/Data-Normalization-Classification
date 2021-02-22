---
layout: default
title: Other Ways to Represent the Data
nav_order: 6
---

# Ordinal Data
Ratio data (eg. PKR) can be translated to or described as original data.  Sequential color schemes are a good choice for ordinal data as well.  The following is an example of ordinal data, but with a poor choice of category labels.  What does low, medium or high mean in this context?  


<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="Ordinal_Map_Bad_Labels.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="Ordinal_Map_Bad_Labels.png" target="_blank">View Image in New Tab</a>

Here is an example with better choices.  The categories give a good description of what the data is showing.  However, we can't infer anything about the differences between categories.

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="Ordinal_Map.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="Ordinal_Map.png" target="_blank">View Image in New Tab</a>


# Nominal Data
A nominal (categorical) variable can take on one of a limited number of possible values, assigning each record to a nominal category on the basis of a qualitative property.  When working with categorical data, avoid sequential and diverging colormaps, as they give the impression of an order or ranking in the data.  Choose a colormap designed for [categorical data](https://colorbrewer2.org/#type=qualitative&scheme=Accent&n=5).  You don't have to stick with the colors shown on color brewer, but they are a good starting point.

Race is an example of categorical data, and we can choose to attribute a categorical value to the provinces/states in a number of ways.  For instance, we could map the race making up the largest number of police killings in each province/state.


<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="MostNumerousRace_Map.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="MostNumerousRace_Map.png" target="_blank">View Image in New Tab</a>

However, this is a bit misleading, for reasons we discussed earlier.  Its not accounting for differential population.  It is more meaningful to map the race most likely to be killed by police in each state/province.  

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="HighestRateRace_Map.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="HighestRateRace_Map.png" target="_blank">View Image in New Tab</a>


# Poll Questions:
### 11) Which map gives a more truthful representation of the data? 
    A) Race of Majority of Police Killing Victims
    B) Race Most Likely to be Killed by Police


