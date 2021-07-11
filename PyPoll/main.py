import os
import csv

csvpath=os.path.join('..','Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
    #Variables
    listVotes = []
    listCandidates = []
    khan = []
    correy = []
    li = []
    otooley = []


    for row in csvreader:
        listVotes.append(int(row[0]))
        listCandidates.append(row[2])

    totalVotes = (len(listVotes))
    

#Total up candidates
    for candidate in listCandidates:
        if candidate == "Khan":
            khan.append(listCandidates)
            khanVotes = len(khan)
        elif candidate == "Correy":
            correy.append(listCandidates)
            correyVotes = len(correy)
        elif candidate == "Li":
            li.append(listCandidates)
            liVotes = len(li)
        else:
            otooley.append(listCandidates)
            otooleyVotes = len(otooley)

#Calculate percentages

khanPercent = ((khanVotes/totalVotes)*100)    
correyPercent = ((correyVotes/totalVotes)*100)   
liPercent = ((liVotes/totalVotes)*100)   
otooleyPercent = ((otooleyVotes/totalVotes)*100)   

#Winner if statement
if khanPercent > (correyPercent or liPercent or otooleyPercent):
    winner = "Khan"
elif correyPercent > (khanPercent or liPercent or otooleyPercent):
    winner = "Correy" 
elif liPercent > (correyPercent or khanPercent or otooleyPercent):
    winner = "Li"
else:
    winner = "O'Tooley"

#Print Results
print("Election Results")
print("-------------------------")
print("Total Votes:" + str(totalVotes))
print("-------------------------")
print("Khan:" + str(round(khanPercent,2)) + "(" + str(khanVotes) + ")")
print("Correy:" + str(round(correyPercent,2)) + "(" + str(correyVotes) + ")")
print("Li:" + str(round(liPercent,2)) + "(" + str(liVotes) + ")")
print("O'Tooley:" + str(round(otooleyPercent,2)) + "(" + str(otooleyVotes) + ")")
print("-------------------------")
print("Winner:" + str(winner))
print("-------------------------")

# Specify the file to write to
output_path = os.path.join("..", "Resources", "pyoll.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])

    # Write the second,etc. row
    csvwriter.writerow(["Total Votes:" + str(totalVotes)])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Khan:" + str(round(khanPercent,2)) + "(" + str(khanVotes) + ")"])
    csvwriter.writerow(["Correy:" + str(round(correyPercent,2)) + "(" + str(correyVotes) + ")"])
    csvwriter.writerow(["Li:" + str(round(liPercent,2)) + "(" + str(liVotes) + ")"])
    csvwriter.writerow(["O'Tooley:" + str(round(otooleyPercent,2)) + "(" + str(otooleyVotes) + ")"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Winner:" + str(winner)])
    csvwriter.writerow(["-------------------------"])
