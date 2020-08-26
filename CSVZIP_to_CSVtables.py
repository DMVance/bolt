#!/usr/bin/env python3
# Use this script to read large CSV files from a ZIP file into a pandas dataframe, organize into two tables and write both to txt files.

import pandas as pd
import zipfile

# in the future, add user input line to get path to ZIP file. Able to open the contents without knowing the filename or will that need to be input, as well?
#zf1 = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/201908-citibike-tripdata.csv.zip')
#zf2 = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/201909-citibike-tripdata.csv.zip')
#zf3 = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/201910-citibike-tripdata.csv.zip')
#zf4 = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/201911-citibike-tripdata.csv.zip')
#zf5 = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/201912-citibike-tripdata.csv.zip')
zf6 = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/202001-citibike-tripdata.csv.zip')
zf7 = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/202002-citibike-tripdata.csv.zip')
zf8 = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/202003-citibike-tripdata.csv.zip')
zf9 = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/202004-citibike-tripdata.csv.zip')
zf10 = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/202005-citibike-tripdata.csv.zip')
zf11 = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/202006-citibike-tripdata.csv.zip')
zf12 = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/202007-citibike-tripdata.csv.zip')

#df1  = pd.read_csv(zf1.open('201908-citibike-tripdata.csv'))
#df2  = pd.read_csv(zf2.open('201909-citibike-tripdata.csv'))
#df3  = pd.read_csv(zf3.open('201910-citibike-tripdata.csv'))
#df4  = pd.read_csv(zf4.open('201911-citibike-tripdata.csv'))
#df5  = pd.read_csv(zf5.open('201912-citibike-tripdata.csv'))
df6  = pd.read_csv(zf6.open('202001-citibike-tripdata.csv'))
df7  = pd.read_csv(zf7.open('202002-citibike-tripdata.csv'))
df8  = pd.read_csv(zf8.open('202003-citibike-tripdata.csv'))
df9  = pd.read_csv(zf9.open('202004-citibike-tripdata.csv'))
df10 = pd.read_csv(zf10.open('202005-citibike-tripdata.csv'))
df11 = pd.read_csv(zf11.open('202006-citibike-tripdata.csv'))
df12 = pd.read_csv(zf12.open('202007-citibike-tripdata.csv'))

df = pd.concat([df6, df7, df8, df9, df10, df11, df12])
df = df.loc[df['birth year'] >= 1920] # Filter out birth years earlier than 1920 to keep the age range within reason.
#df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12])
df6 = df6.loc[df6['birth year'] >= 1920]
df7 = df7.loc[df7['birth year'] >= 1920]
df8 = df8.loc[df8['birth year'] >= 1920]
df9 = df9.loc[df9['birth year'] >= 1920]
df10 = df10.loc[df10['birth year'] >= 1920]
df11 = df11.loc[df11['birth year'] >= 1920]
df12 = df12.loc[df12['birth year'] >= 1920]

df_bikes6 = df6[['tripduration', 'starttime', 'stoptime', 'start station id', 'end station id', 'bikeid', 'usertype', 'birth year', 'gender']]
df_bikes7 = df7[['tripduration', 'starttime', 'stoptime', 'start station id', 'end station id', 'bikeid', 'usertype', 'birth year', 'gender']]
df_bikes8 = df8[['tripduration', 'starttime', 'stoptime', 'start station id', 'end station id', 'bikeid', 'usertype', 'birth year', 'gender']]
df_bikes9 = df9[['tripduration', 'starttime', 'stoptime', 'start station id', 'end station id', 'bikeid', 'usertype', 'birth year', 'gender']]
df_bikes10 = df10[['tripduration', 'starttime', 'stoptime', 'start station id', 'end station id', 'bikeid', 'usertype', 'birth year', 'gender']]
df_bikes11 = df11[['tripduration', 'starttime', 'stoptime', 'start station id', 'end station id', 'bikeid', 'usertype', 'birth year', 'gender']]
df_bikes12 = df12[['tripduration', 'starttime', 'stoptime', 'start station id', 'end station id', 'bikeid', 'usertype', 'birth year', 'gender']]

df_bikes6[['StartDate','StartTime']] = df_bikes6.starttime.str.split(expand=True)
df_bikes6[['StopDate','StopTime']] = df_bikes6.stoptime.str.split(expand=True)
df_bikes7[['StartDate','StartTime']] = df_bikes7.starttime.str.split(expand=True)
df_bikes7[['StopDate','StopTime']] = df_bikes7.stoptime.str.split(expand=True)
df_bikes8[['StartDate','StartTime']] = df_bikes8.starttime.str.split(expand=True)
df_bikes8[['StopDate','StopTime']] = df_bikes8.stoptime.str.split(expand=True)
df_bikes9[['StartDate','StartTime']] = df_bikes9.starttime.str.split(expand=True)
df_bikes9[['StopDate','StopTime']] = df_bikes9.stoptime.str.split(expand=True)
df_bikes10[['StartDate','StartTime']] = df_bikes10.starttime.str.split(expand=True)
df_bikes10[['StopDate','StopTime']] = df_bikes10.stoptime.str.split(expand=True)
df_bikes11[['StartDate','StartTime']] = df_bikes11.starttime.str.split(expand=True)
df_bikes11[['StopDate','StopTime']] = df_bikes11.stoptime.str.split(expand=True)
df_bikes12[['StartDate','StartTime']] = df_bikes12.starttime.str.split(expand=True)
df_bikes12[['StopDate','StopTime']] = df_bikes12.stoptime.str.split(expand=True)

df_bikes6 = df_bikes6.drop(columns=['starttime', 'stoptime'])
df_bikes7 = df_bikes7.drop(columns=['starttime', 'stoptime'])
df_bikes8 = df_bikes8.drop(columns=['starttime', 'stoptime'])
df_bikes9 = df_bikes9.drop(columns=['starttime', 'stoptime'])
df_bikes10 = df_bikes10.drop(columns=['starttime', 'stoptime'])
df_bikes11 = df_bikes11.drop(columns=['starttime', 'stoptime'])
df_bikes12 = df_bikes12.drop(columns=['starttime', 'stoptime'])

df_start_stations6 = df6[['start station id', 'start station name', 'start station latitude', 'start station longitude']]
df_start_stations7 = df7[['start station id', 'start station name', 'start station latitude', 'start station longitude']]
df_start_stations8 = df8[['start station id', 'start station name', 'start station latitude', 'start station longitude']]
df_start_stations9 = df9[['start station id', 'start station name', 'start station latitude', 'start station longitude']]
df_start_stations10 = df10[['start station id', 'start station name', 'start station latitude', 'start station longitude']]
df_start_stations11 = df11[['start station id', 'start station name', 'start station latitude', 'start station longitude']]
df_start_stations12 = df12[['start station id', 'start station name', 'start station latitude', 'start station longitude']]

df_end_stations6 = df6[['end station id', 'end station name', 'end station latitude', 'end station longitude']]
df_end_stations7 = df7[['end station id', 'end station name', 'end station latitude', 'end station longitude']]
df_end_stations8 = df8[['end station id', 'end station name', 'end station latitude', 'end station longitude']]
df_end_stations9 = df9[['end station id', 'end station name', 'end station latitude', 'end station longitude']]
df_end_stations10 = df10[['end station id', 'end station name', 'end station latitude', 'end station longitude']]
df_end_stations11 = df11[['end station id', 'end station name', 'end station latitude', 'end station longitude']]
df_end_stations12 = df12[['end station id', 'end station name', 'end station latitude', 'end station longitude']]

df_start_stations6 = df_start_stations6.drop_duplicates(subset=['start station id'])
df_start_stations7 = df_start_stations7.drop_duplicates(subset=['start station id'])
df_start_stations8 = df_start_stations8.drop_duplicates(subset=['start station id'])
df_start_stations9 = df_start_stations9.drop_duplicates(subset=['start station id'])
df_start_stations10 = df_start_stations10.drop_duplicates(subset=['start station id'])
df_start_stations11 = df_start_stations11.drop_duplicates(subset=['start station id'])
df_start_stations12 = df_start_stations12.drop_duplicates(subset=['start station id'])

df_end_stations6 = df_end_stations6.drop_duplicates(subset=['end station id'])
df_end_stations7 = df_end_stations7.drop_duplicates(subset=['end station id'])
df_end_stations8 = df_end_stations8.drop_duplicates(subset=['end station id'])
df_end_stations9 = df_end_stations9.drop_duplicates(subset=['end station id'])
df_end_stations10 = df_end_stations10.drop_duplicates(subset=['end station id'])
df_end_stations11 = df_end_stations11.drop_duplicates(subset=['end station id'])
df_end_stations12 = df_end_stations12.drop_duplicates(subset=['end station id'])

df_start_stations = pd.concat([df_start_stations6, df_start_stations7, df_start_stations8, df_start_stations9, df_start_stations10, df_start_stations11, df_start_stations12])
df_end_stations = pd.concat([df_end_stations6, df_end_stations7, df_end_stations8, df_end_stations9, df_end_stations10, df_end_stations11, df_end_stations12])
df_start_stations = df_start_stations.drop_duplicates(subset=['start station id'])
df_end_stations = df_end_stations.drop_duplicates(subset=['end station id'])
#df_stations = pd.concat([df_start_stations, df_end_stations])
#df_stations = df[['start station id', 'start station name', 'start station latitude', 'start station longitude', 'end station id', 'end station name', 'end station latitude', 'end station longitude']]

#df_start_stations.to_csv('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/df_start_stations.csv')
#df_end_stations.to_csv('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/df_end_stations.csv')
chunk_size = 500000
batch_no = 1
for chunk in pd.read_csv(“file.csv”, chunksize=chunk_size):
    chunk.to_csv(“file” + str(batch_no) + “.csv”, index=False)
    batch_no += 1

df_bikes6 
df_bikes7 
df_bikes8 
df_bikes9 
df_bikes10
df_bikes11
df_bikes12

# Have user specify destination for new CSV's or have it automatically save to same folder as original file but with new names?
#df_bikes.to_json('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/df_bikes.json', orient='records')
#df_stations.to_json('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/df_stations.json', orient='records')
#df_bikes6.to_csv('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/df_bikes6.csv', orient='records')
