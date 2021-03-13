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

# Save the results to our text file
with open(file_to_save, 'w') as txt_file:

    # Print the final vote count to the terminal
    Election_results = (
        f'\nElection Results\n'
        f'------------------\n'
        f'Total Votes:{total_votes:,}\n'
        f'------------------\n')

    print(Election_results, end='')

    # Save the final vote count to the text file
    txt_file.write(Election_results)

       # Determine the percentage of votes for each candidate by looping through
    # 1. iterate through the candidate list
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate
        votes=candidate_votes[candidate_name]
        # 3. calculate the percentage of votes
        vote_percentage=float(votes)/float(total_votes)*100
        # 4. print the candidate name and percentage of votes
        candidate_results=(f'{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n')

        #print each candidate, their vote count and percentage to the terminal
        print(candidate_results)

        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count
        if(votes>winning_count) and (vote_percentage>winning_percentage):
        # 2. if true then set winning_count=votes and winning percent=vote percentage
            winning_count=votes
            winning_percentage=vote_percentage
            # 3. set the winning_candidate equal tot he candidates name
            winning_candidate=candidate_name

    # print the winning candidates results to the terminal
    winning_candidate_summary = (
        f'----------\n' 
        f'winner: {winning_candidate}\n' 
        f'Winning Vote Count:{winning_count:,}\n' 
        f'Winning percentage: {winning_percentage:.1f}%\n' 
        f'----------\n')

    print(winning_candidate_summary)

    # Save the winning candidates name to the text file
    txt_file.write(winning_candidate_summary)



    

