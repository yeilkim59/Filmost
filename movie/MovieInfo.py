import csv
import requests
import json
import pandas as pd

f = open('test.csv','r',encoding='utf-8')
rdr=csv.reader(f)

mCode=[]

for line in rdr:
    mCode.append(line[4])

f.close

del mCode[mCode.index("Code")]
cnt= len(mCode)


key="b9d574a51100f2ccbd22cd889f3ed1e7"

movie=[]

for code in mCode:
    url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key="+key+"&movieCd="+code
    
    res= requests.get(url)
    text=res.text
    d=json.loads(text)

    print(d['movieInfoResult']['movieInfo']['movieCd'],d['movieInfoResult']['movieInfo']['movieNm'],d['movieInfoResult']['movieInfo']['genres'])
    movie.append([d['movieInfoResult']['movieInfo']['movieCd'],d['movieInfoResult']['movieInfo']['movieNm'],d['movieInfoResult']['movieInfo']['genres']])
    

data = pd.DataFrame(movie)
data.to_csv("info.csv",mode='w',encoding='utf-8-sig',index=False)
