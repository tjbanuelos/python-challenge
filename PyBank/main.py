# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total = 0
num = 0
# Add more variables to track other necessary financial data
months = []
net_change = []
profits = []
number = []
combined = []

#------------------------------------------------------------------------
# # Making an average function # #

# Define the function
def average(number = [0]):
    
    # Initialize my variables
    total = 0
    count = 0

    # Sum up the numbers in my list
    for num in number:
        total += num
        count += 1

    # # Need to make sure not to divide by zero
    if count == 0:
        return 0
    
    # # Compute the average
    else: 
        return total / count   
#---------------------------------------------------------------------------------   

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:

        # Track the total months
        total_months += 1

        # Track the total profit
        total += int(row[1])

        # Seperate the months and profits as their own list
        months.append(row[0])
        profits.append(row[1])

# # Tracking the net change and max/min
# Convert profits into integers
profits=[int(value) for value in profits] 

# Make a new list of the changes in profits
net_change = [profits[i] - profits[i-1] for i in range(1, len(profits))]

# Add 0 to the beginning of the net change list (Ensures this and months list are the same size)
net_change.insert(0,0)

# Convert net_change into integers
net_change=[int(value) for value in net_change]

# Calculate the greatest increase in profits (amount)
max = max(net_change)

# Calculate the greatest decrease in losses (amount)
min = min(net_change)

#------------------------------------------------------------------------------
# Combine the lists for month and net change into a new list
combined = zip(months, net_change)
#------------------------------------------------------------------------------

# Find the date of the max value
for row in combined:
    if row[1] == max:
        max_month = row[0]
    if row[1] == min:
        min_month = row[0]

# Calculate the average net change across the months
average_change = round(average(net_change), 2)


# Generate the output summary
print("Financial Analysis")
print("---------------------------------")

# Print the output
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(total))
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_month} (${max})')
print(f'Greatest Decrease in Profits: {min_month} (${min})')


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f'Total Months: {total_months} Total: ${total} Average Change: ${average_change} Greatest Increase: {max_month} (${max}) Greatest Decrease: {min_month} (${min})')

