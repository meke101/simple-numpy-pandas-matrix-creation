# Difference between matrix and dataframe:
# All columns in a matrix must have the same data type (numeric, character, etc.) and the same length. A data frame
# is more general than a matrix, in that different columns can have different modes (numeric, character, factor, etc.)
import pandas as pd

data_frame = pd.read_csv('salaries.csv')


print(data_frame.columns)

