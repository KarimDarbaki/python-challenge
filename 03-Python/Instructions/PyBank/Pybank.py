
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')



    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    total=0
    profit_losses=0
    pre_value=0

    for row in csvreader:
      #  print(row[1])
        total=total+1
        profit_losses=profit_losses+int(row[1])
        net_change=int(row[1])-pre_value
        pre_value=int(row[1])  
        
       # ave_change=int(pre_value)/(total)
         

    print("Financial Analysis")   
    print("----------------------------------")
    print("Total months = "+ str(total))
    print("Total="+str(profit_losses))
    print("Average Change = "+str(ave_change))    
