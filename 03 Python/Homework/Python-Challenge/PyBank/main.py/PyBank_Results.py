# import libraries
import os
import csv
import sys

# set a path
csvpath =  os.path.join('Resources', 'budget_data.csv')

# declare your variables
total_months = 0
total_revenue = 0
greatest_inc = -sys.maxsize - 1
greatest_inc_date = ""
greatest_dec = sys.maxsize
greatest_dec_date = ""

# read the file in
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    # count months, find the total revenue and find the greatest increase & decrease in revenue
    for row in csvreader:
        total_months += 1
        total_revenue += int(row[1])
        if int(row[1]) >= greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_date = row[0]
        if int(row[1]) <= greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_date = row[0]

# calculate the average revenue change
average_change = round(total_revenue/total_months, 2)

# print results to your terminal
print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(average_change))
print("Greatest Increase in Revenue: " + greatest_inc_date + " ($" + str(greatest_inc) + ")")
print("Greatest Decrease in Revenue: " + greatest_dec_date + " ($" + str(greatest_dec) + ")")

# create the new txt file
new_file = open("Output/analysis_1.txt", "w")

# write the txt file
new_file.write("Financial Analysis \n")
new_file.write("-------------------------------------------- \n")
new_file.write("Total Months: " + str(total_months) + "\n")
new_file.write("Total Revenue: $" + str(total_revenue) + "\n")
new_file.write("Average Revenue Change: $" + str(average_change) + "\n")
new_file.write("Greatest Increase in Revenue: " + greatest_inc_date + " ($" + str(greatest_inc) + ")" + "\n")
new_file.write("Greatest Decrease in Revenue: " + greatest_dec_date + " ($" + str(greatest_dec) + ")" + "\n")
