---
layout: default
title: Canadian Police Violence Data
nav_order: 2
---
# Canadian Police Violence Data

This dataset covers January 2000 to June 2020 and was collected by the [CBC](https://newsinteractives.cbc.ca/fatalpoliceencounters/).  It is available for download at the bottom of the article.  

    "There is no government database listing deaths at the hands of the police available to the public in Canada, so CBC News created its own. The CBC’s research librarians have collected detailed information on each case, such as ethnicity, the role of mental illness or substance abuse, the type of weapon used and the police service involved, to create a picture of who is dying in police encounters. "

This is not an official count because police departments in Canada are not mandated to collect all of this information.  Rather this dataset is a collection of second-hand information in the form of press releases, news articles, etc.  Some records are missing or incomplete.  The total number of incidents is higher than detailed here.  For example, this dataset does not include the killings of Rodney Naistus and Lawrence Wegner in January and February 2000.
* Rodeny and Lawrence were victims ["starlight tours"](https://en.wikipedia.org/wiki/Saskatoon_freezing_deaths), a heinous practice where police, abduct indigenous people during winter and drop them off in rural areas far from their homes, leaving them to freeze to death if they couldn't make it home.  
* I have reached out to to the CBC for comment on why these incidents were omitted from the data set, but they were unable to give a clarify wheter this was an oversite or an intentional omission.

Another key issue with relying on a news corporation to collect this information, is that it is not updated at regular intervals.  The last time the dataset was updated prior to this summer was in 2017. They updated it in 2020 after the killing of George Floyd.  But once the subject falls out of the news cycle, they have little incentive to continue.
  * I have added incidents that were omitted in the Deady Force Article and updated it through December 2020 to the best of my abilities.  However, it is difficult to find information regarding police killings (esepecially historically) so my updates are also incomplete.

Despite the incomplete nature of this dataset, it is best record available.  It is important to understand the pervasiveness of police violence ans sytemic racism in policing in Canada, This is a problem across North America, not just in the United States.

# 1) Police killings by year in Canada

## 2020 was a record-breaking year, with *at least* 48 police involved killings.
There were *at least* 578 killings between January 2000 - November 2020.  There was a statistically significant (p<0.001) increasing trend of 1.04 killings/year over this period.  

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
Histograms show the shape and spread of a dataset.  Here we see the age distribution of victims in 5-year increments.  The histogram shows us that the age is slightly skewed towards older ages.  The mean age of victims is 35.6 and the standard deviation is 11.6.  The youngest victim was 15 and the oldest was 77

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
There are 74 police services listed in the dataset, of which 10 are responsible for 75% of all police killings.  The RCMP are the federal police and serve as the provincial police in eight provinces and the territories.  They are the deadliest police sericve in Canada.  Large municipal police departments and provincial police are responsible for the majority of the rest police killings.

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
You might hear someone say: "The majority of people killed by police in Canada are White".  This statement isn't false ... but it is also very misleading.

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
    

