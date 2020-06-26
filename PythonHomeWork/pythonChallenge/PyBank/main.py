import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pyBankCSVPath = os.path.join("..", "PyBank","Resources", "budget_data.csv")


with open(pyBankCSVPath) as pyBankfile:
    csvReader = csv.reader(pyBankfile, delimiter = ",")
    count = 0
    total = 0
    next(csvReader)
    max = 0
    min = 0
    for row in csvReader:
        if int(row[1]) > max:
            max = int(row[1])
        if int(row[1]) < min:
            min = int(row[1])
        total += int(row[1])
        count += 1
    print(f" Total Months : {count}")
    print(f" Total :        {total}")
    print(f" Total :        avg change(NaN)")
    print(f"Greatest Increase in Profits:  {max}")
    print(f"Greatest decrease in Profits:  {min}")

    output_file = os.path.join("analysis","output.csv")
    with open(output_file, "w") as datafile :
       writer = csv.writer(datafile)
       writer.writerow([f" Total Months : {count}"])
       writer.writerow([f" Total :        {total}"])
       writer.writerow([f" Total :        avg change(NaN)"])
       writer.writerow([f"Greatest Increase in Profits:  {max}"])
       writer.writerow([f"Greatest Decrease in Profits:  {min}"])