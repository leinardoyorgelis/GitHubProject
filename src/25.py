import pandas as pd

# Example 1: Reading CSV file with Pandas
df = pd.read_csv('data.csv')

# Example 2: Writing DataFrame to a new CSV file using Pandas
df.to_csv('output.csv', index=False)

# Example 3: Reading CSV file and getting its values using Pandas
values = df.values

# Example 4: Adding columns with values from another DataFrame using Pandas
df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df2 = pd.DataFrame({'col1': [5, 6]})

df3 = pd.concat([df1, df2], axis=1)
print(df3)
