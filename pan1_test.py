import pandas as pd
# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)

# Create a DataFrame from a list of lists
data_list = [['Alice', None], ['Bob', 30]]
df_list = pd.DataFrame(data_list, columns=['Name', 'Age'])

# Display the DataFrame
print(df)
print(df_list)

# Remove rows with missing values
df_cleaned = df.dropna()

# Fill missing values with a specific value
df_filled = df.fillna(69)


print(df_cleaned)
print(df_filled)

# Create a DataFrame with a string column
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})

# Format 'Name' column to uppercase
df['Name'] = df['Name'].str.upper()

# Display DataFrame
print(df)
