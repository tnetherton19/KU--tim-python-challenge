import csv
import os 

input_csv='C:\\Users\\tbnet\\Desktop\\UKED201811DATA5\\02-Homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv'

total_votes=0
candidates=[]
vote_count={}

with open(input_csv) as csv_file:
    csvreader=csv.reader(csv_file)

    for row in csvreader:
    	total_votes +=1
    	if row ['Candidate'] not in candidates:
    		candidates.append(row['Candidate'])
    		vote_count[row['Candidate']]=1
    	elif row['Candidate'] in candidates:
    		vote_count[row['Candidate']] += 1

prior_candiate= 0

print("Election Results")
print("-------------------------------")
print("Total Vote Counts: "+ str(total_votes))
print("-------------------------------")
for key, value in vote_count.items():
    print(key + ": " + str(((float(value/total_votes)*100),1)) + "%" + " (" + str(value)+ ")")
for key, value in vote_count.items():
    if value > prior_candiate:
        most_vote = key
        prior_candiate = value
print("--------------------------------")
print("Winner: " + most_vote)
print("--------------------------------")
