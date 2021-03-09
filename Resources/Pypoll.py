# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load=os.path.join('election_results.csv')

# Assign a variable to save ethe file to a path
file_to_save=os.path.join('analysis','election_analysis.txt')

# 1. Initialize a total vote counter.
total_votes=0

# Candidate options
candidate_options=[]

# Declare empty dictionary
candidate_votes={}

# Winning candidate and winning count tracker
winning_candidate=''
winning_count=0
winning_percentage=0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    # Read the header row
    headers=next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:

        # 2. Add to the total vote count.
        total_votes+=1

        # Print the candidate name for each row
        candidate_name=row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
            
        # 3. Add a vote to taht candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through
# 1. Iterate through the candidate list
for candidate_name in candidate_votes:
    # 2. retrieve vote count of a candidate
    votes=candidate_votes[candidate_name]
    # 3. calculate the percentage of votes
    vote_percentage=float(votes)/float(total_votes)*100
    # 4. print the canddiate name and percentage of votes
    print(f'{candidate_name}: received {vote_percentage: .1f}% of the vote.')


# Determine winning vote count and candidate
# 1. determine if the votes are greater than the winning count
if(votes>winning_count) and (vote_percentage>winning_percentage):
    # 2. if true then set the winning_count = to the votes and set winning_percentage= to vote_percentage
    #vote percentage
    winning_count=votes
    winning_percentage=vote_percentage
    # 3. set the winning_candidate equal to the candidates name
    winning_candidate=candidate_name

# To do: print out each candidates name, vote count, and percentage of votes to the terminal
print(f'{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n')

# for candidate in candidate_votes
winning_candidate_summary=(
    f'----------------------------------\n'
    f'Winner:{winning_candidate}\n'
    f'Winning vote count:{winning_count:,}\n'
    f'Winning percentage:{winning_percentage:.1f}%\n'
    f'----------------------------------\n')

print(winning_candidate_summary)






