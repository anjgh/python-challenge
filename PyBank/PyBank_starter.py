#create file path across operating systems
import os
#module for reading CSV files
import csv

#set path for file
csvpath = os.path.join('Resources','budget_data.csv')

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

    #skip the header
    next(csvfile)

    #get the first row data
    first_row = next(csvreader)
    first_profit_value = int(first_row[1])
    net_total_profit_losses = net_total_profit_losses + first_profit_value
    total_months_count = total_months_count + 1
    
    for row in csvreader:
        total_months_count = total_months_count + 1
        current_profit_value = int(row[1])   

        #incrementally add the value of int(row[1]) to net_total_profit_losses
        net_total_profit_losses = net_total_profit_losses + current_profit_value
        
        #calculate the change and add it to average_change list
        change =  current_profit_value - first_profit_value
        average_change.append(change)
        total_change = total_change + change

        #check for greatest increase and greatest decrease  
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]
        elif change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]    

        #update first_profit_value to the current row's profit value
        first_profit_value = current_profit_value        

    #calculate the average_change
    average_change = total_change/len(average_change)

#prepare output
results = (
    "\nFinancial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months_count}\n"
    f"Total: ${net_total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

#print the results
print(results)

output_path = os.path.join('analysis','financial_analysis.txt')
with open(output_path, mode = 'w') as textfile:
    textfile.write(results)