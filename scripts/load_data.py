import pandas as pd

""" Checking and cleaning estat_isoc_ci_ac_i$defaultview_filtered.tsv before loading into database
"""

# Print first 3 lines of the TSV file to preview data format
with open("../data/estat_isoc_ci_ac_i$defaultview_filtered.tsv") as f:
    for i in range(3):
        print(f.readline())

# Read TSV file into pandas dataframe, specifying tab separator
df = pd.read_csv('../data/estat_isoc_ci_ac_i$defaultview_filtered.tsv', sep='\t')

# Split the first column that contains multiple fields separated by commas into separate columns
new_cols = df['freq,indic_is,unit,ind_type,geo\\TIME_PERIOD'].str.split(",", expand=True)
new_cols.columns = ['freq', 'indic_is', 'unit', 'ind_type', 'geo']

# Drop the original combined column and concatenate the new split columns with remaining data
df = pd.concat([new_cols, df.drop(columns=['freq,indic_is,unit,ind_type,geo\\TIME_PERIOD'])], axis=1)

# Save the processed and cleaned data to CSV file
df.to_csv('../data/estat_isoc_ci_ac_i.csv', index=False)
print(df.head(6))  # Print first 6 rows of processed dataframe

# Print list of all column names
headers = df.columns.tolist()
print(f"Column names: {headers}")

# Get basic statistics about the data
count_total = len(df)
print(f"Total rows: {count_total}")  # Print total number of rows

year_header = [col for col in df.columns if str(col).startswith('20')]
print(f"Number of year columns: {len(year_header)}")

count_totalgeo = len(df['geo'].unique())
print(f"Total unique geo: {count_totalgeo}")  # Print number of unique geographic locations

count_LT = len(df[df['geo'] == 'LT'])
print(f"Total rows of LT: {count_LT}")  # Print number of rows for Lithuania (LT)

print(df.describe())