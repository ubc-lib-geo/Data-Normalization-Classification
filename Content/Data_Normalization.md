---
layout: default
title: Data Normalization
nav_order: 3
---
# Data Normalization

Normalization, is the process of scaling (AKA Normalizing) one number by another:
* ie. To find get the proportion of Canada's population made up by each racial group, we need to know:
     * A) The population of each racial group
     * B) The total population
  * Dividing A by B, tells the percentage of Canada's population each demographic group makes up.

Comparing the Proportion of Police Killings for each demogrpahic group to their respective proporion of the population is informative
* However, its more meaningful to combine the police killings and population into one statistc: ###The Police Killing Rate (PKR)
  * The PKR is the number of police killings per unit of population (ie. million) per unit of time (ie. year)

For example, Canada's Total Police Killing Rate is 0.81 killings per million residents per year

<img src="https://render.githubusercontent.com/render/math?math= PKR = (\frac{556 Police Killings}{35,151,728 ppl}) x (\frac{1,000,000 ppl}{19.5 yr}) = 0.81 killings per million ppl per yr">

<!-- 
  This is how I wrote the equation in the .ipynb markdown cell.  It dosn't work here so I tried the img above
\begin{align}
\ PKR & = (\frac{556 Police Killings}{35,151,728 ppl}) x (\frac{1,000,000 ppl}{19.5 yr})$ \\
\end{2align} -->

This does not describe the whole picture, because there are large dispariteis in the police killing rate between demographic groups.
  * The PKR for Indigneous people is 2.76 killings per million people per year
  * The PKR for Black peopole is 2.05 killings per million people per year
  * The PKR for White peopole is 0.47 killings per million people per year

<a href="CA_Race_Normalized.png" target="_blank">View Image in New Tab</a>

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="CA_Race_Normalized.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>


We can normalize our data by demographic information at different administrative levels (eg. Province, Municipality)