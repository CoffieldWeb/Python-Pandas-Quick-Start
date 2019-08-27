import pandas as pd
import xlrd

#Open stocks.xlsx and create a DataFrame with the results
df = pd.read_excel("stocks.xlsx")

#Notice the type for df is a DataFrame (pandas.core.frame.DataFrame)
print(type(df))

#Show the first 5 rows
print(df.head())
#	Date	Open	High	Low	Close	Volume	Adj Close
#0	2014-07-21	83.46	83.53	81.81	81.93	2359300	81.93
#1	2014-07-18	83.30	83.40	82.52	83.35	4020800	83.35
#2	2014-07-17	84.35	84.63	83.33	83.63	1974000	83.63
#3	2014-07-16	83.77	84.91	83.66	84.91	1755600	84.91
#4	2014-07-15	84.30	84.38	83.20	83.58	1874700	83.58

#Let's get the Date column. 
my_series = df["Date"]

#Notice the type for my_series is a Series (pandas.core.series.Series)
print(type(my_series))

#Create a new DataFrame with just the Date and Open columns.
limited_columns = df[['Date','Open']]
print(limited_columns.head())
#	Date	Open
#0	2014-07-21	83.46
#1	2014-07-18	83.30
#2	2014-07-17	84.35
#3	2014-07-16	83.77
#4	2014-07-15	84.30

#lets get the days when Open was below 83.5
below_83_Open = df[df.Open < 83.5]
print(below_83_Open.head())
#	Date	Open	High	Low	Close	Volume	Adj Close
#0	2014-07-21	83.46	83.53	81.81	81.93	2359300	81.93
#1	2014-07-18	83.30	83.40	82.52	83.35	4020800	83.35
#41	2014-05-23	83.20	83.23	82.49	83.08	1596900	83.08
#42	2014-05-22	83.05	83.26	82.61	83.00	1382100	83.00
#43	2014-05-21	82.15	83.09	81.60	82.97	1762600	82.97

#lets get the days when Open was below 83.5 and the Close was above 85
filtered_rows = df[(df.Open < 83.5) & (df.Close > 85)]
print(filtered_rows.head())
#	Date	Open	High	Low	Close	Volume	Adj Close
#1669	2008-01-22	80.25	87.53	79.14	85.5	21774200	33.32