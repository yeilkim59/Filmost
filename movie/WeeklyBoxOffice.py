import requests
import json
import datetime
import pandas as pd


key ="e3704d553370c702c763dcfaa21bf84b"
weekGb= 0
targetDt=[]
startDt = datetime.date(2018,1,1)
endDt =datetime.date(2018,1,20)

for i in range(0,100):
    Dt= startDt.strftime('%Y%m%d')
    targetDt.append(Dt)
    startDt = startDt+datetime.timedelta(weeks=1)

    if(startDt >= endDt):
        break

movie = []
for tDt in targetDt:
    url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key="+key+"&targetDt="+tDt+"&weekGb="+str(weekGb)

    res= requests.get(url)
    text=res.text

    d=json.loads(text)

    for b in d['boxOfficeResult']['weeklyBoxOfficeList']:
        week = d['boxOfficeResult']['yearWeekTime']
        date = d['boxOfficeResult']['showRange']
        print(b)
        movie.append([week,date,b['rank'],b['movieNm'],b['movieCd'],b['openDt'],b['audiCnt'],b['audiAcc']])
        print(week,date,b['rank'],b['movieNm'],b['movieCd'],b['openDt'],b['audiCnt'],b['audiAcc'])



data=pd.DataFrame(movie, columns=["yyyyWW","Date","Rank","Title","Code","OpenDate","Weekly","Total"])
data.to_csv("wbo.csv", mode="w", encoding='utf-8-sig', index=False)
