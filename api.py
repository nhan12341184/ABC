import os
import json
import time
import datetime
import requests
from bs4 import BeautifulSoup
from operator import itemgetter
from datetime import date

port = int(os.environ.get('PORT', 80))

url = "https://www.worldometers.info/coronavirus/"

def Run():
    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.findAll('tbody')

    covid_19_data_main = []

    #Total

    for row in table[1].find_all('tr'):
        cols = row.find_all('td')
        covid_19_global = {
            "country" : "global",
            "cases" : int(cols[1].text.replace(' ','').replace(',','')),
            "deaths" : cols[3].text.replace(' ','').replace(',',''),
            "recovered" : cols[5].text.replace(' ','').replace(',','')
        }
        covid_19_data_main.append(covid_19_global)

    #Countries

    for row in table[0].find_all('tr'):
        cols = row.find_all('td')
        data = {
            "country" : cols[0].text,
            "cases" : int(cols[1].text.replace(' ','').replace(',','')),
            "deaths" : cols[3].text.replace(' ','').replace(',',''),
            "recovered" : cols[5].text.replace(' ','').replace(',','')
        }
        covid_19_data_main.append(data)

    covid_19_data_sorted = sorted(covid_19_data_main, key=itemgetter('cases'), reverse=True)

    for data in covid_19_data_sorted:
        for value in data:
            data[value] = str(data[value])

    #data_done = json.dumps(covid_19_data_sorted)

    #Write Json File
    f = open("data.json", "w")
    f.write(12)
    f.close()

num = 0
while True:
    num += 1
    tmp_time = datetime.datetime.now()
    print("Updated:",num,"-",tmp_time.strftime("%H:%M:%S %Y-%m-%d"))
    Run()
    print("-----------------------------------------------------------")
    time.sleep(5)
