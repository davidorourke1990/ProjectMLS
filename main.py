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

#show how many players per club
print(MLS19Alphabet["Club"].value_counts())

#subsetting columns
Salary_Column1 = MLS19_Salary["Salary"]
print(Salary_Column1)

#subsetting multiple columns to get just last name and Salary
MLS19_Salary = MLS19_Salary[["Last_Name", "Salary",]]
print(MLS19_Salary)

##max salary
print(MLS19["Salary"].max())

#minimum salary
print(MLS19["Salary"].min())

#Obtain the players earning over 1million $ only
Salary_Millionaire = MLS19_Salary[MLS19_Salary["Salary"] > 1000000.00]
print(Salary_Millionaire)

#Number of players earning over 1million $
Salary_Millionaire.count()
print(Salary_Millionaire.count())

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
Team_Summary = MLS19.groupby("Club")["Salary"].agg([min, max, sum])
print(Team_Summary)

#Check for missing values
null_data = MLS19[MLS19.isnull().any(axis=1)]
print(null_data)

#show whoe dataset and indicate tha values that are missing
print(MLS19.isna())

#show overview if there is any data misisng in any of the columns
print(MLS19.isna().any())

#total amount missing in each column
print(MLS19.isna().sum())

#sample of misisng First names
MLS19Name = MLS19[["Last_Name", "First_Name",]]
print(MLS19Name[45:52])

#replace missing first names by combining first and last name columns to create one column called 'Name'
def Fullname(x, y):
    if str(x) == "NaN":
        return str(y)
    else:
        return str(x) + " " + str(y)

MLS19['Name'] = np.vectorize(Fullname)(MLS19['First_Name'], MLS19['Last_Name'])
print(MLS19)

#Now we can drop the excess columns of 'Last_Name' and 'First_Name'
MLS19 = MLS19.drop(['Last_Name', 'First_Name'], axis = 1)
print(MLS19)

#Now we can replace the Players with no defined position value with 'None'
MLS19["Position"].fillna("None", inplace = True)
print(MLS19)

#Run again to check what else remains missing
print(MLS19.isna().sum())

#Number of players according to their positions
print(MLS19["Position"].value_counts())

#Salaries and Guaranteed comp according to playing positions
Salary_Position = MLS19.groupby("Position").mean()
print(Salary_Position)

#Sort the Salary postion by position on pitch


#plot the average salaries by the position of each player
Salary_Position.plot(kind="barh", title="Salary by Playing Position 2019")
plt.show()

#plot average spend of each club on salary on bar chart
Club_Position = MLS19.groupby("Club").mean()
Club_Position.sort_values(by = 'Salary', ascending = False,inplace=True)

plt.figure(figsize=(12,8))
sns.set_style("whitegrid")
sns.barplot(x=Club_Position.index, y=Club_Position["Salary"])
plt.xticks(rotation= 80)
plt.xlabel('Clubs')
plt.ylabel('Salaries')
plt.title('Average Salary per Club 2019')
plt.show()

