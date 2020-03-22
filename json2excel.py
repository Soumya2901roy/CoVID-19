
import requests
import json
import csv
import time

r=requests.get("https://api.covid19india.org/raw_data.json")
headers=['currentstatus','detectedstate','gender','dateannounced','nationality']
c=r.json()
print(type(c))
raw_data=c["raw_data"]
with open('data.csv','a') as csvfile:
    write=csv.writer(csvfile,delimiter=',')

    write.writerow(headers)
    for each_line in raw_data:
        temp=[]
        for h in headers:
            temp.append(each_line[h])
        #print(temp)
        write.writerow(temp)

#print(raw_data)
