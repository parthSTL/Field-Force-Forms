import requests, getpass
import pandas as pd
import sqlite3
import os
import shutil
# password=getpass.getpass() # Privacy for Password
password=''
# API of HDD TFiber form
r = requests.get('https://nssbsurvey.sterliteapps.com/api/v1/data/s49_2087', auth=('parth.pandey@stl.tech', password))
# print(r.status_code)
data=r.json() # Fetching Data from API
df=pd.DataFrame(data)

# Removing column Coordinates and including it in a float object
# df['start_lat'] = df.apply(lambda row: row.Start_Point['coordinates'][0]  , axis = 1)
# df['start_long']=df.apply(lambda row: row.Start_Point['coordinates'][1], axis=1)
# df['end_lat']=df.apply(lambda row: row.End_Point['coordinates'][0], axis=1)
# df['end_long']=df.apply(lambda row: row.End_Point['coordinates'][1], axis=1)

def lat(geoloc, man_lat):
    if len(geoloc)>0:
        s= str(geoloc['coordinates'][1])
        return s[:9]
    else:
        if len(man_lat)>9:
            return man_lat[:9]
        else:
            return man_lat
def long(geoloc, man_long):
    if len(geoloc)>0:
        s=str(geoloc['coordinates'][0])
        return s[:9]
    else:
        if len(man_long)>9:
            return man_long[:9]
        else:
            return man_long

df['start_lat'] = df.apply(lambda row: lat(row['Start_Point'],row['Start_Point_Manual_Latitude'])  , axis = 1)
df['start_long']=df.apply(lambda row: long(row['Start_Point'],row['Start_Point_Manual_Longitude'])  , axis = 1)
df['end_lat'] = df.apply(lambda row: lat(row['End_Point'],row['End_Point_Manual_Latitude'])  , axis = 1)
df['end_long']=df.apply(lambda row: long(row['End_Point'],row['End_Point_Manual_Longitude'])  , axis = 1)
df = df.drop('End_Point_Manual_Longitude', axis=1)
df = df.drop('End_Point_Manual_Latitude', axis=1)
df = df.drop('End_Point', axis=1)
df = df.drop('Start_Point_Manual_Longitude', axis=1)
df = df.drop('Start_Point_Manual_Latitude', axis=1)
df = df.drop('Start_Point', axis=1)
df=df.drop('_geolocation',axis=1)
df.columns = df.columns.str.replace(" ", "") # What was the need
df['prikey']=pd.to_numeric(df['prikey'])

# DIT Form
r1 = requests.get('https://nssbsurvey.sterliteapps.com/api/v1/data/s49_2094', auth=('parth.pandey@stl.tech', password))
data=r1.json() # Fetching Data from API
df1=pd.DataFrame(data)


df1['prikey']=pd.to_numeric(df1['prikey'])
df1['coupler_lat'] = df1.apply(lambda row: lat(row['coupler_location'],row['coupler_location_manual_lat'])  , axis = 1)
df1['coupler_long']=df1.apply(lambda row: long(row['coupler_location'],row['coupler_location_manual_long'])  , axis = 1)
df1 = df1.drop('coupler_location_manual_long', axis=1)
df1 = df1.drop('coupler_location_manual_lat', axis=1)
df1 = df1.drop('coupler_location',axis= 1)
df1=df1.drop('_geolocation',axis=1)
df1.columns = df1.columns.str.replace(" ", "") # What was the need


# # Blowing Form
r2 = requests.get('https://nssbsurvey.sterliteapps.com/api/v1/data/s49_2022', auth=('parth.pandey@stl.tech', password))
data=r2.json() # Fetching Data from API
df2=pd.DataFrame(data)
df2.columns = df2.columns.str.replace(" ", "") # What was the need
df2['prikey']=pd.to_numeric(df2['prikey'])

# DRT Form
r3 = requests.get('https://nssbsurvey.sterliteapps.com/api/v1/data/s49_2072', auth=('parth.pandey@stl.tech', password))
data=r3.json() # Fetching Data from API
df3=pd.DataFrame(data)

df3['chamber1_lat'] = df3.apply(lambda row: lat(row['Chamber1_Location_Point'],row['Chamber1_Manual_Latitude'])  , axis = 1)
df3['chamber1_long']=df3.apply(lambda row: long(row['Chamber1_Location_Point'],row['Chamber1_Manual_Longitude'])  , axis = 1)
df3['chamber2_lat'] = df3.apply(lambda row: lat(row['Chamber2_location_Point'],row['Chamber2_Manual_Latitude'])  , axis = 1)
df3['chamber2_long']=df3.apply(lambda row: long(row['Chamber2_location_Point'],row['Chamber2_Manual_Longitude'])  , axis = 1)
df3['Duct_dam_punct_lat'] = df3.apply(lambda row: lat(row['Duct_dam_punct_loc_point'],row['Duct_dam_punct_loc_Manual_Latitude'])  , axis = 1)
df3['Duct_dam_punct_long']=df3.apply(lambda row: long(row['Duct_dam_punct_loc_point'],row['Duct_dam_punct_loc_Manual_Longitude'])  , axis = 1)
df3['Duct_miss_lat'] = df3.apply(lambda row: lat(row['Duct_miss_loc_pt'],row['Duct_miss_loc_Manual_Latitude'])  , axis = 1)
df3['Duct_miss_long']=df3.apply(lambda row: long(row['Duct_miss_loc_pt'],row['Duct_miss_loc_Manual_Longitude'])  , axis = 1)
df3 = df3.drop('Chamber1_Location_Point', axis=1)
df3 = df3.drop('_geolocation', axis=1)
df3 = df3.drop('Chamber1_Manual_Latitude', axis=1)
df3 = df3.drop('Chamber1_Manual_Longitude', axis=1)
df3 = df3.drop('Chamber2_location_Point', axis=1)
df3 = df3.drop('Chamber2_Manual_Latitude', axis=1)
df3 = df3.drop('Chamber2_Manual_Longitude', axis=1)
df3 = df3.drop('Duct_dam_punct_loc_point', axis=1)
df3 = df3.drop('Duct_dam_punct_loc_Manual_Latitude', axis=1)
df3 = df3.drop('Duct_dam_punct_loc_Manual_Longitude', axis=1)
df3 = df3.drop('Duct_miss_loc_pt', axis=1)
df3 = df3.drop('Duct_miss_loc_Manual_Latitude', axis=1)
df3 = df3.drop('Duct_miss_loc_Manual_Longitude', axis=1)
df3.columns = df3.columns.str.replace(" ", "") # What was the need
df3['prikey']=pd.to_numeric(df3['prikey'])

# # T&D Form
r4 = requests.get('https://nssbsurvey.sterliteapps.com/api/v1/data/s49_2107', auth=('parth.pandey@stl.tech', password))
data = r4.json()
df4=pd.DataFrame(data)

df4['from_loc_lat'] =df4.apply(lambda row: lat(row['From_Location'],row['From_Location_Latitude_Manual'])  , axis = 1)
df4['from_loc_long']=df4.apply(lambda row: long(row['From_Location'],row['From_Location_Longitude_Manual'])  , axis = 1)
df4['to_loc_lat'] =  df4.apply(lambda row: lat(row['To_Location'],row['To_Location_Latitude_Manual'])  , axis = 1)
df4['to_loc_long']=  df4.apply(lambda row: long(row['To_Location'],row['To_Location_Longitude_Manual'])  , axis = 1)
df4 = df4.drop('From_Location', axis= 1)
df4 = df4.drop('To_Location', axis= 1)
df4 = df4.drop('_geolocation',axis= 1)
df4 = df4.drop('From_Location_Latitude_Manual',axis= 1)
df4 = df4.drop('To_Location_Latitude_Manual',axis= 1)
df4 = df4.drop('To_Location_Longitude_Manual',axis= 1)
df4 = df4.drop('From_Location_Longitude_Manual',axis= 1)


df4.columns = df4.columns.str.replace(" ", "") # What was the need
df4['prikey']=pd.to_numeric(df3['prikey'])

shutil.rmtree('Output\PDF')
shutil.rmtree('Output\Excel')
os.mkdir('Output\PDF')
os.mkdir('Output\Excel')


# Making a connection to data.db
conn = sqlite3.connect("data.db")#
c = conn.cursor()
# Including HDD table in data.db
df.to_sql("hdd",conn, if_exists='replace')
df1.to_sql("dit",conn, if_exists='replace')
df2.to_sql("blowing",conn, if_exists='replace')
df3.to_sql("drt",conn, if_exists='replace')
df4.to_sql("tnd",conn, if_exists='replace')