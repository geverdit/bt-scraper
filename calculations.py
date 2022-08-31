import pandas as pd
import numpy as np
import os
#import matplotlib as mpl

data = open(os.getcwd() + '\\' + 'bt-scraper\cleanedData.csv')
df = pd.read_csv(data)

blantonsIndex = df[df['Whiskey'] == 'Blantons'].index.values
ehtIndex = df[df['Whiskey'] == 'EH Taylor'].index.values
erIndex = df[df['Whiskey'] == 'Eagle Rare'].index.values
wellerIndex = df[df['Whiskey'] == 'Weller'].index.values
sazIndex = df[df['Whiskey'] == 'Sazerac'].index.values
sopIndex = df[df['Whiskey'] == 'Single Oak Project'].index.values
closeIndex = df[df['Whiskey'] == 'CLOSED'].index.values

# Questions I want to answer:
#    1. What’s the prediction for tomorrows bourbon?
#    2. Is there a pattern?
#    3. Which bourbons favor which week days?
#        * Count of bourbon per weekday
#    4. Which bourbons favor which month days?
#        * count of bourbon per month day
#    5. What bourbons favor which months?
#        * Count of bourbon per month
#    6. What bourbon is most likely to follow a certain bourbon?
#  DONE  7. Minimum number of days before a bourbon repeats
#  DONE  8. Maximum amount of days before a bourbon repeats 
#  DONE  9. Average number of days before a bourbon repeats

class BlantonsData():
    result=[]
    for i in range(len(blantonsIndex)):
        if i < len(blantonsIndex)-1:
            result.append(blantonsIndex[i+1] - blantonsIndex[i])
        elif i == len(blantonsIndex):
            result.append(blantonsIndex[i] - blantonsIndex[i-1])

    max = max(result)
    min = min(result)
    avg = round((sum(result) / len(result)), 2)

    count = pd.Series(result).value_counts()
    #print(count)
    print (f'Blantons:\nMax: {max} days \nMin: {min} day(s) \nAverage: {avg} days\n')
class EHTData():
    result=[]
    for i in range(len(ehtIndex)):
        if i < len(ehtIndex)-1:
            result.append(ehtIndex[i+1] - ehtIndex[i])
        elif i == len(ehtIndex):
            result.append(ehtIndex[i] - ehtIndex[i-1])

    max = max(result)
    min = min(result)
    avg = round((sum(result) / len(result)), 2)

    count = pd.Series(result).value_counts()
    #print(count)
    # print (f'EH Taylor:\nMax: {max} days \nMin: {min} day(s) \nAverage: {avg} days\n')
class ERData():
    result=[]
    for i in range(len(erIndex)):
        if i < len(erIndex)-1:
            result.append(erIndex[i+1] - erIndex[i])
        elif i == len(erIndex):
            result.append(erIndex[i] - erIndex[i-1])

    max = max(result)
    min = min(result)
    avg = round((sum(result) / len(result)), 2)

    count = pd.Series(result).value_counts()
    #print(count)
    #print (f'Eagle Rare:\nMax: {max} days \nMin: {min} day(s) \nAverage: {avg} days\n')
class WellerData():
    result=[]
    for i in range(len(wellerIndex)):
        if i < len(wellerIndex)-1:
            result.append(wellerIndex[i+1] - wellerIndex[i])
        elif i == len(wellerIndex):
            result.append(wellerIndex[i] - wellerIndex[i-1])

    max = max(result)
    min = min(result)
    avg = round((sum(result) / len(result)), 2)

    count = pd.Series(result).value_counts()
    #print(count)    
    #print (f'Weller:\nMax: {max} days \nMin: {min} day(s) \nAverage: {avg} days\n')
class SazData():
    result=[]
    for i in range(len(sazIndex)):
        if i < len(sazIndex)-1:
            result.append(sazIndex[i+1] - sazIndex[i])
        elif i == len(sazIndex):
            result.append(sazIndex[i] - sazIndex[i-1])

    max = max(result)
    min = min(result)
    avg = round((sum(result) / len(result)), 2)

    count = pd.Series(result).value_counts()
    #print(count)
    #print (f'Sazerac:\nMax: {max} days \nMin: {min} day(s) \nAverage: {avg} days\n')
class SOPData():
    result=[]
    for i in range(len(sopIndex)):
        if i < len(sopIndex)-1:
            result.append(sopIndex[i+1] - sopIndex[i])
        elif i == len(sopIndex):
            result.append(sopIndex[i] - sopIndex[i-1])

    max = max(result)
    min = min(result)
    avg = round((sum(result) / len(result)), 2)

    count = pd.Series(result).value_counts()
    #print(count)
    #print (f'Single Oak Project:\nMax: {max} days \nMin: {min} day(s) \nAverage: {avg} days\n')
