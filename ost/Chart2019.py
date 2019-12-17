from selenium import webdriver
import time
from time import sleep
import re
from bs4 import BeautifulSoup
from time import sleep
import requests
import json
import re
import pandas as pd

header = {'User-Agent': ''}

wd = webdriver.Chrome("C://Users//lg//AppData//Local//Programs//Python//Python37//WebDriver/chromedriver.exe")
wd.get('https://www.melon.com/chart/index.htm')
wd.get("http://www.melon.com/chart/search/index.htm")

wd.implicitly_wait(3)

wd.find_element_by_xpath('//*[@id="d_chart_search"]/div/h4[1]/a').click()
wd.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[1]/span/label').click()

wd.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[1]/span/label').click()

result=[]
cnt=0

for i in range(1,12):
    wd.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[3]/div[1]/ul/li[' + str(i) + ']/span/label').click()
    

    wd.implicitly_wait(10)
    if(i==1 or i==5 or i==8 or i==10):
        for i in range(1,6):
            wd.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[4]/div[1]/ul/li[' + str(i) + ']/span/label').click()
            wd.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[18]/span/label').click()
            wd.find_element_by_xpath('//*[@id="d_srch_form"]/div[2]/button/span/span').click()
            cnt+=1

    else:
        for i in range(1,5):
            wd.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[4]/div[1]/ul/li[' + str(i) + ']/span/label').click()
            wd.find_element_by_xpath('//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[18]/span/label').click()
            wd.find_element_by_xpath('//*[@id="d_srch_form"]/div[2]/button/span/span').click()
        
            cnt+=1

            sleep(5)

            
            song_ids = wd.find_elements_by_xpath('//*[@id="lst50"]/td[4]/div/a')
            song_ids = [re.sub('[^0-9]', '', song_id.get_attribute("href")) for song_id in song_ids]
            ranks = wd.find_elements_by_xpath('//*[@id="lst50"]/td[2]/div/span[1]')

            for rank, song_id in zip(ranks, song_ids):
                sleep(5)

                req = requests.get('http://www.melon.com/song/detail.htm?songId=' + song_id, headers = header)
                html = req.text
                soup = BeautifulSoup(html, "html.parser")

                title = soup.find(attrs={"class": "song_name"}).text.replace('곡명', '').replace('\t','').replace('\n','').replace('\r','')
                artist = soup.find(attrs={"class": "artist_name"}).text
                album = soup.select('#downloadfrm > div > div > div.entry > div.meta > dl > dd')[0].text
                genre = soup.select('#downloadfrm > div > div > div.entry > div.meta > dl > dd')[2].text
                
                result.append(['2019'+str(cnt),rank.text,title,artist,album,genre])
                print(['2019'+str(cnt),rank.text,title,artist,album,genre])
                
            sleep(5)
            wd.find_element_by_xpath('//*[@id="frm"]/div[2]/span/a').click()

            song_ids = wd.find_elements_by_xpath('//*[@id="lst100"]/td[4]/div/a')
            song_ids = [re.sub('[^0-9]', '', song_id.get_attribute("href")) for song_id in song_ids]
            ranks = wd.find_elements_by_xpath('//*[@id="lst100"]/td[2]/div/span[1]')

            for rank, song_id in zip(ranks, song_ids):
                sleep(5)

                req = requests.get('http://www.melon.com/song/detail.htm?songId=' + song_id, headers = header)
                html = req.text
                soup = BeautifulSoup(html, "html.parser")

                title = soup.find(attrs={"class": "song_name"}).text.replace('곡명', '').replace('\t','').replace('\n','').replace('\r','')
                artist = soup.find(attrs={"class": "artist_name"}).text
                album = soup.select('#downloadfrm > div > div > div.entry > div.meta > dl > dd')[0].text
                genre = soup.select('#downloadfrm > div > div > div.entry > div.meta > dl > dd')[2].text
                
                result.append(['2019'+str(cnt),rank.text,title,artist,album,genre])
                print(['2019'+str(cnt),rank.text,title,artist,album,genre])
                                     
data = pd.DataFrame(result)
data.to_csv("chart2019.csv",mode='w',encoding='utf-8-sig',index=False)
