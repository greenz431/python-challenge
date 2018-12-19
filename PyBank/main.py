print("Financial Analysis")
print("----------------------------------------")

import os
import csv
import pandas as pd
import numpy as np
from dateutil.relativedelta import relativedelta
from datetime import datetime

date1 = pd.Series(pd.date_range('2001-1-1', periods=1,freq='M'))
date2 = pd.Series(pd.date_range('2017-2-1', periods=1,freq='W'))

df = pd.DataFrame(dict(Start_date = date1, End_date = date2))

df['diff_months'] = df['End_date'] - df['Start_date']
df['diff_months']= df['diff_months']/np.timedelta64(1,'M')


print(f"Total Months: {df.iloc[0]['diff_months']}")

csvpath = os.path.join("budget_data.csv")

with open(csvpath,newline='') as fin:
    csvreader = csv.reader(fin,delimiter=',')
    csv_header = next(csvreader)
    total = 0
    for row in csv.reader(fin):
        total += int(row[1])
    print(f"Total: {total}")

import pandas as pd
df = pd.read_csv('budget_data.csv')
mean1 = df['Change'].mean()
print(f"Average Change: {mean1}")

import pandas as pd
df = pd.read_csv('budget_data.csv')
max1 = df['Change'].max()
date_max = df.loc[df['Change']==1926159,'Date']


print(f"Greatest Increase in Profits: {date_max} {max1}")

import pandas as pd
df = pd.read_csv('budget_data.csv')
min1 = df['Change'].min()
date_min = df.loc[df['Change']==-2196167,'Date']

print(f"Greatest Decrease in Profits: {date_min} {min1}")

def out_fun():
    return "Financial Analysis
    ----------------------------------------
    Total Months: 192.16821700650937
    Total: 38382578
    Average Change: -2288.1976744186045
    Greatest Increase in Profits: Feb-12 1926159
    Greatest Decrease in Profits: Sep-13 -2196167"
output = out_fun()
file = open("homework.txt","w")
file.write(output)
file.close()





    
    





  
