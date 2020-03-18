import requests
from bs4 import BeautifulSoup
import re
#import pandas as pd
import datetime
url = 'https://ncov2019.live/data'
now = datetime.datetime.now().strftime(("%Y-%m-%d:%H:00:00"))


req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

tables = soup.find_all('tr')

covid_data_d = {}

for table in tables:

    table_bodies = table.find_all('td')
    region_data_l = []
    for table_body in table_bodies:
        region_data_l.append(table_body.get_text())

    if len(region_data_l) == 0:
        continue
    region_data_l = [i.lstrip().rstrip() for i in region_data_l]
    region_data_l = [i.replace(',','') for i in region_data_l]
    covid_data_d[region_data_l[0]] = region_data_l[1:]



#print(covid_data_d)
#print(covid_data_d["India"])

for country in covid_data_d:
    print(country)
    print(covid_data_d[country])
