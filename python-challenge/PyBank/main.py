import os
import csv
from statistics import mean 

csvpath = os.path.join('Resources', 'budget_data.csv')

found = False
total_months = 0
total_revenue = 0
avg_rev_change = 0
rev = []
greatest_inc = 0
greatest_dec = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #print(csvreader)
    for row in csvreader:
        
        #The total number of months included in the dataset
        row_count = sum(1 for row in csvreader)
        print(row_count)

#The net total amount of "Profit/Losses" over the entire period
        #csv_header = next(csvreader)
        #rev_total = sum(float(row[1]) for row in csvreader)
        #print(rev_total)

    def rev(simpleList):
        print(f"The values within the list are...")
        for value in simpleList:
            print(value)
        print("The length of this list is... " + str(len(simpleList)))

    print(rev)
# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

#text
# Financial Analysis
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
