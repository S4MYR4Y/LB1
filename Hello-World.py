import requests
from datetime import datetime, timedelta

response = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20241017&end=20241023&valcode=pln&sort=exchangedate&order=desc&json")

data = response.json()

print (data)

resp_dict = response.json()
print (resp_dict)

dates =[]
rates =[]
for item in resp_dict:
    print(" exchangedate", item['exchangedate'], "rate",item['rate'])
    dates.append(item['exchangedate'])
    rates.append([item['rate']])


import matplotlib.pyplot as plt

plt.plot(dates, rates)

plt.show()




