#create file path across operating systems
import os
#module for reading CSV files
import csv

#set path for file
csvpath = os.path.join('Resources','budget_data.csv')

print("Financial Analysis\n")
print("----------------------------\n")

total_months_count = 0
net_total_profit_losses = 0
average_change = []
total_change = 0
greatest_increase = 0
greatest_increase_date = ''
greatest_decrease = 0
greatest_decrease_date = ''

#open the CSV
with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    first_profit_value = int(next(csvreader)[1])
    
    #Loop through looking for total number of months
    for row in csvreader:
        if row[0] != csv_header:
            total_months_count = total_months_count + 1
        if row[1] != csv_header:
            #incrementally add the value of int(row[1]) to net_total_profit_losses
            net_total_profit_losses = net_total_profit_losses + int(row[1]) 

        current_profit_value = int(row[1])   
        change =  current_profit_value - first_profit_value
        average_change.append(change)
        total_change = total_change + change
          
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]
        elif change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]    

        first_profit_value = current_profit_value        


    average_change = total_change/len(average_change)

print(f"Total Months: {total_months_count}\n")
print(f"Total: ${net_total_profit_losses}\n")
print(f"Average Change: ${average_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")