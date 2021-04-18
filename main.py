import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("MLS17.csv")

##print the head
print(dataset.head())

### check for missing values
print(dataset.isnull().sum())
