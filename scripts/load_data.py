import pandas as pd

# Print first 3 lines of the TSV file
with open("../data/estat_isoc_ci_ac_i$defaultview_filtered.tsv") as f:
    for i in range(3):
        print(f.readline())

# Read TSV file into dataframe
df = pd.read_csv('../data/estat_isoc_ci_ac_i$defaultview_filtered.tsv', sep='\t')

# Split the first column by ',' into separate columns
new_cols = df['freq,indic_is,unit,ind_type,geo\\TIME_PERIOD'].str.split(",", expand=True)
new_cols.columns = ['freq', 'indic_is', 'unit', 'ind_type', 'geo']

# Drop old combined column and concat with new columns
df = pd.concat([new_cols, df.drop(columns=['freq,indic_is,unit,ind_type,geo\\TIME_PERIOD'])], axis=1)

# Save processed data to CSV
df.to_csv('../data/estat_isoc_ci_ac_i.csv', index=False)
print(df.head(6))

for index, row in df.iterrows():
    print(index, row['geo'][:3])
    if index >= 3:
        break
