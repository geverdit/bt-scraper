import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup as bs

url = 'https://buffalotracedaily.com/2022-gift-shop-releases/'
r = requests.get(url)
soup = bs(r.text, 'html.parser')

dailyTableHTML = soup.find('figure', class_= 'wp-block-table')
    
for entry in dailyTableHTML.find_all('tbody'):

    dateData = []
    dayOfWeekData = []
    primaryWhiskeyData = []
    col={}

    rows = entry.find_all('tr')
    for row in rows:
        dateData.append(row.find_all('td')[0].text)
        dayOfWeekData.append(row.find_all('td')[1].text)
        primaryWhiskeyData.append(row.find_all('td')[2].text)
        
    col = {"Date": dateData, "Day": dayOfWeekData, "Whiskey": primaryWhiskeyData}
    #print(col)

    df=pd.DataFrame(col)
    print(df)
    df.to_csv('/Users/iangeverdt/python projects/buffalo trace project/yearlyData/2022List.csv', index = False)