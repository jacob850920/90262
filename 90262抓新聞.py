# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:10:20 2020

@author: Tony Kuo
"""

import csv
from bs4 import BeautifulSoup
# import requests
# import pandas as pf
from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import calendar
import time,datetime

now_date = time.strftime("%Y%m%d")
day=int(now_date[-2:])


n_days1=5#前五天
for i in range(0,n_days1):
    

    now = datetime.datetime.now()
    delta = datetime.timedelta(days=i)
    n_days = now-delta
    now1=now.strftime('%Y%m%d')
    
    n_days1=n_days.strftime('%Y%m%d')
    month01=str(n_days1[-4:-2])#月
    month02=int(month01)
    day01=str(n_days1[-2:])#號
    day02=int(day01)

options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
driver =webdriver.Chrome(chrome_options=options)



page=0
with open('90262抓新聞.csv','w+',newline='', encoding="utf-8-sig") as csvfile:   #解決多一空行 newline=''
    writer = csv.writer(csvfile)
    writer.writerow(('時間','類別','標題',['網站']))
    for i in range(5):

        r=driver.get("https://www.ettoday.net/news/news-list-2020-"+str(month02)+"-"+str(day02)+"-0.htm")
        
        page+=1
        html = driver.page_source
        sp=BeautifulSoup(html,"html.parser")
        search_time=sp.select("div.part_list_2 > h3 > span")
        search_a=sp.select("div.part_list_2 > h3 > em")
        search_b=sp.select("div.part_list_2 > h3 > a")
        # search_c=sp.select("div.part_list_2 > h3 > a")
        
        for i in range(len(search_time)):
            
            print(search_time[i].text,end=' ')#時間
            print(search_a[i].text,end=' ')#標題
            print(search_b[i].text,end=' ')#內容
            print(search_b[i].get('href'))#連結
            writer.writerow([search_time[i].text,search_a[i].text,search_b[i].text,search_b[i].get('href')])
        day02=day02+1




 
    


driver.close()#關閉網頁
