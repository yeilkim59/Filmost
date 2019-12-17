import numpy as np
import pandas as pd
import matplotlib.pyplot as lit
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from matplotlib import font_manager, rc
from collections import Counter

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

mov = pd.read_csv("C://Users//lg//Desktop//데이터크롤링//movie/mov_data.csv")
ost = pd.read_csv("C://Users//lg//Desktop//데이터크롤링//ost/ostchart.csv")

data =mov.drop_duplicates('Title')
title=data.Title


print(title)

res=pd.DataFrame()
res2=pd.DataFrame()
t=pd.DataFrame()

for name in title:
    find=ost[ost['Album'].str.contains(name)]
    find2=ost[ost['Album'].str.contains(name)].drop_duplicates('yyyyWW')
    
    res=res.append(find)
    res2=res2.append(find2)
    print(name,len(find))

    if not len(find) is 0:
        find3=mov[mov['Title'].str.contains(name)]
        t=t.append(find3)

result=pd.DataFrame(res)
result.to_csv("all_result.csv",mode='w',encoding='utf-8-sig', index=False)
    
chartIn=res.drop_duplicates('Album')
print(chartIn.Album)

result2=pd.DataFrame(t)
result2.to_csv("all_chartIn.csv", mode='w',encoding='utf-8-sig', index=False)

t=t[t['Title']!='에그엔젤 코코밍: 두근두근 핼러윈 파티']
df=t.sort_values(by='Total', ascending=False)
df=df.drop_duplicates('Title',keep='first').sort_values(by='Total',ascending=True)
print("결과",df)

x=df.Title
y=df.Total

plt.barh(x,y)
plt.xlabel('Total')
plt.ylabel('Title')
plt.title('음원 차트에 있는 영화 누적 관객수')
plt.axvline(x=4684247, color='r', linestyle='--', linewidth=1)

    
plt.show()

res2_Album=res2["Album"].value_counts()

ax=sns.countplot(x="Album",data=res2,order=res2.Album.value_counts().index)
for i in range(res2_Album.shape[0]):
    ax.text(x=i,y=res2_Album[i],s=res2_Album[i])
ax.set_xticklabels(ax.get_xticklabels(), rotation=10, ha="right")
ax.set(ylim=(0,105))
ax.set_xlabel('Title')
ax.set_ylabel('Week')
ax.set_title('몇 주동안 차트에 있었을까?')
plt.show()
