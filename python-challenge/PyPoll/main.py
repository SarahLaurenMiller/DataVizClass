import os, csv
from statistics import mean

csvpath = os.path.join('Resources', 'election_data.csv')

total_voters = []
county = []
candidates = []
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
 
with open(csvpath,newline="", encoding="utf-8") as election:
    csvreader = csv.reader(election,delimiter=",") 
    header = next(csvreader) #skip header

    for row in csvreader:
        total_voters.append(row[0])

        if row[2] == "Khan": 
            Khan_votes +=1 #counting instances of candidates
        elif row[2] == "Correy":
            Correy_votes +=1
        elif row[2] == "Li": 
            Li_votes +=1
        elif row[2] == "O'Tooley":
            OTooley_votes +=1

candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [Khan_votes, Correy_votes,Li_votes,OTooley_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
Khan_percent = (Khan_votes/(len(total_voters))) *100
Correy_percent = (Correy_votes/(len(total_voters))) * 100
Li_percent = (Li_votes/(len(total_voters)))* 100
OTooley_percent = (OTooley_votes/(len(total_voters))) * 100

print(f'Election Results')
print(f"----------------------------")
print(f'Total votes: {len(total_voters)}')
print(f"----------------------------")
print(f"Khan: {Khan_percent:.3f}% ({Khan_votes})")
print(f"Correy: {Correy_percent:.3f}% ({Correy_votes})")
print(f"Li: {Li_percent:.3f}% ({Li_votes})")
print(f"O'Tooley: {OTooley_percent:.3f}% ({OTooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

with open ("pypoll_output.txt", "w") as output:
    output.write("Election Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total votes: {len(total_voters)}\n")
    output.write("----------------------------\n")
    output.write(f"Khan: {Khan_percent:.3f}% ({Khan_votes})\n")
    output.write(f"Correy: {Correy_percent:.3f}% ({Correy_votes})\n")
    output.write(f"Li: {Li_percent:.3f}% ({Li_votes})\n")
    output.write(f"O'Tooley: {OTooley_percent:.3f}% ({OTooley_votes})\n")
    output.write("----------------------------\n")
    output.write(f"Winner: {key}\n")
    output.write("----------------------------\n")

# Scratch work
# Determine candidates 
def unique(candidates): 
    unique_list = [] 
    for x in candidates: 
        if x not in unique_list: 
            unique_list.append(x) 
    for x in unique_list: 
        print(x)
#unique(candidates)
