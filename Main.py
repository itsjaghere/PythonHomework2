# Objective 1: Import modules os and csv

import os
import csv

# Objective 2: Set the path for the CSV file in PyBankcsv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Objective 3: Create the lists to store data.

profit = []
monthly_changes = []
date = []

# Initialize the variables as required.

count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Open the CSV
#kept getting error in this line
# with open ( file, 'r', newline='', encoding='UTF-8') as sd:
with open(csvpath, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   #csv_header = next(csvreader)

   # Conducting the ask
   for row in csvreader:
     # Use count to count the number months in this dataset
     count = count + 1

     # Will need it when collecting the greatest increase and decrease in profits
     date.append(row[0])

     # Append the profit information & calculate the total profit
     profit.append(row[1])
     total_profit = total_profit + int(row[1])

     #Calculate the average change in profits from month to month. Then calulate the average change in profits
     final_profit = int(row[1])
     monthly_change_profits = final_profit - initial_profit

     #Store these monthly changes in a list
     monthly_changes.append(monthly_change_profits)

     total_change_profits = total_change_profits + monthly_change_profits
     initial_profit = final_profit

     #Calculate the average change in profits
     average_change_profits = (total_change_profits/count)

     #Find the max and min change in profits and the corresponding dates these changes were obeserved
     greatest_increase_profits = max(monthly_changes)
     greatest_decrease_profits = min(monthly_changes)

     increase_date = date[monthly_changes.index(greatest_increase_profits)]
     decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

   