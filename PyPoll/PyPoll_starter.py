#create file path across operating systems
import os
#module for reading CSV files
import csv

#set path for file
csvpath = os.path.join('Resources','election_data.csv')

total_votes_count = 0
candidates = []
candidate_vote_count = {}

#open the CSV
with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    for row in csvreader:
        total_votes_count = total_votes_count + 1 

        candidate = row[2]    
      
        if candidate not in candidates:
            #if the candidate is not already in the candidates list, then append candidate to candidates list
            candidates.append(candidate)
            #candidate is added as key and value initialized to 1
            candidate_vote_count[candidate] = 1 

        elif candidate in candidates:
            # If the candidate is already in the dictionary, increments their vote count by 1
            candidate_vote_count[candidate] = candidate_vote_count[candidate] + 1

#max() function checks each candidate's vote count (value) and returns candidate (key) with the highest count
winner = max(candidate_vote_count, key = candidate_vote_count.get)               

results = (            
    "\nElection Results\n"
    "----------------------------\n"   
    f"Total Votes: {total_votes_count}\n"
    "----------------------------\n"
)
    #loop through both the candidate (key) and votes (value) in candidate_vote_count dictionary and print them
    #calculate vote percentage by taking each votes (valte) and dividing it by total_votes_count
    #print the candidate's name, vote percentage (formatted to 3 decimal places) and the total votes they received
for candidate, votes in candidate_vote_count.items():
    percentage = (votes / total_votes_count) * 100
    results = results + f"{candidate}: {percentage:.3f}% ({votes})\n"

results = results + (
    "----------------------------\n"
    f"Winner: {winner}\n"
    "----------------------------\n"
)

#print the results
print(results)

output_path = os.path.join('analysis','election_analysis.txt')
with open(output_path, mode = 'w') as textfile:
    textfile.write(results)
