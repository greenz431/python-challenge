print("Election Results")
print("----------------------------------------")

import os
import csv

votes = []
candidate = []


csvpath = os.path.join("election_data.csv")

with open(csvpath,newline='') as fin:
    csvreader = csv.reader(fin,delimiter=',')
    csv_header = next(csvreader)

    for row in csv.reader(fin):
        votes.append(row[0])
    total_votes = set(votes)
print(f"Total Votes: " + str(len(total_votes)))

print("------------------------------------------")

with open(csvpath,newline='') as fin:
    csvreader = csv.reader(fin,delimiter=',')
    csv_header = next(csvreader)

    for row in csv.reader(fin):
        candidate.append(row[2])
    unique_candidate = set(candidate)

    print(unique_candidate)

print("---------------------------------------------------------------------")

with open(csvpath,newline='') as fin:
    csvreader = csv.reader(fin,delimiter=',')
    csv_header = next(csvreader)
    
O_Tooley = candidate.count("O'Tooley")
Li = candidate.count('Li')
Correy = candidate.count('Correy')
Khan = candidate.count('Khan')

print(f"O'Tooley: " + str(O_Tooley))
print(f"Li: " + str(Li))
print(f"Correy " + str(Correy))
print(f"Khan: " + str(Khan))

print("------------------------------------------------")

Khan_percentage = (Khan/len(total_votes))*100
Li_percentage = (Li/len(total_votes))*100
Correy_percentage = (Correy/len(total_votes))*100
OTooley_percentage = (O_Tooley/len(total_votes))*100

print(f"O'Tooley: " + str(OTooley_percentage))
print(f"Li: " + str(Li_percentage))
print(f"Correy " + str(Correy_percentage))
print(f"Khan: " + str(Khan_percentage))

print("-------------------------------------------------")

print("Winner: Khan")

file = open("main.txt","w")
file.write(f"Election Results"
  "-------------------------"
  "Total Votes: 3521001"
  "-------------------------"
  "Khan: 63.000% (2218231)"
  "Correy: 20.000% (704200)"
  "Li: 14.000% (492940)"
  "O'Tooley: 3.000% (105630)"
  "-------------------------"
  "Winner: Khan")


file.close()
 
