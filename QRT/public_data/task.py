import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('x_train.csv')

# Function to replace outliers with the median based on the interquartile range
def replace_outliers_with_median(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    median = df[column].median()
    df[column] = df[column].apply(lambda x: median if x < lower_bound or x > upper_bound else x)
    return df

# Apply the function to replace outliers in each numeric column
numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
numeric_columns.remove('DAY_ID')
for col in numeric_columns:
    df = replace_outliers_with_median(df, col)

# Fill NaN values with the median of the column or 0
for col in df.columns:
    if df[col].isna().any():  # Check if there are any NaN values in the column
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':
            # Replace NaN with the median
            df[col].fillna(df[col].median(), inplace=True)
        else:
            # If non-numeric, you can choose to fill with a placeholder value or just skip
            # For example, if you want to fill with a string 'missing', uncomment the next line
            # df[col].fillna('missing', inplace=True)
            pass  # Or replace 'pass' with 'df[col].fillna(0, inplace=True)' to fill with zeros


# Replace 'column_name' with the name of the column you want to sort by
# Set 'ascending=True' for ascending order, and 'ascending=False' for descending order
df_sorted = df.sort_values(by='DAY_ID', ascending=True)

# To reset the index after sorting and drop the old index
df_sorted.reset_index(drop=True, inplace=True)

# Save the reordered DataFrame to a new CSV file if desired
df_sorted.to_csv('reordered_x_train.csv', index=False)

# Optionally, print the sorted DataFrame to the console
print(df_sorted)

# Define the x-axis as the 'DAY_ID' column from the DataFrame
x = df_sorted['DAY_ID']

# Prepare the figure
plt.figure(figsize=(14, 7))  # Set the figure size (optional)

# Create a list of column names you want to plot
# Assuming that the first two columns are 'ID' and 'DAY_ID' and should not be plotted
columns_to_plot = df_sorted.columns[3:]

# Plot each column against 'DAY_ID'
for column in columns_to_plot:
    plt.plot(x, df_sorted[column], label=column)

#plt.plot(x, df_sorted['DE_RAIN'], marker='.', linestyle='-')

plt.xlabel('DAY_ID')  # X-axis label
plt.ylabel('Values')  # Y-axis label
plt.title('Values vs. DAY_ID')  # Title of the plot
plt.legend()  # Show legend

plt.grid(True)  # Show grid
plt.tight_layout()  # Fit the plot nicely into the figure area

# Display the plot
plt.show()