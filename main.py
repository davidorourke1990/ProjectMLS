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

##sort my multiple variables
MLS19Alphabet = MLS19.sort_values(["Club", "Last_Name"])
print(MLS19Alphabet)

#if i wanted to sort by salary
MLS19_Salary = MLS19.sort_values("Salary", ascending=False)
print(MLS19_Salary.head())
