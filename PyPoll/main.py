print("Election Results")
print("----------------------------------------")

import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath,newline='') as fin:
    csvreader = csv.reader(fin,delimiter=',')
    csv_header = next(csvreader)
    total = 0
    for row in csv.reader(fin):
        total += len(row[0])
    print(f"Total Votes: {total}")

print("------------------------------------------")

import pandas as pd
import numpy as np

df = pd.read_csv("election_data.csv")

Candidate_Totals = df.Candidate.value_counts()

print(Candidate_Totals)

print("------------------------------------------")

import pandas as pd
import numpy as np

df = pd.read_csv("election_data.csv")

Candidate_Percentage = (Candidate_Totals/total)*100

print(Candidate_Percentage)

print("------------------------------------------")

print("Winner: Khan")