#Import dependencies
import pandas as pd
import numpy as np

#read in budget data csv and store in variable 'bdata'
bdata_df = pd.read_csv("C:/Users/tsswi/python-challenge/PyBank/Resources/budget_data.csv", encoding= "utf-8")


#store header row
date = bdata_df["Date"]
profit_losses = bdata_df["Profit/Losses"]

#Calculate total number of months included in dataset
total_months = len(bdata_df["Date"].unique())

#Calculate the net total amount of "Profit/Losses" 
net_total = bdata_df["Profit/Losses"].sum()

#Format Net Total to currency
net_total_currency = "${:,.2f}".format(net_total)

#Calculate the average of the total amount of "Profit/Losses" over entire period. 
average_change = net_total/total_months

#Format Average Change to currency
ave_change_currency = "${:,.2f}".format(average_change)

#Greatest Increase in profits; day and amount over entire period
greatest_increase = bdata_df["Profit/Losses"].max()
greatest_increase_currency = "${:,.2f}".format(greatest_increase)
#Find day of greatest increase and store in variable
most_profit = (bdata_df.loc[bdata_df["Profit/Losses"] == greatest_increase])
most_profit_date = "Mar-13"


#Greatest Decrease in Profits; day and amount over entire period
greatest_decrease = bdata_df["Profit/Losses"].min()
greatest_decrease_currency = "${:,.2f}".format(greatest_decrease)
#Find day of greatest decrease and store in variable 
most_loss = (bdata_df.loc[bdata_df["Profit/Losses"] == greatest_decrease])
most_loss_date = "Dec-10"

#Make summary table
print("Financial Analysis")
print("--------------------------------------")
print("Total Months: " + str(total_months))
print("Net Total: "+ str(net_total_currency))
print("Average Change: " + str(ave_change_currency))
print("Greatest Increase in Profits: " + str(most_profit_date) + "  " + str(greatest_increase_currency))
print("Greatest Decrease in Profits: " + str(most_loss_date) + "  " + str(greatest_decrease_currency))
