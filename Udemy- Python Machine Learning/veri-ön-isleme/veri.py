import seaborn as sns
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include=['float64','int64'])
df = df.dropna()
#print(df.head())

df_table = df["table"]
print(df_table.head)


Q1 = df_table.quantile(0.25)
Q3 = df_table.quantile(0.75)
IQR = Q3 - Q1


altSınır = Q1 - 1.5*IQR
üstSınır = Q3 + 1.5*IQR



print((df_table < altSınır) | (df_table > üstSınır))

aykiri_truFalse = (df_table < altSınır)
print(aykiri_truFalse.head())



import pandas as pd
df_table = pd.DataFrame(df_table)
df_table.shape
temiz_df = df_table[~((df_table < (altSınır)) | (df_table > (üstSınır))).any(axis=1)]
print(temiz_df.shape)