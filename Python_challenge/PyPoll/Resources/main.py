import os

import csv 

electiondatacsv = os.path.join("Python_challenge", "PyPoll", "Resources","election_data.csv")

# Defining variables 
vote_list = []
total_votes = []
Charles_votes = 0
Diana_votes = 0
Raymon_votes = 0

with open(electiondatacsv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    csv.reader(csv_file, delimiter = ",")

    header = next(csv_reader)
    
    # loop through each rows
    for row in csv.reader(csv_file):

        # Use append function to store names into vote_list
        vote_list.append(row[2])
        
        # Track the total months as rows using len function 
        total_votes = len(vote_list)
    
        # Use if loop to count the votes per candidates 
        if (row[2] == 'Charles Casper Stockham'):
            Charles_votes = Charles_votes + 1
        
        elif (row[2] == 'Diana DeGette'):
            Diana_votes = Diana_votes + 1
        
        else:
            Raymon_votes = Raymon_votes + 1

# Calculate each candidate percentage by using figures obtain from above if loop and round off to 3 decimals with round function 
Charles_percentage = round((Charles_votes / total_votes)*100,3)
Diana_percentage = round((Diana_votes / total_votes)*100,3)
Raymon_percentage = round((Raymon_votes / total_votes)*100,3)


# Print out the required information  
print('Election Results:')
print('------------------------')
print('Total Votes:', total_votes)
print('------------------------')
print('Charles Casper Stockham:' + ' ' + str(Charles_percentage) + '% ' + '('+ str(Charles_votes) + ')')
print('Diana DeGette:' + ' ' + str(Diana_percentage) + '% ' + '('+ str(Diana_votes) + ')')
print('Raymon Anthony Doane:' + ' ' + str(Raymon_percentage) + '% ' + '('+ str(Raymon_votes) + ')')
print('------------------------')

# Put each candidate votes into a new list 
votes_in_total = [Charles_votes, Diana_votes, Raymon_votes]

# Use max function to get the maximum value from the list 
max_count_votes = max(votes_in_total)

# Use if function to obtain the winner with most votes and print the winner 
if max_count_votes == Charles_votes :
    print('Winner: Charles Casper Stockham')

elif max_count_votes == Diana_votes :
    print('Winner: Diana DeGette')   

else:
    print('Winner: Raymon Anthony Doane ')
print('------------------------')

output_path = os.path.join("Python_challenge", "PyPoll", "Resources", "Analysis", 'election_results.txt')

with open(output_path, 'w') as output:

# Write the results into a .txt file 
    output.write('Election Results:')
    output.write("\n")
    output.write('------------------------')
    output.write("\n")
    output.write('Total Votes:' + str(total_votes))
    output.write("\n")
    output.write('------------------------')
    output.write("\n")
    output.write('Charles Casper Stockham:' + ' ' + str(Charles_percentage) + '% ' + '('+ str(Charles_votes) + ')')
    output.write("\n")
    output.write('Diana DeGette:' + ' ' + str(Diana_percentage) + '% ' + '('+ str(Diana_votes) + ')')
    output.write("\n")
    output.write('Raymon Anthony Doane:' + ' ' + str(Raymon_percentage) + '% ' + '('+ str(Raymon_votes) + ')')
    output.write("\n")
    output.write('------------------------')
    output.write("\n")
    if max_count_votes == Charles_votes :
        output.write('Winner: Charles Casper Stockham')

    elif max_count_votes == Diana_votes :
        output.write('Winner: Diana DeGette')   

    else:
        output.write('Winner: Raymon Anthony Doane ')
        output.write("\n")
        output.write('------------------------')
   