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

ost = pd.read_csv("C://Users//lg//Desktop//데이터크롤링//ost/ostchart.csv")

title=ost.drop_duplicates('Title')
print(title)

ost_Title=ost["Title"].value_counts()[:30]

ax=sns.countplot(x="Title",data=ost,order=ost.Title.value_counts().iloc[:30].index)
for i in range(ost_Title.shape[0]):
    ax.text(x=i,y=ost_Title[i],s=ost_Title[i])
ax.set_xticklabels(ax.get_xticklabels(), rotation=20, ha="right")
ax.set(ylim=(0,105))
ax.set_xlabel('Title')
ax.set_ylabel('Week')
ax.set_title('OST인기 순위')
plt.show()
