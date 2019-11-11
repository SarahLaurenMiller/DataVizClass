import os, csv

from statistics import mean

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = []
total_profit = []
monthly_profit_change = []
 
with open(csvpath,newline="", encoding="utf-8") as budget:
    csvreader = csv.reader(budget,delimiter=",") 
    header = next(csvreader) #skip header

    for row in csvreader: 

        # Append the total months and total profit to their corresponding lists
        # Moves the data from the csv to the lists 
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Find max and min in the monthly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Find corresponding month using month list and index from max and min
# Use the plus 1 at the end since month associated with change is the next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements in GitBash

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Profit/Loss: ${round(mean(total_profit),2)}")
print(f"Average Profit/Loss Change Between Months: ${round(mean(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} ${(str(max_increase_value))}")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} ${(str(max_decrease_value))}")

with open ("pybank_output.txt", "w") as output:
    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total Months: {len(total_months)}\n")
    output.write(f"Total: ${sum(total_profit)}\n")
    output.write(f'Average Profit/Loss: ${round(mean(total_profit),2)}\n')
    output.write(f"Average Profit/Loss Change Between Months: ${round(mean(monthly_profit_change),2)}\n")
    output.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
    output.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")
