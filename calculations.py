import pandas as pd
import numpy as np
import os
#import matplotlib as mpl

data = open(os.getcwd() + '\\' + 'bt-scraper\cleanedData.csv')
df = pd.read_csv(data)

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
#    7. Minimum number of days before a bourbon repeats
#    8. Maximum amount of days before a bourbon repeats 
#    9. Average number of days before a bourbon repeats


# Values in dataframe that satisfy this condition
print(df.where(df['Date']>'2021-12-31'))
