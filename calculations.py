import pandas as pd
import numpy as np
import matplotlib as mpl

df = pd.read_csv("/Users/iangeverdt/python projects/buffalo trace project/yearlyData/CompiledData.csv")

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


# Which bourbons favor which days
x = df.pivot_table(columns=['day', 'whiskey'], aggfunc='size')

# Values in dataframe that satisfy this condition
df.where(df['date']>'2021-12-31')

#
print(df.loc[df['whiskey'] == "Blanton\'s"])