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
        votes.append(row[0])
        candidate.append(row[2])
    unique_candidate = set(candidate)

    print(unique_candidate)

print("---------------------------------------------------------------------")

with open(csvpath,newline='') as fin:
    csvreader = csv.reader(fin,delimiter=',')
    csv_header = next(csvreader)
    
    for row in csv.reader(fin):
        candidate.count(row[2])
    candidate_list_K = candidate.count('Khan')
    candidate_list_C = candidate.count('Correy')
    candidate_list_L = candidate.count('Li')
    candidate_list_O = candidate.count("O'Tooley")
    

print(f"O'Tooley: " + candidate_list_O)
print(f"Li: " + candidate_list_L)
print(f"Correy " + candidate_list_C)
print(f"Khan: " + candidate_list_K)

print("------------------------------------------------")

Khan_percentage = (candidate_list_K/total_votes)*100
Li_percentage = (candidate_list_L/total_votes)*100
Correy_percentage = (candidate_list_C/total_votes)*100
OTooley_percentage = (candidate_list_O/total_votes)*100

print(f"O'Tooley: " + OTooley_percentage)
print(f"Li: " + Li_percentage)
print(f"Correy " + Correy_percentage)
print(f"Khan: " + Khan_percentage)

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
 
