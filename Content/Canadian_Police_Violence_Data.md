---
layout: default
title: Canadian Police Violence Data
nav_order: 2
---
# Canadian Police Violence Data

## Notes on Terminology

**Police Killing:** A death directly resulting from police use of force.  Including but not limited to: shooting, tazing, other use of force.

**Police-Involved Deaths**  Any civilian death at the hands of police or in the custody of police.  Includes police killings, and deaths resulting from police negligence/inaction: suicide, overdoses, medical emergencies, etc.  This is broader term that is more difficult to refute on the grounds of semantics.  

<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="CBC_screenshot.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="CBC_screenshot.png" target="_blank">View Image in New Tab</a>

*"There is no government database listing deaths at the hands of the police available to the public in Canada, so CBC News created its own. The CBC’s research librarians have collected detailed information on each case, such as ethnicity, the role of mental illness or substance abuse, the type of weapon used and the police service involved, to create a picture of who is dying in police encounters."*

A dataset covering January 2000 to December 2020 was collected by the [CBC](https://newsinteractives.cbc.ca/fatalpoliceencounters/). This is not an official or complete count, police in Canada are not mandated to collect/publish data regarding deaths.  This dataset is a collection of second-hand: press releases, news articles, etc.  Most records are incomplete.  Many more are missing (eg. ["starlight tour"](https://en.wikipedia.org/wiki/Saskatoon_freezing_deaths) deaths.  Further the dataset is not updated regularly.  The dataset was first published in 2018 but was not updated again until summer 2020.


<div style="overflow: hidden;
  padding-top: 56.25%;
  position: relative">
  <iframe src="KCC_screenshot.png" title="Processes" scrolling="no" frameborder="0"
    style="border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;">
   <p>Your browser does not support iframes.</p>
 </iframe>
</div>
<a href="KCC_screenshot.png" target="_blank">View Image in New Tab</a>

A more up to date record is available on [killercopscanada](https://killercopscanada.wordpress.com/), a WordPress blog run by an anonymous user that was started in 2015.  This blog contains 600+ posts pertaining to at least 400+ incidents, 200+ are missing from the CBC dataset.  We have combined these data sets into one, more comprehensive database.  

## Police involved deaths by year in Canada

2020 was a record-breaking year, with *at least* 74 police involved deaths.  There was a statistically significant (p<0.001) increasing trend of 2.6 killings/year over this period.  Is this trend real? Or an artifact of increased awareness and access to information?

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


## Age of the victims

Histograms show the shape and spread of a dataset.  Here we see the age distribution of victims in 5-year increments.  The histogram shows us that the age is slightly skewed towards older ages.

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

## What type of weapon (if any) did the victim have?
Over 45% of victims were unarmed.  **Note** Being Armed is does *not* justify any individual police killing.  However, in aggregate a higher number of killings of unarmed people can indicate a predisposition towards excessive use of force.

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


## Which police departments are responsible for the most deaths?
There are over 100 departments in the dataset, of which the 17 below are responsible for 73% of all the deaths. 

|Rank|               Department                |Province|Killings|
|---:|-----------------------------------------|--------|-------:|
|   1|RCMP                                     |BC      |     108|
|   2|Toronto Police Service                   |ON      |      71|
|   3|Ontario Provincial Police                |ON      |      52|
|   4|RCMP                                     |AB      |      50|
|   5|Sûreté du Québec                         |QC      |      47|
|   6|Edmonton Police Service                  |AB      |      43|
|   7|Service de police de la Ville de Montreal|QC      |      32|
|   8|Winnipeg Police Service                  |MB      |      31|
|   9|Calgary Police Service                   |AB      |      31|
|  10|Vancouver Police Department              |BC      |      27|
|  11|Peel Regional Police                     |ON      |      21|
|  12|RCMP                                     |SK      |      16|
|  13|Ottawa Police Service                    |ON      |      16|
|  14|York Regional Police                     |ON      |      12|
|  15|RCMP                                     |NU      |      10|
|  16|London Police Service                    |ON      |      10|
|  17|Hamilton Police Service                  |ON      |      10|


# 5) The racial breakdown of police killings.
You might hear someone say: "The majority of people killed by police in Canada are White".  This statement might not be false ... but it is also very misleading.

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


# Poll Questions:

### 3) What should we do to get a more accurate picture of the racial breakdown of police killings?
    A) Display the data alongside the proportion of Canada's total population each racial group comprises 
    B) Divide by the total number of police killings to get a percentage
    C) Subtract the Unknown category and then divide by the total number of police killings to get a percentage
    D) Divide the total killings of each racial group by the total population of each racial group
    

