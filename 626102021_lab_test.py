# 1. Define a problem statement
'''
This project analyzes two Facebook network datasets (1684.edges and 1912.edges) to identify user connectivity patterns
and determine the most connected users in each network.
'''
import pandas as pd
import numpy as np
from collections import Counter

# 2. Read the datasets into Python
data1 = pd.read_csv("1684.edges", sep=" ", header=None) # Load dataset 1
data2 = pd.read_csv("1912.edges", sep=" ", header=None) # Load dataset 2
print("Dataset 1 sample:") # printed the selected output of dataset 01
print(data1.head())
print("\nDataset 2 sample:") # printed the selected output of dataset 02
print(data2.head())

# 3. Compute summary statistics
print("\nDataset 1 Statistics")
print("Mean:", np.mean(data1[0]))
print("Minimum value:", np.min(data1[0]))
print("Maximum value:", np.max(data1[0]))
print("Standard deviation:", np.std(data1[0]))

print("\nDataset 2 Statistics")
print("Mean:", np.mean(data2[0]))
print("Minimum value:", np.min(data2[0]))
print("Maximum value:", np.max(data2[0]))
print("Standard deviation:", np.std(data2[0]))


# 4. Design and implement an algorithm
print("\nDesign and implement an algorithm")
def top_users(data):
    users = list(data[0]) + list(data[1])
    connections = Counter(users)
    return connections.most_common(5)

print("Top users in Dataset1:", top_users(data1))
print("Top users in Dataset2:", top_users(data2))