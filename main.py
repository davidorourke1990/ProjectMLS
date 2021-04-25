import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

MLS19 = pd.read_csv("MLS19.csv")

##print the head
print(MLS19.head())

##print the tail
print(MLS19.tail())

##get the shape of dataset
MLS19.shape
print(MLS19.shape)

##show the dataframe info
MLS19.info()
print(MLS19.info())

##show the columns
MLS19.columns
print(MLS19.columns)

##show the index
MLS19.index
print(MLS19.index)

##describe the dataset
MLS19.describe()
print(MLS19.describe())

##if i wanted to sort by clubs in alphabetical order
MLS19club = MLS19.sort_values("Club")
print(MLS19club)

##sorting by multiple variables
MLS19Alphabet = MLS19.sort_values(["Club", "Last_Name"])
print(MLS19Alphabet)

#sort by salary in ascending order and show top 10 highest earners
MLS19_Salary = MLS19.sort_values("Salary", ascending=False)
print(MLS19_Salary.head(10))
#show the 10 lowest earners
print(MLS19_Salary.tail(10))

#subsetting columns
Salary_Column1 = MLS19_Salary["Salary"]
print(Salary_Column1)

#subsetting multiple columns to get just last name and Salary
Salary_Column2 = MLS19_Salary[["Last_Name", "Salary",]]
print(Salary_Column2)

##max salary
Salary_Column2["Salary"].max()

#minimum salary

#Obtain the players earning over 1million $ only
Salary_Column3 = Salary_Column2[Salary_Column2["Salary"] > 1000000.00]
print(Salary_Column3)

#Number of players earning over 1million $
Salary_Column3.count()
print(Salary_Column3.count())

#Create a new Column to find out difference in Salary and Guaranteed Compensation
MLS19["Comp_Diff"] = MLS19["Guaranteed_Comp"] - MLS19["Salary"]
print(MLS19.head())

#Check who has the largest difference in Salary and Guaranteed Compensation
MLS19Comp = MLS19.sort_values("Comp_Diff", ascending=False)
print(MLS19Comp.head(10))

#summarize numerical data
##Average Salary
print(MLS19_Salary.mean())

##median number
print(MLS19_Salary.median())

##Standard Deviation
print(MLS19_Salary.std())

#Group by Club and Salaries (minimum, max and Total per club)
Team_Summary = MLS19_Salary.groupby("Club")["Salary"].agg([min, max, sum])
print(Team_Summary)

#Number of players according to their positions
print(MLS19["Position"].value_counts())

#Salaries and Guaranteed comp according to playing positions
Salary_Position = MLS19.groupby("Position").mean()
print(Salary_Position)

#Sort the Salary postion by position on pitch


Salary_Position.plot(kind="barh", title="Salary by Playing Position 2019")
plt.show()

#plot sum of each club salary on bar chart
Club_Position = MLS19.groupby("Club").mean()

plt.figure(figsize=(12,8))
sns.set_style("whitegrid")
sns.barplot(x=Club_Position.index, y=Club_Position["Salary"])
plt.xticks(rotation= 80)
plt.xlabel('Clubs')
plt.ylabel('Salaries')
plt.title('Clubs & Salaries')
plt.show()


