# The DATA we need to retrieve.
    # 1. The total number of votes cast.
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
   
with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)

        #Read the Header row
        headers = next(file_reader)

        #Print each row in the CSV file.
        for row in file_reader:
            print(headers)