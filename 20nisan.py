import seaborn as sns
planets = sns.load_dataset('all')
df = planets.copy()
df.head()