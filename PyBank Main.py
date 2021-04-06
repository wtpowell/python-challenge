#import tools
import os
import csv

#define the path for the csv file
budget_csv = os.path.join("..", "python-challenge", "budget_data.csv")

#open said csv
with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#define headers
    csv_header = next(csvreader) 
   
#define lists
    total_months = []
    profit = []
    profit_average = []


#go through each row and collect information for amount of months as well as the total profit number
    for row in csvreader:
        total_months.append(row[0])
        profit.append(int(row[1]))

#go through row 1 and find the difference between each number and put that into a list from above        
    for i in range(len(profit)-1):
        profit_average.append(profit[i+1]-profit[i])


#collect max and min from profit average list
max_increase = max(profit_average)
max_decrease = min(profit_average)

#find the corresponding dates for the max and min
max_increase_date = profit_average.index(max(profit_average))    
max_decrease_date = profit_average.index(min(profit_average))  
    
#print to terminal        
print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total Profits: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_average)/len(profit_average),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_date]} ${(max_increase)}")  
print(f"Greatest Decrease in Profits: {total_months[max_decrease_date]} ${max_decrease}")   

#print into a txt file
import sys
sys.stdout = open('PyBank Analysis.txt', 'w')    
print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total Profits: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_average)/len(profit_average),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_date]} ${(max_increase)}")  
print(f"Greatest Decrease in Profits: {total_months[max_decrease_date]} ${max_decrease}")
sys.stdout.close()
