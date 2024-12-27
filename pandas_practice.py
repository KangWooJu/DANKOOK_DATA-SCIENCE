import pandas as pd

age = pd.Series([25,30,35,40,45])
age
type(age)

data = ['spring','summer','fall','winter']
season = pd.Series(data)
season

season.iloc[2]