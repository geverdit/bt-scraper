import pandas as pd
import glob
import os

saveFolder = os.getcwd() + '\dailyPickFiles'

# setting the path for joining multiple files
files = os.path.join(saveFolder, "*.csv")

# list of merged files returned
files = glob.glob(files)

# joining files with concat and read_csv
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df.to_csv(os.getcwd() + '\mergedCSV.csv', index = False)

#Renaming different variations of the same name to a standard
text = open(os.getcwd() + '\mergedCSV.csv', 'r', encoding='ascii', errors='replace')
text = ''.join([i for i in text]) \
    .replace('E.H Taylor, Jr. Small Batch', 'EH Taylor')\
    .replace('E.H. Taylor Jr. Small Batch', 'EH Taylor')\
    .replace('"E.H. Taylor, Jr. Small Batch"', 'EH Taylor')\
    .replace(u'\ufffd', '')\
    .replace('W.L. Weller Special Reserve', 'Weller')\
    .replace('Weller Special Reserve', 'Weller')\
    .replace('Sazerac Rye', 'Sazerac')\
    .replace('None', 'CLOSED')\
    .replace('Closed', 'CLOSED')

x = open(os.getcwd() + '\cleanedData.csv','w')
x.writelines(text)
x.close()
