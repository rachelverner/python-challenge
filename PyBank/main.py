import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        
        #Store data
        totalMonths = []
        totalProfit = []
        revenueChange = []

    #Months/Profits/Losses    
        for row in csvreader:
            totalMonths.append(row[0])
            totalProfit.append(row[1])
        

    #Changes over the entire period
        for change in range(1, len(totalProfit)):
            revenueChange.append(int(totalProfit[change]) - int(totalProfit[change-1])) 

    #Average
        revenueAverage = sum(revenueChange) / len(revenueChange)

    #Max and min
    maxChange = max(revenueChange)
    minChange = min(revenueChange)

    #Random steps to try to fix things that went wrong
    totalofMonths=len(totalMonths)
    total_profit=sum(int(i) for i in totalProfit)

    #Print results
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:" + str(totalofMonths))
    print("Total Profit:" + str(total_profit))
    print("Average Change:" + str(revenueAverage))
    print("Greatest increase in profits:" + str(maxChange))
    print("Greatest decrease in profits:" + str(minChange))

# Specify the file to write to
output_path = os.path.join("..", "Resources", "pybank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])

    # Write the second,etc. row
    csvwriter.writerow(["Total Months:" + str(totalofMonths)])
    csvwriter.writerow(["Total Profit:" + str(total_profit)])
    csvwriter.writerow(["Average Change:" + str(revenueAverage)])
    csvwriter.writerow(["Greatest increase in profits:" + str(maxChange)])
    csvwriter.writerow(["Greatest decrease in profits:" + str(minChange)])
    
