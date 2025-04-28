import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
import sklearn

from sklearn.datasets import _california_housing 

#load the dataset
data = sklearn.datasets.fetch_california_housing()
housing = data.data
print(data.data)

#display the first few rows of the dataset 
print(housing[:5]) # specially for numpy ndarrays

# print(housing.head()) -> specially for pd dataframes

#get the shape of the dataset 
print(housing.shape) # same for both pd dataframe and numpy ndarrays 

#Calculate summary statistics (mean,median,standard deviation)
print("mean =",np.mean([housing[:,0]]))
print("median =",np.median(housing[:,0]))
print("standard deviation =",np.std(housing[:,0]))

#display target variable MedHouseVal 


