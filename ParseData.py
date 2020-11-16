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


class GetData(object):
    """docstring for GetData"""
    def __init__(self):
        super(GetData, self).__init__()

        self.can_province_names = {
          'AB': 'Alberta',
          'BC': 'British Columbia',
          'MB': 'Manitoba',
          'NB': 'New Brunswick',
          'NL': 'Newfoundland and Labrador',
          'NS': 'Nova Scotia',
          'NT': 'Northwest Territories',
          'NU': 'Nunavut',
          'ON': 'Ontario',
          'PE': 'Prince Edward Island',
          'QC': 'Quebec',
          'SK': 'Saskatchewan',
          'YT': 'Yukon'
        }
        self.can_province_abbrev = {
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
        # Import Canadian Data

        self.CA_PoliceKillings = pd.read_csv('Inputs/PoliceKillings_Canada_CBC_Updated.csv',
                                              parse_dates=['DATE'],
                                              index_col=['VICTIM ID']
                                             )
        self.CA_PoliceKillings=self.CA_PoliceKillings.set_index(pd.DatetimeIndex(self.CA_PoliceKillings['DATE']),
                                                      drop=True
                                             )
        self.CA_PoliceKillings['ARMED TYPE'] =  self.CA_PoliceKillings['ARMED TYPE'].replace({
                                'Air gun, replica gun':'Other weapons',
                                'Bat, club, other swinging object':'Other weapons',
                                'Vehicle':'Other weapons',
                                'Knife, axe, other cutting instruments':'Knife',
                                'Unknown':'None',
                                'Chemical or sprays':'Other weapons'})

        self.CA_PoliceKillings['RACE'] =  self.CA_PoliceKillings['RACE'].replace({
                                'Other':'Visible minority, n.i.e',
                                'Caucasian':'Visible minority, n.i.e'})
        self.CA_PoliceKillings.RACE.fillna('Unknown',inplace=True)

        self.CA_PoliceKillings['POLICE SERVICE'] =  self.CA_PoliceKillings['POLICE SERVICE'].replace({
        #                         'Service de police de la Ville de Lévis, Sûreté du Québec':'Service de police de la Ville de Lévis',
        #                         'Sûreté du Québec':'SQ',
                                'Peterborough Lakefield Community Police Force':'Peterborough Police Service',
                                'OPP':'Ontario Provincial Police',
        #                         # 'Service de police de la Ville de Montréal':'Montreal Police Service'
                                })
        

        CA_Census = pd.read_csv('Inputs/Canadian_Census_2016.csv',
                                              index_col=['PRUID']
                                              )

        CA_Census =  CA_Census.rename(columns={
            'Caucasian':'White'})
        CA_Census['Asian'] = CA_Census['Chinese']+CA_Census['Filipino']+CA_Census['West Asian']+\
        CA_Census['Japanese']+CA_Census['Korean']+CA_Census['Southeast Asian']
        CA_Census = CA_Census.drop(['Chinese','Filipino','West Asian','Japanese','Korean','Southeast Asian'],axis=1)
        CA_Census['Unknown'] = 0

        CA_Census['Visible minority, n.i.e'] = CA_Census['Visible minority, n.i.e']+CA_Census['Multiple visible minorities']
        CA_Census = CA_Census.drop(['Multiple visible minorities'],axis=1)

        CA_Provinces= gpd.read_file('Inputs/Canadian_Census_Boundaries_2016.shp').set_index('PRUID')

        dtype = 'int64'
        CA_Provinces.index = CA_Provinces.index.astype(dtype)
        CA_Provinces= CA_Provinces.join(CA_Census)
        # CA_Provinces= CA_Provinces.rename(columns={'Caucasian':'White'})
        CA_Provinces= CA_Provinces.set_index('prov')



        Municipal = pd.read_csv('Inputs/Municipal_Data.csv',index_col=['GEO UID'],
                                                      encoding= 'utf-8')
        Municipal.loc[Municipal['Caucasian']<0,'Caucasian']=0
        
        Municipal =  Municipal.rename(columns={
            'Caucasian':'White'})
        Municipal['Asian'] = Municipal['Chinese']+Municipal['Filipino']+Municipal['West Asian']+\
        Municipal['Japanese']+Municipal['Korean']+Municipal['Southeast Asian']
        Municipal = Municipal.drop(['Chinese','Filipino','West Asian','Japanese','Korean','Southeast Asian'],axis=1)
        Municipal['Unknown'] = 0

        Municipal['Visible minority, n.i.e'] = Municipal['Visible minority, n.i.e']+Municipal['Multiple visible minorities']
        Municipal = Municipal.drop(['Multiple visible minorities'],axis=1)






        Municipal_Boundaries=gpd.read_file('Inputs/lcsd000a14a_e.shp')
        Municipal_Boundaries = Municipal_Boundaries.set_index(
            Municipal_Boundaries['CSDUID'].astype(
            Municipal.index.dtype))


        self.Municipal_Boundaries=Municipal_Boundaries.join(Municipal)
        self.Municipal_Boundaries['PROV']=self.Municipal_Boundaries['PRNAME'].str.split(' / ',expand=True)[0]
        # self.Municipal_Boundaries = self.Municipal_Boundaries.rename(columns={
        #     'Caucasian':'White'})
        self.Municipal_Boundaries['Name']=self.Municipal_Boundaries['Name'].astype(str).str[:-1]


        # Import and Parse United States Data
        self.US_PoliceKillings =  pd.read_csv('Inputs/PoliceKillings_US.csv',
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
        self.US_PoliceKillings['Unarmed/Did Not Have an Actual Weapon']=self.US_PoliceKillings['Unarmed/Did Not Have an Actual Weapon'].replace({
            'Unclear':'Unarmed',
            'Unarmed/Did Not Have an Actual Weapon':'Unarmed'
            })
        # self.US_PoliceKillings.loc[self.US_PoliceKillings["Victim's race"]=='Native America',"Victim's race"]='Indigenous'

        self.US_PoliceKillings['AGE']=self.US_PoliceKillings["Victim's age"].replace({
            'Unknown':np.nan,'40s':np.nan}).astype(float)


        US_Census_Detailed =  pd.read_csv('Inputs/US_Census_Data_2018.csv',skiprows=1,
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

        US_States= gpd.read_file('Inputs/cb_2018_us_state_20m.shp').set_index('AFFGEOID')
        US_States= US_States.join(US_Census)
        US_States= US_States.set_index('STUSPS')

        self.CA_Length=(self.CA_PoliceKillings.index.max()-self.CA_PoliceKillings.index.min()).days/365.25
        self.US_Length=(self.US_PoliceKillings.index.max()-self.US_PoliceKillings.index.min()).days/365.25

        ## Subset CA_Provincesdata by province and join
        CA_Killings_By_Race = (self.CA_PoliceKillings.groupby(['PROV','RACE']).count()['GENDER'].unstack())
        self.CA_PoliceKillings['Year'] = self.CA_PoliceKillings.index.year
        CA_Killings_By_Year = (self.CA_PoliceKillings.groupby(['PROV','Year']).count()['GENDER'].unstack())

        #Join to the geodataframe

        self.CA = CA_Provinces.join(self.CA_PoliceKillings.groupby('PROV').count()["GENDER"])
        self.CA = self.CA.rename(columns={'GENDER':'Total_Killings'})
        self.CA = self.CA.join(CA_Killings_By_Race,rsuffix='_Killings')
        # self.CA = self.CA.rename(columns={'Unknown':'Unknown_Killings'})
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
        Combined = Categories.copy()
        for cat in Categories:
            if cat == 'Unknown':
                self.CA[cat+'_Rate']=self.CA[cat+'_Killings']/self.CA['Total']*scale/self.CA_Length
                self.US[cat+'_Rate']=self.US[cat+'_Killings']/self.US['Total']*scale/self.US_Length
                self.CA[cat+'_Rate']=self.CA[cat+'_Rate'].fillna(0)
                self.US[cat+'_Rate']=self.US[cat+'_Rate'].fillna(0)
                CA_Rate = self.CA[cat+'_Killings'].sum()/self.CA['Total'].sum()*scale/self.CA_Length
                US_Rate = self.US[cat+'_Killings'].sum()/self.US['Total'].sum()*scale/self.US_Length
                Combined.append(cat+'_Killings')
                Combined.append(cat+'_Rate')
            else:
                self.CA[cat+'_Rate']=self.CA[cat+'_Killings']/self.CA[cat]*scale/self.CA_Length
                self.US[cat+'_Rate']=self.US[cat+'_Killings']/self.US[cat]*scale/self.US_Length
                self.CA[cat+'_Rate']=self.CA[cat+'_Rate'].fillna(0)
                self.US[cat+'_Rate']=self.US[cat+'_Rate'].fillna(0)
                CA_Rate = self.CA[cat+'_Killings'].sum()/self.CA[cat].sum()*scale/self.CA_Length
                US_Rate = self.US[cat+'_Killings'].sum()/self.US[cat].sum()*scale/self.US_Length
                Combined.append(cat+'_Killings')
                Combined.append(cat+'_Rate')
            Summary['CA'][cat] = CA_Rate
            Summary['US'][cat] = US_Rate
        self.Summary = pd.DataFrame(data=Summary)
        Combined.append('geometry')
        self.Combined=self.CA[Combined].append(self.US[Combined])


    def Breaks(self,column,classes=5,labels=None,Manual_Bins=None,STD_i = 1):
        self.CA_jenks = jenkspy.jenks_breaks(self.CA[column], nb_class=classes)
        self.CA[column+'_NB'] = pd.cut(self.CA[column],
                            bins=self.CA_jenks,
                            labels=labels,
                            include_lowest=True,
                            duplicates='drop'
                                       )

        self.US_jenks = jenkspy.jenks_breaks(self.US[column], nb_class=classes)
        self.US[column+'_NB'] = pd.cut(self.US[column],
                            bins=self.US_jenks,
                            labels=labels,
                            include_lowest=True
                                       )

        self.Combined_jenks = jenkspy.jenks_breaks(self.Combined[column], nb_class=classes)
        self.Combined[column+'_NB'] = pd.cut(self.Combined[column],
                            bins=self.Combined_jenks,
                            labels=labels,
                            include_lowest=True
                                       )

    # Quantiles
        self.classes = classes
        self.CA[column+'_QB'] = pd.qcut(self.CA[column],
                            q=self.classes,
                            duplicates='drop'
                                       )

        self.US[column+'_QB'] = pd.qcut(self.US[column],
                            q=self.classes,
                            duplicates='drop'
                                       )

        self.Combined[column+'_QB'] = pd.qcut(self.Combined[column],
                            q=self.classes,
                            duplicates='drop'
                                       )

        # Equal Intervals
        import math
        # start = math.floor(min(self.US[column].min(),self.CA[column].min())*10)/10\
        start = 0
        end = math.ceil(max(self.US[column].max(),self.CA[column].max())*10)/10
        freq = (end-start)/classes


        self.EB_bins= np.linspace(start,end,classes+1)
                            
        self.CA[column+'_EB'] = pd.cut(self.CA[column],
                            bins=pd.interval_range(start=start,freq=freq,end=end,closed='neither'),
                            labels=labels,
                            include_lowest=True,
                            duplicates='drop'
                                       )

        self.US[column+'_EB'] = pd.cut(self.US[column],
                            bins=pd.interval_range(start=start,freq=freq,end=end,closed='neither'),
                            labels=labels,
                            include_lowest=True,
                            duplicates='drop'
                                       )

        self.Combined[column+'_EB'] = pd.cut(self.Combined[column],
                            bins=pd.interval_range(start=start,freq=freq,end=end,closed='neither'),
                            labels=labels,
                            include_lowest=True,
                            duplicates='drop'
                                       )

        # Manual Breaks
        if Manual_Bins != None:
            self.Manual_Bins = Manual_Bins
            self.CA[column+'_MB'] = pd.cut(self.CA[column],
                                bins=self.Manual_Bins,
                                labels=labels,
                                include_lowest=True,
                                duplicates='drop'
                                           )

            self.US[column+'_MB'] = pd.cut(self.US[column],
                                bins=self.Manual_Bins,
                                labels=labels,
                                include_lowest=True,
                                duplicates='drop'
                                           )

            self.Combined[column+'_MB'] = pd.cut(self.Combined[column],
                                bins=self.Manual_Bins,
                                labels=labels,
                                include_lowest=True,
                                duplicates='drop'
                                           )
        

        self.CA['STD'] = (self.CA[column]-self.CA[column].mean())/self.CA[column].std()
        bins = np.arange(0,max(self.CA['STD'].min()*-1,self.CA['STD'].max())+STD_i,STD_i)
        self.CA_STD_bins = (np.append(bins[::-1][:-1]*-1,bins))
        self.CA[column+'_STD'] = pd.cut(self.CA['STD'],
                            bins=self.CA_STD_bins,
                            duplicates='drop'
                                       )

        self.US['STD'] = (self.US[column]-self.US[column].mean())/self.US[column].std()
        bins = np.arange(0,max(self.US['STD'].min()*-1,self.US['STD'].max())+STD_i,STD_i)
        self.US_STD_bins = (np.append(bins[::-1][:-1]*-1,bins))
        self.US[column+'_STD'] = pd.cut(self.US['STD'],
                            bins=self.US_STD_bins,
                            duplicates='drop'
                                       )

        self.Combined['STD'] = (self.Combined[column]-self.Combined[column].mean())/self.Combined[column].std()
        bins = np.arange(0,max(self.Combined['STD'].min()*-1,self.Combined['STD'].max())+STD_i/.5,STD_i)
        self.Combined_STD_bins = (np.append(bins[::-1][:-1]*-1,bins))
        self.Combined[column+'_STD'] = pd.cut(self.Combined['STD'],
                            bins=self.Combined_STD_bins,
                            duplicates='drop'
                                       )