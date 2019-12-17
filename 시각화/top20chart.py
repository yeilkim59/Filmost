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

df=mov.sort_values(by='Total',ascending=False)
data = df.drop_duplicates(['Title'],keep='first')
ost = pd.read_csv("C://Users//lg//Desktop//데이터크롤링//ost/ostchart.csv")

title=data.Title[0:20]

res1 =pd.DataFrame()
res2 =pd.DataFrame()
res3 =pd.DataFrame()

for name in title:
    find1 =ost[ost['Album'].str.contains(name)]
    find2 =ost[ost['Album'].str.contains(name)].drop_duplicates('yyyyWW')
    
    res1=res1.append(find1)
    res2=res2.append(find2)
    
    print(name,len(find1))

result1 =pd.DataFrame(res1)
result1.to_csv("result1.csv",mode='w',encoding='utf-8-sig', index=False)


chartIn =res1.drop_duplicates('Album')
print("해당 영화")
print(chartIn.Album)

    
song =pd.DataFrame(res1.sort_values(by='Rank',ascending=True).drop_duplicates('Title'))
print("곡명",song.Rank,song.Title)
result2= pd.DataFrame(song)
result2.to_csv("result2.csv",mode='w',encoding='utf-8-sig',index=False)

res2_Album = res2['Album'].value_counts()
ax=sns.countplot(x="Album",data=res2,order=res2.Album.value_counts().index)
for i in range(res2_Album.shape[0]):
    ax.text(x=i,y=res2_Album[i],s=res2_Album[i])
ax.set_xticklabels(ax.get_xticklabels(), rotation=10, ha="right")
ax.set(ylim=(0,30))
ax.set_xlabel('Title')
ax.set_ylabel('Week')
ax.set_title('몇 주동안 차트에 있었을까?')
plt.show()

pop=song[0:15]
print(pop)

for name in pop.Title:
    find=res1[res1['Title']==name]
    res3=res3.append(find)
    
x=pop.Title
y=pop.Rank

ax=sns.countplot(x="Title",data=res3)
ax.set(ylim=(0,30))
ax.set_xticklabels(ax.get_xticklabels(), rotation=20, ha="right")

plt.twinx()
plt.scatter(x,y)
plt.ylim(20,0)
plt.xlabel('OST Title')
plt.ylabel('Rank')
plt.title('인기 OST별 차트인/최고 순위')
plt.show()
