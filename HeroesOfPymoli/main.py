'''
Jean-Paul Mitterhofer
10/28/2019
'''

# Dependencies and Setup
import pandas as pd
import os
import csv

# File to Load (Remember to Change These)
file_to_load = os.path.join(".","Resources","purchase_data.csv")

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

#print out the head to view what columns you have
print(purchase_data.head())

#Total number of players df = df.groupby('domain')['ID'].nunique()
total_number_of_players = purchase_data["SN"].value_counts()
print(f"Total number of Players: {len(total_number_of_players)}")

#Purchase Analysis
#Total unique items
unique_items = purchase_data["Item ID"].value_counts()
print(f"Total unique items: {len(unique_items)}")
