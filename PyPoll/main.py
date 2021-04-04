import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join( 'Analysis', 'Election_Results.txt')

county_names = []
county_votes = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    candidate = []
    Totalvotes = 0
    winner_vote = 0
    winning_candidate = ""
    candidate_votes ={}

    for row in csvreader:
        Totalvotes = Totalvotes + 1
        candidate_name = row[2]
        if candidate_name not in candidate:
            candidate.append(candidate_name)
            candidate_votes[candidate_name]= 0
        # else:
        candidate_votes[candidate_name] += 1
    
    final_result = (
        f"Election Results\n"
        f"------------------------\n"
        f"Total Votes: {Totalvotes}\n"
        f"------------------------\n"
        )
    print(final_result)

    for key in candidate_votes:
        votes = candidate_votes.get(key)
        percentage = (votes)/(Totalvotes)*100
        
        if votes > winner_vote:
            winner_vote = votes
            winning_candidate = key
        
        voter_output = f"{key}: {percentage:.3f}% ({votes})\n"
        

        print(voter_output)
    
    winner=(
        f"------------------------\n"
        f"winner: {winning_candidate}\n"
        f"------------------------\n"


    )
    print(winner)

    with open(output_path, "w") as textFile:
    #     Election_Results(

    # final_result = (
    #     "Election Results\n"
    #     "------------------------\n"
    #     "Total Votes: {Totalvotes}\n"
    #     "------------------------\n"
    #     )   
    # winner=(
    #     "------------------------\n"
    #     "winner: {winning_candidate}\n"
    #     "------------------------\n"
    #         ))
        textFile.write(final_result)
        for key in candidate_votes:
            votes = candidate_votes.get(key)
            percentage = (votes)/(Totalvotes)*100
        
            if votes > winner_vote:
                winner_vote = votes
                winning_candidate = key
        
            voter_output = f"{key}: {percentage:.3f}% ({votes})\n"
        

            textFile.write(voter_output)
        textFile.write(winner)
    

    
     
