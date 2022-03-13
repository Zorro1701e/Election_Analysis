# The DATA we need to retrieve.
    # 1. The total number of votes cast. (369,711)
    # 2. A complete lists of Candidates who recieved votes.
    # 3. Percentage of votes each candidate won.
    # 4. Total number of votes each candidate won. 
    # 5. Winner of election based on popular vote.


# Import the datetime class from the datetime module.
#import datetime
# Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
# Print the present time.
#print("The time right now is ", now)
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join(".", "election_results.csv")
file_to_save = os.path.join('.', 'election_analysis.txt')

# 1. Inititalize counter to Zero
total_votes = 0

#Candidate options 
candidate_options = []
# I DECLARE AN EMPTY DICTIONARY!
candidate_votes = {}

#open election results & read file
with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)

        #Read the Header row
        headers = next(file_reader)

    #Print each row in the CSV file.
        for row in file_reader:
            # 2. add to the total vote count..
            total_votes += 1

        #print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate THEN...
        if candidate_name not in candidate_options:
            # ADD it to the list of candidates.
            candidate_options.append(candidate_name)

            # begin tracking THAT candidates vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1


# print the candidate vote dictionary
print(candidate_votes)
   