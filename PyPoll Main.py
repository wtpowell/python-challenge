#import tools
import os
import csv

#set up csv pathing
poll_csv = os.path.join("..", "python-challenge", "election_data.csv")

#set up variables to be used later
total_votes = 0
khan_votes = 0
li_votes = 0
correy_votes = 0
otooley_votes = 0


#open csv file and then go through row 2 and tally up votes via the name
with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:

        total_votes += 1

        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1

#set up two lists to store our data gather from pervious lopp
votes = [khan_votes, li_votes, correy_votes, otooley_votes]
candidates = ["Khan", "Li", "Correy", "O'Tooley"]

#set up a dictionary zip so that we can store both strings and integers in one zip and set up a key for said dictionary
dict_candidates_votes = dict(zip(candidates,votes))
winner = max(dict_candidates_votes, key=dict_candidates_votes.get)

#get your percents of the votes
k_percent = (khan_votes/total_votes) * 100
l_percent = (li_votes/total_votes) * 100
c_percent = (correy_votes/total_votes) * 100
o_percent = (otooley_votes/total_votes) * 100


#print to terminal
print("Election Results")
print("-----------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------")
print(f"Khan: {round(float(k_percent))}% {int(khan_votes)} Votes") 
print(f"Li: {round(float(l_percent))}% {int(li_votes)} Votes")
print(f"Correy: {round(float(c_percent))}% {int(correy_votes)} Votes")
print(f"O'Tooley: {round(float(o_percent))}% {int(otooley_votes)} Votes")
print("-----------------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------------")


#export to a txt file 
import sys
sys.stdout = open('PyPoll Analysis.txt', 'w')
print("Election Results")
print("-----------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------")
print(f"Khan: {round(float(k_percent))}% {int(khan_votes)} Votes") 
print(f"Li: {round(float(l_percent))}% {int(li_votes)} Votes")
print(f"Correy: {round(float(c_percent))}% {int(correy_votes)} Votes")
print(f"O'Tooley: {round(float(o_percent))}% {int(otooley_votes)} Votes")
print("-----------------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------------")
sys.stdout.close()