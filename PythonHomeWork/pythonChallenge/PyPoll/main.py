import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pyPollCSVPath = os.path.join("..", "PyPoll","Resources", "election_data.csv")


with open(pyPollCSVPath) as pyPollfile:
    csvReader = csv.reader(pyPollfile, delimiter = ",")
    # initialize counters and totals variables
    count = 0
    khanCount = 0
    correyCount = 0
    LiCount = 0
    tooleyCount = 0
    total = 0
    next(csvReader) # skip the first header
    winner = 0 # use for identifying winner
    
    for row in csvReader:
        count += 1  # main total cvoter count
        if row[2] == "Khan":
            khanCount += 1
        elif row[2] == "Correy":
            correyCount += 1
        elif row[2] == "Li":
            LiCount += 1
        elif row[2] == "O'Tooley":
            tooleyCount += 1
        
    # will uses count total to identify winner with if conditional
    if khanCount > winner:
        winner = khanCount
        status = "khan"
    elif correyCount > winner:
        winner = correyCount
        status = "Correy"
    elif LiCount > winner:
        winner = LiCount
        status = "Li"
    elif tooleyCount > winner:
        winner = tooleyCount
        status = "O'tooley"
    khanPercent = round(khanCount/count*100,4)
    correyPercent = round(correyCount/count*100,4)
    LiPercent = round(LiCount/count*100,4)
    tooleyPercent = round(tooleyCount/count*100,4)
    print(f"-----------------------------")    
    print(f"Total Votes:  {count}")
    print(f"-----------------------------")
    print(f"Khan:  {khanPercent}% ({khanCount})    ") 
    print(f"Correy:  {correyPercent}% ({correyCount})    ") 
    print(f"Li:  {LiPercent}% ({LiCount})    ") 
    print(f"O'Tooley:  {tooleyPercent}% ({tooleyCount})    ")
    print(f"-----------------------------")    
    print(f"Winner:  {status}")
    print(f"-----------------------------")            

    output_file = os.path.join("analysis","output.csv")  # output portion of my script
    with open(output_file, "w") as datafile :
       writer = csv.writer(datafile)
       writer.writerow([f"-----------------------------"])    
       writer.writerow([f"Total Votes:  {count}"])
       writer.writerow([f"-----------------------------"])
       writer.writerow([f"Khan:  {khanPercent}% ({khanCount})    "]) 
       writer.writerow([f"Correy:  {correyPercent}% ({correyCount})    "]) 
       writer.writerow([f"Li:  {LiPercent}% ({LiCount})    "]) 
       writer.writerow([f"O'Tooley:  {tooleyPercent}% ({tooleyCount})    "])
       writer.writerow([f"-----------------------------"])    
       writer.writerow([f"Winner:  {status}"])
       writer.writerow([f"-----------------------------"])          

   