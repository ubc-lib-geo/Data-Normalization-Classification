---
layout: default
title: Canadian Police Violence Data
nav_order: 2
---
# Canadian Police Violence Data


This data was collected by the CBC and is available for download [here](https://newsinteractives.cbc.ca/fatalpoliceencounters/)
    
* "There is no government database listing deaths at the hands of the police available to the public in Canada, so CBC News created its own. The CBC’s research librarians have collected detailed information on each case, such as ethnicity, the role of mental illness or substance abuse, the type of weapon used and the police service involved, to create a picture of who is dying in police encounters. "
    
    
* This is not an official count because police departments in Canada are not mandated to collect all of this information.  Rather this dataset is a collection of second hand information in the form of press releases, news articles, etc.  Some records are incomplete, and the total number of incidents is likely higher than detailed here.

# 1) Police killings by year
* There were 556 killings between January 2000 - June 2020
    * Increasing trend of 0.85 killings/year.
    * 2020 is on pace to be a record breaking year.

    <!-- CA_Trendline.png -->

<a href="CA_Trendline.png" target="_blank">View Image in New Tab</a>

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="CA_Trendline.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>

# 2) Age distribution of victims

Histograms show the shape and spread of a dataset.
* Here we see the age distribution of victims in 5 year increments.
    * The youngest was 15 and the oldest was 77
    * The mean age is 35.6, the standard deviation is 11.6
* The histogram shows us that the age is slightly skewed towards older ages
    * The distribution has a tail


<a href="CA_AgeHist.png" target="_blank">View Image in New Tab</a>

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="CA_AgeHist.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>

# 3) What type of weapon (if any) did the victim have?
* Nearly 30% of victims were unarmed.
    * Note - Being Armed is does not justify any individual police killing.
    * However, in aggregate a higher number of killings of unarmed people can indicate a predisposition towards excessive use of force.

<a href="CA_Weapon.png" target="_blank">View Image in New Tab</a>

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="CA_Weapon.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>


# 4) Which police departments are responsible for the most killings?
Here are all departments which have killed at least ten people in the last 20 years.
* Provincial police services and large municipal police departments are responsible for the most deaths
* The RCMP serves as the provincial police in eight provinces and the territories.
    * All together, the RCMP is responsible for 34% of deaths 

# 10 Deadliest Police Services

|               Police Service            |Provnce|Killings|
|-----------------------------------------|-------|-------:|
|RCMP                                     |BC     |      78|
|Toronto Police Service                   |ON     |      56|
|Service de police de la Ville de Montréal|QC     |      35|
|Sûreté du Québec                         |QC     |      34|
|RCMP                                     |AB     |      33|
|Edmonton Police Service                  |AB     |      27|
|Ontario Provincial Police                |ON     |      27|
|Calgary Police Service                   |AB     |      26|
|Vancouver Police Department              |BC     |      24|
|Winnipeg Police Service                  |MB     |      21|


<a href="PoliceViolenceIncidents.html" target="_blank">View map new tab</a>

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="PoliceViolenceIncidents.html" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>


# 5) The racial breakdown of police killings.
* "The majority of people killied by police in Canada are White".  This statement isn't false ... but it is very missleading.

<a href="CA_Race.png" target="_blank">View Image in New Tab</a>

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="CA_Race.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>


* Demographic groups are not evenly represented in the populations
    * Canada's population is 73.4% White, but they only account for 43.0% of police killings.
    * Canada's population only 4.7% Indigenous and 3.4% Black, but they account for 16.2% and 8.6% of police killings  
    * The victim's race is unreported 138 (24.8%) of the indidents.   



<a href="CA_Race_Proportional.png" target="_blank">View Image in New Tab</a>

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


# What would we excpect from a uniformm proportional distribution.

A [Chi Square](https://www.youtube.com/watch?v=2QeDRsxSF9M) test can be used to check if the observed number of police killings by racial group is significantly different than what we'd expect
ex. 

Here is an example for the country as a whole:

There were 556 police killings in Canada between Jan 2000 and June 2020, meaning the police killing rate was: 0.81 per million residents per year.
  * If Systemic Racism did not exist in Canada, as the RCMP commissioner claims ... This rate would apply to each demographic group. We can get the epxected distribution by multiplying the population of each demographic group by the average PKR and the record lenght (20.4 years).
  * The Chi Square test, will compare the expected and observed distribution to see if the deviations in the observed killings are beyond what would be randomly expected 
    * The test is significant to p =  5.2e-62
      * There is VERY STRONG evidence showing that there are systemic racial biases in police killings


Power_divergenceResult(statistic=304.9759918146094, pvalue=5.23539302248104e-62)
| By Race                     |   Total |   White |   Asian |   South Asian |   Indigenous |   Black |   Arab |   Latin American |   Visible minority, n.i.e | Unknown   |
|:----------------------------|--------:|--------:|--------:|--------------:|-------------:|--------:|-------:|-----------------:|--------------------------:|:----------|
| Total Population (Millions) |    35.1 |    25.8 |     3.2 |           1.9 |          1.6 |     1.1 |    0.5 |              0.4 |                       0.3 | --        |
| Expected Distribtuion       |   556   |   408   |    50   |          30   |         26   |    18   |    8   |              7   |                       5   | --        |
| Observed Killings           |   556   |   236   |    15   |          12   |         89   |    48   |    5   |              3   |                       5   | 127.0     |