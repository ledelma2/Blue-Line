
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import csv


file = r'Food_Inspections.csv'
file2 = r'restaurants_60601-60606.csv'
file3 = r'reviews_60601-60606.csv'

read1 = pd.read_csv(file) #food inspection
restarauntInFoodInspection = read1['AKA Name'].values

read2 = pd.read_csv(file2) #restaraunts
restarauntInRestaraunts = read2['name'].values

#read3 = pd.read_csv(file3, error_bad_lines=False)

csv = open("query4.csv", "w")
csv.write("Passes, Fails, Conditional Pass\n")

for index, rows in restarauntInFoodInspection:
    resultColumn = (index, rows["Inspection Type"])


print('Max', read1['Zip'].max()) #testing
print('Min', read1['Zip'].min()) #testing

print(type(restarauntInFoodInspection)) #type

#To be Done
#City of Chicago food inspection download ———————————
#Dba name aka name is the same as restaurant name as yelp ——————————
#Collect data from both of them in query ——————————
#Pandas library to pull data ——————————
#One object for food inspection and one for restaurant ——————————
#Iterate over the records (loop) ——————————
#Using name of restaurant lookup in food inspection
#Aka name column == restaurant name
#One restaurant will get ,multiple records in food inspection results
#Count passes and fails and conditional pass -> choose variable and add to it
#Yelp review -> avg review rating (might take too much time) get this from TA provided them
#Query that as same way

#Plot avg review rating against pass/fails/conditionals

csv.close()