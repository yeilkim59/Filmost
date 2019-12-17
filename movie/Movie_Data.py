import pandas as pd



df1=pd.read_csv('C://Users//lg//AppData//Local//Programs//Python//Python37/wbo.csv')
df2=pd.read_csv('C://Users//lg//AppData//Local//Programs//Python//Python37/info.csv')

df3 =pd.concat([df1,df2],axis=1)

del df3['0']
del df3['1']

df3.rename(columns={'2':'Genre'}, inplace=True)

data =pd.DataFrame(df3)
data.to_csv("mov_data.csv", encoding='utf-8-sig',index=False)
