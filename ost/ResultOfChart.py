import csv
import pandas as pd


df=pd.read_csv("C://Users//lg//Desktop//데이터크롤링/2018chart.csv")

df2=df[df['5'].str.contains('영화|애니메이션')]

data=pd.DataFrame(df2)
data.to_csv("ostChart2018.csv",mode='w',encoding="utf-8-sig", index=False)



df3=pd.read_csv("C://Users//lg//Desktop//데이터크롤링/2019chart.csv")

df4=df[df['5'].str.contains('영화|애니메이션')]

data=pd.DataFrame(df4)
data.to_csv("ostChart2019.csv",mode='w',encoding="utf-8-sig", index=False)


result=pd.concat[df2,df4]

data=pd.DataFrame(result, columns=["yyyyWW","Rank","Title","Artist", "Album","Genre"])
data.to_csv("ostChart.csv", mode='w',encoding="utf-8-sig", index=False)

