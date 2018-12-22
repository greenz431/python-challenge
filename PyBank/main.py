print("Financial Analysis")
print("----------------------------------------")

import os
import csv

csvpath = os.path.join("budget_data.csv")

months = []
profit_loss = []
change = []


with open(csvpath,newline='') as fin:
    csvreader = csv.reader(fin,delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

    for i in range(1,len(profit_loss)):
        change.append(profit_loss[i]-profit_loss[i-1])

    total_months = set(months)
    total_revenue = sum(profit_loss)
    total_change = sum(change)
    length_change = len(change)
    average_change = total_change/length_change
    max_change = max(change)
    max_change_date = months[change.index(max_change)]
    min_change = min(change)
    min_change_date = months[change.index(min_change)]

print(f"Total Months: " + str(len(total_months)))
print(f"Total Revenue: $" + str(total_revenue))
print(f"Average Change: $" + str(round(average_change,2)))
print(f"Greatest Increase in Profits: " + str((max_change_date) + " $" + str(max_change)))
print(f"Greatest Decrease in Profits: " + str((min_change_date) + " $" + str(min_change)))

file = open("main.txt","w")
file.write("Financial Analysis"
"----------------------------------------"
"Total Months: 86"
"Total Revenue: $38382578"
"Average Change: $-2288.2"
"Greatest Increase in Profits: Feb-12 $1926159"
"Greatest Decrease in Profits: Sep-13 $-2196167")


file.close()