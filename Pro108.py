import plotly.figure_factory as pf  
import pandas as pd 
import csv

f = pd.read_csv("Pro108Data.csv")
fig = pf.create_distplot([f["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()












