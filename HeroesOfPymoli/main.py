'''
Jean-Paul Mitterhofer
10/28/2019
'''

# Dependencies and Setup
import pandas as pd
import os

# File to Load (Remember to Change These)
file_to_load = os.path.join(".","Resources","purchase_data.csv")

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
print(purchase_data.head())
print("\n")

##################################################

#Used unique function to give me the unique values. This turns the dataframe to a dict
group_number_of_players = purchase_data["SN"].nunique()

#Create data frame to display data
df_player = pd.DataFrame({
    "Total Players": [group_number_of_players]
})

print(df_player)
print("\n")

##################################################

#Unique Items
unique_items = purchase_data["Item ID"].value_counts()
unique_items = unique_items.count()
#Average Price
total_avg_price = purchase_data["Price"].mean()
#Number of Purchases
total_num_of_pur = purchase_data["Item Name"].count()
#Total Revenue
total_rev = purchase_data["Price"].sum()
#creating a summary dataframe
summary_df = pd.DataFrame({
    'Number of Unique Items': [unique_items],
    'Average Price': "${:.2f}".format(total_avg_price),
    'Number of Purchases': [total_num_of_pur],
    'Total Revenue': "${:,.2f}".format(total_rev)
})

print(summary_df)
print("\n")

##################################################

#creating a copy of the data frame
gender = purchase_data[["SN", "Gender"]].copy()
#drop duplicate SN to have the true amount of gender
gender.drop_duplicates("SN", keep = "first", inplace = True)
#The count of Gender
gender_count_df = gender["Gender"].value_counts()
# #Find the percentage of Genders within the DF
gender_per_df = gender_count_df/gender["Gender"].count()
# #Creating a data frame summary
demographics_summary = pd.DataFrame ({
    "Total Count":gender_count_df, 'Percentage of Players': gender_per_df.map("{:.2%}".format)
})
print(demographics_summary)
print("\n")

##################################################

#a copy of purchase data to drop duplicates form column SN
purchase_date_copy = purchase_data.copy()
#drop duplicate SN to have the true amount of gender
purchase_date_copy.drop_duplicates("SN", keep = "first", inplace = True)
#group copy by gender
grouped_gender_df_copy = purchase_date_copy.groupby(["Gender"])
#group by gender
grouped_gender_df = purchase_data.groupby(["Gender"])

#Purchase count
gender_purchase_count = grouped_gender_df["Price"].count()
#Average purchase
gender_avg_purchase = grouped_gender_df["Price"].mean()
#Total purchase price
gender_total_purchase_value = grouped_gender_df["Price"].sum()
#Average total purchase per person
gender_avg_total = grouped_gender_df["Price"].sum()/grouped_gender_df_copy["Gender"].count()

#DF for Purchase Analysis
purchasing_analysis = pd.DataFrame ({
    "Purchase Count":gender_purchase_count, 
    'Average Purchase Price': gender_avg_purchase.map("${:,.2f}".format),
    'Total Purchase Value': gender_total_purchase_value.map("${:,.2f}".format), 
    'Avg Total Purchase per Person': gender_avg_total.map("${:,.2f}".format)
})
print(purchasing_analysis)
print("\n")

##################################################

#Defining my bin
bins = [0, 9, 14, 19, 24, 29, 34, 39, 99]
#Defining my loabel that is going on my bin, Label always has one less then bin
age_range_label = ["< 10","10-14","15-19","20-24","25-29","30-34","35-39","40 +"]
#Using the cut function to create age range column, that adds the bin corelating with the age
purchase_date_copy["Age Range"] = pd.cut(purchase_date_copy["Age"], bins, labels = age_range_label)
#Count the bins that the ages are stored in 
demographics_total_count = purchase_date_copy["Age Range"].value_counts()
#Divide each age count value with the total age amount of to get the percentage
demographics_percentage = demographics_total_count/purchase_date_copy["Age Range"].count()
#Add the data into a dataframe and format to round to the nearest two decimal place
demographics_table = pd.DataFrame ({
    "Total Count": demographics_total_count, "Percentage of Players": demographics_percentage.map("{:.2%}".format)
})
#Sorting the index from ascending order
demographics_table = demographics_table.sort_index()
print(demographics_table)
print("\n")

##################################################

#Create a copy of purchase data that has duplicate SN, which also has all price invoices
purchase_analysis_data = purchase_data.copy()
#Using the cut function to create age range column, that adds the bin corelating with the age
purchase_analysis_data["Age Range"] = pd.cut(purchase_analysis_data["Age"], bins, labels = age_range_label)
#Group the data frame by column Age Range 
grouped_analysis_data = purchase_analysis_data.groupby(["Age Range"])
#Find purchase count of price
age_purchasing_count = grouped_analysis_data["Price"].count()
#Find the average purchase price
age_avg_purchasing_price = grouped_analysis_data["Price"].mean()
#Find the total value for each age range
age_total_purchase_value = grouped_analysis_data["Price"].sum()
#using the purchase data copy from previous since duplicate SN are not there, create a count of price
per_person_count = purchase_date_copy.groupby(["Age Range"])["Price"].count()
#Find the age total per person by dividing sum with count per person
age_total_purchase_per_person = age_total_purchase_value/per_person_count

#Create a data frame    
age_purchas_analysis = pd.DataFrame ({
    "Purchase Count": age_purchasing_count, 
    "Average Purchase Price": age_avg_purchasing_price.map("${:,.2f}".format),
    "Total Purchase Value": age_total_purchase_value.map("${:,.2f}".format),
    "Avg Total Purchase per Person": age_total_purchase_per_person.map("${:,.2f}".format)
})

print(age_purchas_analysis)
print("\n")

##################################################

#Group by SN
top_spenders = purchase_data.groupby(["SN"])
#Count the number of users spent
spender_count = top_spenders["Price"].count()
#Average Purchase Price
spender_avg_purchase_price = top_spenders["Price"].mean()
#Total Purchase Value
spender_tot_purchase_value = top_spenders["Price"].sum()
#Created a summary data frame
top_spenders_summary = pd.DataFrame({
    "Purchase Count" : spender_count,
    "Average Purchase Price": spender_avg_purchase_price.map("${:,.2f}".format),
    "Total Purchase Value": spender_tot_purchase_value
})

#sort the Top SPender Summary by descedning order
sort_top_spenders_summary = top_spenders_summary.sort_values("Total Purchase Value", ascending = False)
#After sorting format the column Total Purchase Value. If you format before, it changes the descending order
sort_top_spenders_summary["Total Purchase Value"] = sort_top_spenders_summary["Total Purchase Value"].map("${:,.2f}".format)
#print head
print(sort_top_spenders_summary.head())
print("\n")

##################################################

#Retrieve the Item ID, Item Name, and Item Price columns
popular_items = purchase_data[["Item ID", "Item Name", "Price"]]
#Group by Item ID and Item Name
group_popular_items = popular_items.groupby(["Item ID","Item Name"])
#Count of items and rename data so no scalar values error occurs
popular_purchas_count = group_popular_items.count()

#Mean Avg of items and rename data so no scalar values error occurs
popular_item_price = group_popular_items.mean()

#Sum of items and rename data so no scalar values error occurs
popular_item_sum = group_popular_items.sum()

#Create a Data frame
most_popular_items = pd.DataFrame({
    "Purchase Count":popular_purchas_count["Price"],
    "Item Price": popular_item_price["Price"],
    "Total Purchase Value": popular_item_sum["Price"]
})

#Formatting the item price and total purchase value
most_popular_items["Item Price"] = most_popular_items["Item Price"].map("${:,.2f}".format)
most_popular_items["Total Purchase Value"] = most_popular_items["Total Purchase Value"].map("${:,.2f}".format)
#Sort values from descending purchase count
sort_most_popular_items = most_popular_items.sort_values("Purchase Count", ascending = False)

print(sort_most_popular_items.head())
print("\n")

##################################################

#Create a function to convert string currency to float
#remove $, commas, and convert to float
def convert_cur(val):
    if type(val) == str:
        new_val = val.replace(',','').replace('$', '')
    else:
        return float(val) 
    return float(new_val)

#Apply the function to the Total Purchase Value
most_popular_items["Total Purchase Value"] = most_popular_items["Total Purchase Value"].apply(convert_cur)
#Sort column Total Purchase Value
sort_total_purchase_items = most_popular_items.sort_values("Total Purchase Value", ascending = False)
#Applu curency to Total Purchas Value
sort_total_purchase_items["Total Purchase Value"] = sort_total_purchase_items["Total Purchase Value"].map("${:,.2f}".format)

sort_total_purchase_items.head()

########################END##########################