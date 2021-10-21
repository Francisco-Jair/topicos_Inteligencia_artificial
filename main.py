import pandas as pd

data = pd.read_table('adult.data', delim_whitespace=True, header=0)

print(data.columns)