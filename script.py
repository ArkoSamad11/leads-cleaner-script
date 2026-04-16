import pandas as pd

# load raw data where TK represents downloaded csv path
df = pd.read_csv('TK')

# identifies individuals with only verified emails, no exceptions
new_df = df[df['Email Status'] == 'Verified']

# strips csv down to its essentials information
new_df_subset = new_df[['First Name', 'Last Name', 'Title', 'Company Name', 'Email']]

# remove rows where email column is N/A or blank
new_df_subset = new_df_subset[new_df_subset['Email'].notna() & (new_df_subset['Email'].str.strip() != '')]

# export to csv where TK represents name of file before .csv extension
# Mac
new_df_subset.to_csv('/Users/arkosamad/Downloads/TK', index=False)
# Windows 
new_df_subset.to_csv(r'C:\Users\arkosamad\Downloads\TK', index=False)