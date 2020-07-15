# Difference between matrix and dataframe:
# All columns in a matrix must have the same data type (numeric, character, etc.) and the same length. A data frame
# is more general than a matrix, in that different columns can have different modes (numeric, character, factor, etc.)
import numpy as np
import pandas as pd

matrix = np.arange(0, 10).reshape(5, 2)

df = pd.DataFrame(data=matrix, columns=['A','B'])

print(df)

# Read a data frame from a file:
data_frame = pd.read_csv('salaries.csv')

print(data_frame)

# For extra info e.g. mean
print(data_frame.describe())