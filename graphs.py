# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#print ("Hello World")
import pandas as pd
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

df = pd.read_csv(url, delimiter=',',header = 'infer')
df_interest = df.loc[
                df['Country/Region'].isin(['United Kingdom','US', 'Italy', 'Germany'])
                & df['Province/State'].isna()]

df_interest.rename(index=lambda x: df_interest.at[x,'Country/Region'], inplace=True)
df1 = df_interest.transpose()
df1 = df1.drop(['Province/State','Country/Region', 'Lat','Long'])
df1 = df1.loc[(df1 != 0).any(1)]
df1.index = pd.to_datetime(df1.index)

from matplotlib import pyplot
df1.plot()
pyplot.xlabel('Dates')
pyplot.ylabel('No of Deaths')
pyplot.show()




