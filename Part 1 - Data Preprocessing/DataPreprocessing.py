#importing libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importing data

data = pd.read_csv('Data.csv')
X=data.iloc[:, :-1].values
Y=data.iloc[:, :3].values

#testing for an output
print(data.head(2))

#handling missing values
from sklearn.preprocessing import imputer