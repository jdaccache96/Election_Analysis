import os 
import csv
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

#1. Create a county list and county votes dictionary
county_options = []
county_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#2. Track the largest county and county voter turnout 
winning_county = ""
winning_county_count = 0 
winning_county_percentage = 0 

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]

        #3.Extract the county name from each row 
        county_name = row[1]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1 

        #4a. Write an if statement that checks that the county does not match any existing county in the county list 
            #4b. Add the existing county to the list of counties
            #4c. Begin tracking the county's vote count      
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0 
        #5. Add a vote to that county's vote count
        county_votes[county_name] += 1 
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n"
        f"County Votes:\n"
        f"-----------------------\n")

    print(election_results, end="")
   
    txt_file.write(election_results)

    #6a. Write a for loop to get the county from the county dictionary
        #6b. Retrieve the county vote count
        #6c. Calculate the percentage of votes for the county
        #6d. Print the county results in the terminal
        #6e. Save the county votes to a text file 
        #6f. Write an if statement to determine the winning county and get its vote count
    for county_name in county_votes:
        total_county_votes = county_votes[county_name]

        county_vote_percentage = float(total_county_votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {county_vote_percentage:.1f}% ({total_county_votes:,})\n")
        print(county_results)
        txt_file.write(county_results)
    

    #7. Print the county with the largest turnout to the terminal
        if (total_county_votes > winning_county_count) and (county_vote_percentage > winning_county_percentage):
            winning_county_count = total_county_votes
            winning_county_percentage = county_vote_percentage
            winning_county = county_name

    winning_county_summary = (
        f"-------------------\n"
        f"Winning County: {winning_county}\n"
        f"Winning County Vote Count: {winning_county_count:,}\n"
        f"Winning County Vote Percentage: {winning_county_percentage:.1f}%\n"
        f"-------------------\n")
    print(winning_county_summary)

    txt_file.write(winning_county_summary)
    #8. Save the county with the largest turnout to a text file 

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name 

    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------\n")
    print(winning_candidate_summary)
  
    txt_file.write(winning_candidate_summary)
