---
layout: default
title: Data Normalization
nav_order: 3
---
# Data Normalization

Demographic groups are not evenly represented in the population.  Canada's population is 73.4% White, but White people only account for 43.0% of police killings.  Meanwhile, Canada's population only 4.7% Indigenous and 3.4% Black, but these groups account for 16.2% and 8.6% of police killings respectively.  The victim's race is unreported 138 (24.8%) of the indidents, this means the numbers for across racial groups are likely higher than reported.

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="CA_Race_Proportional.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="CA_Race_Proportional.png" target="_blank">View Image in New Tab</a>

In order to adquately acount for this, we need to Normalize our data.  Normalization, is the process of scaling one variable by another.  For example, to find get the proportion of Canada's population made up by each racial group, we can divide the population of each racial group by the total population.  This tells the percentage of Canada's population each racial group makes up.  Normalizing by the sum of a dataset is the simplest example of data nromalization.  Doing the same opperation to the police killings data allows us to plot them side by side because they are on the same sale (Percentage).

Comparing the proportion of police killings for each demogrpahic group to their respective proporion of the population is informative.  However, its more meaningful to combine the police killings and the population into one statistc.

### The Police Killing Rate (PKR):
  * The PKR is the number of police killings per unit of population (ie. million) per unit of time (ie. year)

For example, Canada's Total Police Killing Rate is 0.81 killings per million residents per year

<!-- ![\Large PKR = (\frac{556 Police Killings}{35,151,728 ppl}) x (\frac{1,000,000 ppl}{19.5 yr}) = 0.81 killings per million ppl per yr] -->
(<a href="https://www.codecogs.com/eqnedit.php?latex=PKR&space;=&space;(\frac{556&space;Police&space;Killings}{35,151,728&space;ppl})&space;x&space;(\frac{1,000,000&space;ppl}{19.5&space;yr})&space;=&space;0.81&space;killings&space;per&space;million&space;ppl&space;per&space;yr" target="_blank"><img src="https://latex.codecogs.com/gif.latex?PKR&space;=&space;(\frac{556&space;Police&space;Killings}{35,151,728&space;ppl})&space;x&space;(\frac{1,000,000&space;ppl}{19.5&space;yr})&space;=&space;0.81&space;killings&space;per&space;million&space;ppl&space;per&space;yr" title="PKR = (\frac{556 Police Killings}{35,151,728 ppl}) x (\frac{1,000,000 ppl}{19.5 yr}) = 0.81 killings per million ppl per yr" /></a>)

This does not describe the whole picture, because there are large dispariteis in the police killing rate between demographic groups.  The PKR for Indigneous and Black people are 2.76 and 2.05 per million people per year.  The PKR for White people is 0.47 per million people per year.


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
<a href="CA_Race_Normalized.png" target="_blank">View Image in New Tab</a>




# What would we excpect from a uniform proportional distribution?

A [Chi Square](https://www.youtube.com/watch?v=2QeDRsxSF9M) test can be used to check if the observed number of police killings by racial group is significantly different than what we'd expect
ex. 

Here is an example for the country as a whole:

There were 556 police killings in Canada between Jan 2000 and June 2020, meaning the police killing rate was: 0.81 per million residents per year.
  * If Systemic Racism did not exist in Canada, as the RCMP commissioner claims ... This rate would apply to each demographic group. We can get the epxected distribution by multiplying the population of each demographic group by the average PKR and the record lenght (20.4 years).
  * The Chi Square test, will compare the expected and observed distribution to see if the deviations in the observed killings are beyond what would be randomly expected.
    * The test is significant to p < 0.0001, meaning there is VERY STRONG evidence showing that there are systemic racial biases in police killings.



|                         | Total Population (Millions)   | Expected Distribtuion   |   Observed Killings |
|:------------------------|:------------------------------|:------------------------|--------------------:|
| Total                   | 35.1                          | 556.0                   |                 556 |
| White                   | 25.8                          | 408.0                   |                 239 |
| Asian                   | 3.2                           | 50.0                    |                  16 |
| South Asian             | 1.9                           | 30.0                    |                  12 |
| Indigenous              | 1.6                           | 26.0                    |                  90 |
| Black                   | 1.1                           | 18.0                    |                  48 |
| Arab                    | 0.5                           | 8.0                     |                   5 |
| Latin American          | 0.4                           | 7.0                     |                   3 |
| Visible minority, n.i.e | 0.3                           | 5.0                     |                   5 |
| Unknown                 | --                            | --                      |                 138 |

