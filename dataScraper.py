import requests
import pandas as pd
import os
from bs4 import BeautifulSoup as bs
from datetime import date

saveFolder = os.getcwd() + '\dailyPickFiles'
currentYear = date.today().year
savePath = saveFolder+'\\' + str(currentYear) + '.csv'

url = f'https://buffalotracedaily.com/{currentYear}-gift-shop-releases/'
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
    #print(df)
    df.to_csv(savePath, index = False)
    