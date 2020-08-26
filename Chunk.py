#!/usr/bin/env python3
# Use this script to read large CSV files from a ZIP file into a pandas dataframe, organize into two tables and write both to txt files.

import pandas as pd
import zipfile

zf = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/ZIP_files/202007-citibike-tripdata.csv.zip')

chunk_size = 900000
batch_no = 1
for chunk in pd.read_csv(zf.open('202007-citibike-tripdata.csv'), chunksize=chunk_size):
    chunk.to_csv('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/df_bikes6_' + str(batch_no) + '.csv', index=False)
    batch_no += 1
    
