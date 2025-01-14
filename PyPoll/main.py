# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
votes_cand_1 = 0  # Tracks the total votes for Charles Casper Stockham
votes_cand_2 = 0  # Tracks the total votes for Diana Degette
votes_cand_3 = 0  # Tracks the total number of votes for Raymond Anthony Doanev

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
votes = []
percentages = []



# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        name = row[2]

        # If the candidate is not already in the candidate list, add them
        if name not in candidates:
            candidates.append(name)

        # add a vote to the candidates count
        if name == "Charles Casper Stockham":
            votes_cand_1 += 1
        elif name == "Diana DeGette":
            votes_cand_2 += 1
        elif name == "Raymon Anthony Doane":
            votes_cand_3 += 1

# Put the individual vote counts in a list
votes = [votes_cand_1, votes_cand_2, votes_cand_3]

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print Header (to terminal)
    print()
    print("Election Results")
    print("------------------------------------------")   

    # Print the total vote count (to terminal)
    print(f'Total Votes: {total_votes}')
    print("------------------------------------------")   

    # Write the total vote count to the text file
    txt_file.write("Total Votes: " + str(total_votes) + " ")

    # Loop through the candidates to determine vote percentages and identify the winner

    # Get the vote count and calculate the percentage
    for value in votes:
        percent = round((value / total_votes) * 100, 3)
        percentages.append(percent)                         # add our percentages to a new list
        

    # Update the winning candidate if this one has more votes

    # Initialize our variable
    winner = candidates[0]

    # Run a for loop to compare the vote totals and potentially change our winner
    for i in range(1,len(votes)):
        if votes[i] > votes[i-1]:
             winner = candidates[i] 

    # Print and save each candidate's vote count and percentage
    for i in range(0, len(candidates)):
        print(f' {candidates[i]}: {percentages[i]}% ({votes[i]})  ')

    print("------------------------------------------")  

    # Generate and print the winning candidate summary
    print(f'Winner: {winner}')


    # Save the winning candidate summary to the text file
    for i in range(0, len(candidates)):
        txt_file.write(f'{candidates[i]}: {percentages[i]}% ({votes[i]})')

    # Print the winner to the text file    
    txt_file.write(f' Winner: {winner}')