#!/usr/bin/env python3
# Use this script to read large CSV files from a ZIP file and break into smaller CSV's to accommodate the large number of rows.

import pandas as pd
import zipfile

# in the future, add user input line to get path to ZIP file. Able to open the contents without knowing the filename or will that need to be input, as well?
zf = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/201907-citibike-tripdata.csv.zip')
df = pd.read_csv(zf.open('201907-citibike-tripdata.csv'))

#df.info()

# Filter out birth years earlier than 1920 to keep the age range within reason.
df.loc[df['birth year'] >= 1920]
#bikeset = df.loc[df['birth year'] >= 1920]  --> Use this if must assign the filtered data set to a new variable...

# Currently manually determining number of rows in zipped CSV, dividing by 2 or 3 as appropriate to get below ~1.4M-row limit, then typing in row slices.
# Need to automate this part of the process.
bikeset1 = df[0:727021]
bikeset2 = df[727021:1454042]
bikeset3 = df[1454042:]

#bikeset1.info()
#bikeset2.info()
#bikeset3.info()

# Have user specify destination for new CSV's or have it automatically save to same folder as original file but with new names?
bikeset1.to_csv('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/bikeset1.csv')
bikeset2.to_csv('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/bikeset2.csv')
bikeset3.to_csv('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/bikeset3.csv')


