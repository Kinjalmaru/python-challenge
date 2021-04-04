import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join( 'Analysis', 'Financial_analysis.txt')

with open(csvpath) as csvfile:
  
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header= next(csvreader)
    Totalmonths = 1
    Greatest = 0
    Lowest = 999999999
    Greatest_month = ""
    Lowest_month = ""
    net_change_list = []
    first_value = next(csvreader)
    prev_change = int(first_value[1])
    Total = int(first_value[1])
    current = []
    average = 0

    for row in csvreader:
        Totalmonths = Totalmonths + 1
        Total += int(row[1])
        net_change = int(row[1]) - prev_change
        prev_change = int(row[1])
        if Greatest < net_change:
            Greatest = net_change
            Greatest_month = str(row[0])
        else:
            Greatest
        if Lowest > net_change:
            Lowest = net_change
            Lowest_month = str(row[0])
        else:
            Lowest
        
        net_change_list = net_change_list + [net_change]
        average = sum(net_change_list)/len(net_change_list)



    Financial_Analysis = (
        f"Financial Analysis\n"
        f"-------------------------------\n"
        f"TotalMonths:  {Totalmonths}\n"
        f"Total: $  {Total}\n"
        f"Average Change: ${average:.2f}\n"
        f"Greatest Increase in Profits :" + str(Greatest_month) + " ($" + str(Greatest) +")\n"
        f"Lowest Decrease in Profits :" + str(Lowest_month) + " ($" + str(Lowest) + ")")
    print(Financial_Analysis)

    with open(output_path, "w") as textFile:
            
       
        textFile.write(Financial_Analysis)


    