import pandas as pd
import numpy as np

# Sample data with None values in the DataFrame
data1 = {'A': [1, 2, None], 'B': [None, 4, None]}
data2 = {'A': [1, 2, None], 'B': [None, 4, None]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Convert None values to numpy.nan in both DataFrames
df1_nan = df1.replace({None: np.nan})
df2_nan = df2.replace({None: np.nan})

# Compare DataFrames using equals() method
are_equal = df1_nan.equals(df2_nan)

print(are_equal)  # Output: True
