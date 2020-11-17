---
layout: default
title: Canadian Police Violence Data
nav_order: 2
---
# Canadian Police Violence Data


This dataset covers January 2000 to June 2020 and was collected by the [CBC](https://newsinteractives.cbc.ca/fatalpoliceencounters/).  It is available for download at the bottom of the article.  
  "There is no government database listing deaths at the hands of the police available to the public in Canada, so CBC News created its own. The CBC’s research librarians have collected detailed information on each case, such as ethnicity, the role of mental illness or substance abuse, the type of weapon used and the police service involved, to create a picture of who is dying in police encounters. "
This is not an official count because police departments in Canada are not mandated to collect all of this information.  Rather this dataset is a collection of second hand information in the form of press releases, news articles, etc.  Some records are incomplete and the total number of incidents is higher than detailed here.  For example, this dataset does not include ["starlight tours"](https://en.wikipedia.org/wiki/Saskatoon_freezing_deaths), a heinous practce where police, most notably in Saskatoon, abduct indigenouos people during winter and drop them off in rural areas far from their homes.  Leaving them to freeze to death if they couldn't make it home. 
  * One issue with relying on a news corporation to collect this information, is that it is not updated at regular intervals.  The last time the dataset was updated prior to this summer was in 2017.  They updated it in 2020 after the killing of George Floyd.  But once the subject falls out of the news cycle, they have little incentive to continue.

Despite the incomplete nature of this dataset, it is best record available.  It is important to understand the pervasiveness of police violence in Canada, because this is a problem across North America, not just in the United States

# 1) Police killings by year in Canada
There were 556 killings between January 2000 - June 2020.  There was a statistically significant (p<0.001) increasing trend of 0.85 killings/year over this period.  As of this summer, 2020 was on pace to be a record breaking year.  

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
<a href="CA_Trendline.png" target="_blank">View Image in New Tab</a>


# 2) Age distribution of victims
Histograms show the shape and spread of a dataset.  Here we see the age distribution of victims in 5 year increments.  The histogram shows us that the age is slightly skewed towards older ages.  The mean age of victims is 35.6 and the standard deviation is 11.6.  The youngest victim was 15 and the oldest was 77

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
<a href="CA_AgeHist.png" target="_blank">View Image in New Tab</a>

# 3) What type of weapon (if any) did the victim have?
Nearly 30% of victims were unarmed.  Note - Being Armed is does not justify any individual police killing.  However, in aggregate a higher number of killings of unarmed people can indicate a predisposition towards excessive use of force.

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
<a href="CA_Weapon.png" target="_blank">View Image in New Tab</a>


# 4) Which police services are responsible for the most killings?
There are 74 police services listed in the dataset, of which 10 are responsible for 75% of all police killings.  The RCMP are the federal police and serve as the provincial police in eight provinces and the territories.  They are the deadliest police serive in Canada.  Large municipal police departments and provincial police are responsible for the majority of the rest police killings.

### Deadliest Police Departments in Canada
|Rank|               Department                |Killings|
|---:|-----------------------------------------|-------:|
|   1|RCMP                                     |     149|
|   2|Toronto Police Service                   |      56|
|   3|Service de police de la Ville de Montréal|      35|
|   4|Sûreté du Québec                         |      34|
|   5|Edmonton Police Service                  |      27|
|   6|Ontario Provincial Police                |      27|
|   7|Calgary Police Service                   |      26|
|   8|Vancouver Police Department              |      24|
|   9|Winnipeg Police Service                  |      21|
|  10|Peel Regional Police                     |      16|



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
<a href="PoliceViolenceIncidents.html" target="_blank">View map new tab</a>


# 5) The racial breakdown of police killings.
You might hear someone "The majority of people killied by police in Canada are White".  This statement isn't false ... but it is also very missleading.

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
<a href="CA_Race.png" target="_blank">View Image in New Tab</a>

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

