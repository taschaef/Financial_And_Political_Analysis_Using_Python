#import dependencies
import pandas as pd
import numpy
import csv

#read in csv with Pandas
edata_df = pd.read_csv("C:/Users/tsswi/python-challenge/PyPoll/Resources/election_data.csv", encoding= "utf-8")

#store header row
ballot_id = edata_df["Ballot ID"]
country = edata_df["County"]
candidate = edata_df["Candidate"]

#count total number of votes cast
total_votes = edata_df["Ballot ID"].nunique()

#find how many votes each candidate won
candidate_count = edata_df["Candidate"].value_counts()

#Store individual values in variables for arithmetic
DDG_count = 272892
CCS_count = 85213
RAD_count = 11606

#Calculate percentages of votes won
DDG_percent = (DDG_count/total_votes)*100
CCS_percent = (CCS_count/total_votes)*100
RAD_percent = (RAD_count/total_votes)*100

#convert to percentages using "+"{:.3f}".format(x)
DDG_percent_final = "{:.3f}".format(DDG_percent)
CCS_percent_final = "{:.3f}".format(CCS_percent)
RAD_percent_final = "{:.3f}".format(RAD_percent)


#Summary table
#print("Election Results")
#print("-------------------------------------------------")
#print("Total Votes: " + str(total_votes))
#print("-------------------------------------------------")
#print("Charles Casper Stockham: " + str(CCS_percent_final) + " " + str(CCS_count))
#print("Diana DeGette: "+ str(DDG_percent_final) + " " + str(DDG_count))
#print("Raymon Anthony Doane: " + str(RAD_percent_final) + " " + str(RAD_count))
#print("-------------------------------------------------")
#print("Winner: Diana DeGette")

#F string summary table 
PyPoll_analysis = (f'Election Results \n'
                 f'------------------------------------ \n'
                 f'Total Votes: {total_votes} \n'
                 f'------------------------------------ \n'
                 f'Charles Casper Stockham: {CCS_percent_final}% ({CCS_count}) \n'
                 f'Diana DeGette: {DDG_percent_final}% ({DDG_count}) \n'
                 f'Raymon Anthony Doane: {RAD_percent_final}% ({RAD_count}) \n'
                 f'------------------------------------- \n'
                 f'Winner: Diana DeGette \n')

print(PyPoll_analysis)

#write text to folder analysis
with open("C:/Users/tsswi/python-challenge/PyPoll/analysis/PyPoll_analysis.txt", "w", encoding= "utf-8") as newtxt2:
    newtxt2.write(PyPoll_analysis)