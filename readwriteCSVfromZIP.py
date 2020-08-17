import pandas as pd
import zipfile

zf = zipfile.ZipFile('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/201907-citibike-tripdata.csv.zip')
df = pd.read_csv(zf.open('201907-citibike-tripdata.csv'))

#df.info()

#df.loc[df['birth year'] >= 1920]

bikeset = df.loc[df['birth year'] >= 1920]

bikeset1 = bikeset[0:727021]
bikeset2 = bikeset[727021:1454042]
bikeset3 = bikeset[1454042:]

#bikeset1.info()
#bikeset2.info()
#bikeset3.info()

bikeset1.to_csv('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/bikeset1.csv')
bikeset2.to_csv('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/bikeset2.csv')
bikeset3.to_csv('/Users/davidvance/Documents/Coursework/Homework/02_Bike_Data/bikeset3.csv')


