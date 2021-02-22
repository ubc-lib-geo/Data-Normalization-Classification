---
layout: default
title: Data Normalization
nav_order: 3
---
# Data Normalization

Demographic groups are not evenly represented in the population.  Canada's population is 73.4% White, but White people only account for 41.5% of police killings.  Meanwhile, Canada's population is only 4.8% Indigenous and 3.4% Black, but these groups account for 17.0% and 8.4% of police killings respectively.  The victim's race is unreported 150 (25.8%) of the incidents, this means the numbers for across racial groups are likely higher than reported.

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

In order to adequately account for this, we need to Normalize our data.  Normalization, is the process of scaling one variable by another.  For example, to find get the proportion of Canada's population made up by each racial group, we can divide the population of each racial group by the total population.  This tells the percentage of Canada's population each racial group makes up.  Normalizing by the sum of a dataset is the simplest example of data normalization.  Doing the same operation to the police killings data allows us to plot them side by side because they are on the same sale (Percentage).

Comparing the proportion of police killings for each demographic group to their respective proportion of the population is informative.  However, its more meaningful to combine the police killings and the population into one statistic.

### The Police Killing Rate (PKR):
The PKR is the number of police killings per unit of population (ie. million) per unit of time (ie. year).  For example, Canada's Total Police Killing Rate is 0.79 killings per million residents per year.

<a href="https://www.codecogs.com/eqnedit.php?latex=PKR&space;=&space;(\frac{581&space;Police&space;Killings}{35,151,728&space;ppl})&space;x&space;(\frac{1,000,000&space;ppl}{21&space;yr})&space;=&space;0.79&space;/&space;million&space;ppl&space;/&space;yr" target="_blank"><img src="https://latex.codecogs.com/gif.latex?PKR&space;=&space;(\frac{581&space;Police&space;Killings}{35,151,728&space;ppl})&space;x&space;(\frac{1,000,000&space;ppl}{21&space;yr})&space;=&space;0.79&space;/&space;million&space;ppl&space;/&space;yr" title="PKR = (\frac{581 Police Killings}{35,151,728 ppl}) x (\frac{1,000,000 ppl}{21 yr}) = 0.79 / million ppl / yr" /></a>


This does not describe the whole picture, because there are large disparities in the police killing rate between demographic groups.  The PKR for Indigenous and Black people are **2.82** and **1.95** per million people per year.  The PKR for White people is 0.44 per million people per year.


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




# Statistical Testing

What would we expect from a uniform proportional distribution?  A [Chi Square](https://www.youtube.com/watch?v=2QeDRsxSF9M) test can be used to check if the observed number of police killings by racial group is significantly different than what would be expect if the PKR were equal between racial groups.  Here is an example for the country as a whole.

There were 579 police killings in Canada between January 2000 and December 2020, meaning the police killing rate was: 0.78 per million residents per year.
  * If Systemic Racism did not exist in Canada, as the RCMP commissioner Brenda Lucki claimed ... This rate would apply to each demographic group. We can get the expected distribution by multiplying the population of each demographic group by the average PKR and the record length (21 years).
  * The Chi Square test, will compare the expected and observed distribution to see if the deviations in the observed killings are beyond what would be randomly expected.
    * The test is significant to p < 0.0001, meaning there is **VERY STRONG** evidence showing that there are systemic racial biases in police killings.


|                         | Total Population (Millions)   | Expected Distribtuion   |   Observed Killings |
|:------------------------|:------------------------------|:------------------------|--------------------:|
| Total                   | 35.1                          | 581.0                   |                 581 |
| White                   | 25.8                          | 426.0                   |                 241 |
| Asian                   | 3.2                           | 53.0                    |                  17 |
| South Asian             | 1.9                           | 31.0                    |                  12 |
| Indigenous              | 1.6                           | 27.0                    |                  99 |
| Black                   | 1.1                           | 19.0                    |                  49 |
| Arab                    | 0.5                           | 8.0                     |                   5 |
| Latin American          | 0.4                           | 7.0                     |                   3 |
| Visible minority, n.i.e | 0.3                           | 6.0                     |                   5 |
| Unknown                 | --                            | --                      |                 150 |

# Poll Questions:

### 4) Do you think this pattern contiunes at the municipal department level?
    A) Yes
    B) No
    C) Unsure
    

### 5) What impact do you think the missing data (Unknown race) has on this Chi Squared Analysis?
    A) Invialidates the results
    B) The racial disparities are likely greater than indicated
    C) The racial dispariteis are likely less than indicated
    D) Minimal impact, the race of Unknown victims is probably distributed similarly to those of known race