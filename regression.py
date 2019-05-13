import pandas as pd
import quandl

#get data from quandl.com
df=quandl.get("FINRA/FNRA_GOOGL", authtoken="QXLRYqyjrDN-DaW3ui8i", collapse="monthly", start_date="2016-04-03")


print(df.head())

#df=df[['ShortVolume','TotalVolume']]
