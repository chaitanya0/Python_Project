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

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
objects = df1.max().index
y_pos = np.arange(len(objects))
performance = df1.tail(1).values.tolist()[0]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Deaths')
plt.xlabel('Countries')
plt.title('Deaths per Country')
plt.show()

from matplotlib import pyplot
import numpy as np
#Credit: https://stackoverflow.com/questions/41088236/how-to-have-actual-values-in-matplotlib-pie-chart-displayed-python
def absolute_value(val):
    a  = np.round(val/100.*df1.max().sum(), 0)
    return int(a)
plot = df1.max().plot.pie(y=df1.max().index, figsize=(5, 5),autopct=absolute_value, label='')
plot.set_title('Total Number of Deaths', fontsize=12)
pyplot.show()

# #Credit https://matplotlib.org/3.1.1/gallery/images_contours_and_fields/image_annotated_heatmap.html
# import numpy as np
# from matplotlib import pyplot
# df1 = df1.tail(15)
# dates = df1.index.strftime('%Y-%b-%d')
# countries = df1.max().index
# df2 = pd.DataFrame(df1, columns=df1.columns).astype(int)
# matrix = np.array(df2).transpose()
# fig, ax = pyplot.subplots()
# im = ax.imshow(matrix)
# # We want to show all ticks...
# ax.set_xticks(np.arange(len(dates)))
# ax.set_yticks(np.arange(len(countries)))
# # ... and label them with the respective list entries
# ax.set_xticklabels(dates)
# ax.set_yticklabels(countries)
# # Rotate the tick labels and set their alignment.
# pyplot.setp(ax.get_xticklabels(), rotation=45, ha="right",
#          rotation_mode="anchor")
# # Loop over data dimensions and create text annotations.
# for i in range(len(dates)):
#     for j in range(len(countries)):
#         text = ax.text(i, j, matrix[j, i],
#                        ha="center", va="center", color="w", size = '10')
# ax.set_title("Deaths Per Day Heatmap")
# fig.tight_layout()
# pyplot.show()


# Bokeh Libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show

# The figure will be rendered in a static HTML file called output_file_test.html
output_file('output_file_test.html', 
            title='Empty Bokeh Figure')

# Set up a generic figure() object
fig = figure()

# See what it looks like
show(fig)
