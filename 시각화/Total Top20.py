import numpy as np
import pandas as pd
import matplotlib.pyplot as lit
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

#누적관객수 top 20

mov = pd.read_csv("C://Users//lg//Desktop//데이터크롤링//movie/mov_data.csv")

df=mov.sort_values(by='Total',ascending=False)
data = df.drop_duplicates(['Title'],keep='first')   
data2 =data[0:20].sort_values(by='Total',ascending=True)


x=data2.Title
y=data2.Total

plt.barh(x,y)

plt.title('누적 관객수 TOP 20')
plt.xlabel('Total')
plt.ylabel('Title')
plt.box(False)
plt.axvline(x=10000000, color='r', linestyle='--', linewidth=1)

plt.show()
