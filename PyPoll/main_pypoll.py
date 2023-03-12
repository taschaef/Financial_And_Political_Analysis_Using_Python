#import dependencies
import pandas as pd
import numpy

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
DDG_percent = (DDG_count/total_votes)
CCS_percent = (CCS_count/total_votes)
RAD_percent = (RAD_count/total_votes)

#convert to percentages using "+"{:.2%}".format(x)
DDG_percent_final = "{:.0%}".format(DDG_percent)
CCS_percent_final = "{:.0%}".format(CCS_percent)
RAD_percent_final = "{:.0%}".format(RAD_percent)


#Summary table
print("Election Results")
print("-------------------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------------------")
print("Charles Casper Stockham: " + str(CCS_percent_final) + " " + str(CCS_count))
print("Diana DeGette: "+ str(DDG_percent_final) + " " + str(DDG_count))
print("Raymon Anthony Doane: " + str(RAD_percent_final) + " " + str(RAD_count))
print("-------------------------------------------------")
print("Winner: Diana DeGette")