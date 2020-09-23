import numpy as np
import pandas as pd
import geopandas as gpd
import jenkspy

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

can_province_abbrev = {
  'Alberta': 'AB',
  'British Columbia': 'BC',
  'Manitoba': 'MB',
  'New Brunswick': 'NB',
  'Newfoundland and Labrador': 'NL',
  'Northwest Territories': 'NT',
  'Nova Scotia': 'NS',
  'Nunavut': 'NU',
  'Ontario': 'ON',
  'Prince Edward Island': 'PE',
  'Quebec': 'QC',
  'Saskatchewan': 'SK',
  'Yukon': 'YT'
}
class GetData(object):
    """docstring for GetData"""
    def __init__(self):
        super(GetData, self).__init__()
        # self.scale = scale
        
        # Import Canadian Data

        self.CA_PoliceKillings = pd.read_csv('PoliceKillings_Canada_CBC_Updated.csv',
                                              parse_dates=['DATE'],
                                              index_col=['VICTIM ID']
                                             )
        self.CA_PoliceKillings=self.CA_PoliceKillings.set_index(pd.DatetimeIndex(self.CA_PoliceKillings['DATE']),
                                                      drop=True
                                             )

        CA_Census = pd.read_csv('Canadian_Census_2016.csv',
                                              index_col=['PRUID']
                                              )
        CA_Provinces= gpd.read_file('Canadian_Census_Boundaries_2016.shp').set_index('PRUID')

        dtype = 'int64'
        CA_Provinces.index = CA_Provinces.index.astype(dtype)
        CA_Provinces= CA_Provinces.join(CA_Census)
        CA_Provinces= CA_Provinces.rename(columns={'Caucasian':'White'})
        CA_Provinces= CA_Provinces.set_index('prov')


        # Import and Parse United States Data
        self.US_PoliceKillings =  pd.read_csv('PoliceKillings_US.csv',
                                              parse_dates=['Date of Incident (month/day/year)'],
                                              index_col=['MPV ID'],
                                              encoding= 'unicode_escape'
                                             )
        self.US_PoliceKillings=self.US_PoliceKillings.set_index(pd.DatetimeIndex(self.US_PoliceKillings['Date of Incident (month/day/year)']),
                                                      drop=True
                                             )
        self.US_PoliceKillings['RACE']=self.US_PoliceKillings["Victim's race"].replace({
            'Native American':'Indigenous',
            'Unknown race':'Unknown'})
        # self.US_PoliceKillings.loc[self.US_PoliceKillings["Victim's race"]=='Native America',"Victim's race"]='Indigenous'


        US_Census_Detailed =  pd.read_csv('US_Census_Data_2018.csv',skiprows=1,
                                              index_col=['id'],
                                             )
        vals = ['Geographic Area Name']
        rename = {'Geographic Area Name':'State'}
        for v in US_Census_Detailed.columns.values:
            if v.split('!!')[0]=='Estimate' and len(v.split('!!'))==5:
                if v.split('!!')[3]=='One race':
                    vals.append(v)
                    rename[v]=v.split('!!')[-1]
        US_Census = US_Census_Detailed[vals]
        US_Census=US_Census.rename(columns=rename)
        for i in US_Census_Detailed['Geographic Area Name']:
            US_Census.loc[US_Census['State']==i,'State']=us_state_abbrev[i]
        US_Census=US_Census.rename(columns={'Black or African American':'Black',
                                   'American Indian and Alaska Native':'Indigenous'})
        US_Census['Total']=US_Census_Detailed['Estimate!!SEX AND AGE!!Total population']
        US_Census['Mixed']=US_Census_Detailed['Estimate!!RACE!!Total population!!Two or more races']

        US_States= gpd.read_file('cb_2018_us_state_20m.shp').set_index('AFFGEOID')
        US_States= US_States.join(US_Census)
        US_States= US_States.set_index('STUSPS')

        self.CA_Length=(self.CA_PoliceKillings.index.max()-self.CA_PoliceKillings.index.min()).days/365.25
        self.US_Length=(self.US_PoliceKillings.index.max()-self.US_PoliceKillings.index.min()).days/365.25

        ## Subset CA_Provincesdata by province and join
        CA_Killings_By_Race = (self.CA_PoliceKillings.groupby(['PROV','RACE']).count()['AGE'].unstack())
        self.CA_PoliceKillings['Year'] = self.CA_PoliceKillings.index.year
        CA_Killings_By_Year = (self.CA_PoliceKillings.groupby(['PROV','Year']).count()['AGE'].unstack())

        #Join to the geodataframe

        self.CA = CA_Provinces.join(self.CA_PoliceKillings.groupby('PROV').count()["AGE"])
        self.CA = self.CA.rename(columns={'AGE':'Total_Killings'})
        self.CA = self.CA.join(CA_Killings_By_Race,rsuffix='_Killings')
        self.CA = self.CA.rename(columns={'Unknown':'Unknown_Killings'})
        self.CA = self.CA.join(CA_Killings_By_Year)


        ## Subset CA_Provincesdata by province and join
        US_Killings_By_Race = (self.US_PoliceKillings.groupby(['State',"RACE"]).count()["Victim's age"].unstack())
        self.US_PoliceKillings['Year'] = self.US_PoliceKillings.index.year
        US_Killings_By_Year = (self.US_PoliceKillings.groupby(['State','Year']).count()["Victim's age"].unstack())

        #Join to the geodataframe
        self.US = US_States.join(self.US_PoliceKillings.groupby('State').count()["Victim's age"])
        self.US = self.US.dropna()
        self.US = self.US.rename(columns={"Victim's age":'Total_Killings'})
        self.US = self.US.join(US_Killings_By_Race,rsuffix='_Killings')
        self.US = self.US.rename(columns={'Unknown':'Unknown_Killings'})
        self.US = self.US.join(US_Killings_By_Year)


    def ScaleData(self,scale=1,Categories=['Total','White','Black','Indigenous']):
        # Scale the data, fill the nulls, 
        Summary={}
        Summary['US']={}
        Summary['CA']={}
        for cat in Categories:
            if cat == 'Unknown':
                self.CA[cat+'_Rate']=self.CA[cat+'_Killings']/self.CA['Total']*scale/self.CA_Length
                self.US[cat+'_Rate']=self.US[cat+'_Killings']/self.US['Total']*scale/self.US_Length
                self.CA[cat+'_Rate']=self.CA[cat+'_Rate'].fillna(0)
                self.US[cat+'_Rate']=self.US[cat+'_Rate'].fillna(0)
                CA_Rate = self.CA[cat+'_Killings'].sum()/self.CA['Total'].sum()*scale/self.CA_Length
                US_Rate = self.US[cat+'_Killings'].sum()/self.US['Total'].sum()*scale/self.US_Length
            else:
                self.CA[cat+'_Rate']=self.CA[cat+'_Killings']/self.CA[cat]*scale/self.CA_Length
                self.US[cat+'_Rate']=self.US[cat+'_Killings']/self.US[cat]*scale/self.US_Length
                self.CA[cat+'_Rate']=self.CA[cat+'_Rate'].fillna(0)
                self.US[cat+'_Rate']=self.US[cat+'_Rate'].fillna(0)
                CA_Rate = self.CA[cat+'_Killings'].sum()/self.CA[cat].sum()*scale/self.CA_Length
                US_Rate = self.US[cat+'_Killings'].sum()/self.US[cat].sum()*scale/self.US_Length
            Summary['CA'][cat] = CA_Rate
            Summary['US'][cat] = US_Rate
        self.Summary = pd.DataFrame(data=Summary)
        # self.US_Summary = pd.DataFrame(data=Summary['US'])

    # return(self.CA,self.US)

    def NaturalBreaks(self,column,classes=5,labels=None):
        CA_Breaks = jenkspy.jenks_breaks(self.CA[column], nb_class=classes)
        self.CA[column+'_NB'] = pd.cut(self.CA[column],
                            bins=CA_Breaks,
                            labels=labels,
                            include_lowest=True,
                            duplicates='drop'
                                       )

        US_Breaks = jenkspy.jenks_breaks(self.US[column], nb_class=classes)
        self.US[column+'_NB'] = pd.cut(self.US[column],
                            bins=US_Breaks,
                            labels=labels,
                            include_lowest=True
                                       )
