# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 19:39:01 2021

@author: chaiy
"""
import camelot
tables2=camelot.read_pdf('gst-revenue-collection-march2020.pdf', flavor='stream', pages='0-3')
tables2
tables2[2]  # 2 is the index 
tables2[2].parsing_report
df2=tables2[2].df
df2  
tables2[3]
tables2[3].parsing_report
df3=tables2[3].df
df3
df4=df2.append(df3)
df4
df5=df4[1:]
df5.head()
new_header = df5.iloc[0]
df5 = df5[1:]
df5.columns = new_header