import pandas as pd
import numpy as np

# Read csv into pandas DataFrame
df = pd.read_csv(r'./data/heart.csv')

# Cleaning up data, drop index 449 where 'RestingBP' < 60
df=df.drop(df.index[449])

# Replacing abnormal 'Cholesterol' values with mean values
df_no_heartdisease = df[df['HeartDisease'] == 0]
df_heartdisease = df[df['HeartDisease'] == 1]
positive_cholesterol_no_heartdisease = df_no_heartdisease[df_no_heartdisease['Cholesterol'] != 0]
mean_positive_cholesterol_no_heartdisease = positive_cholesterol_no_heartdisease['Cholesterol'].mean()
positive_cholesterol_heartdisease = df_heartdisease[df_heartdisease['Cholesterol'] != 0]
mean_positive_cholesterol_heartdisease = positive_cholesterol_heartdisease['Cholesterol'].mean()
zero_cholesterol_no_heartdisease_cond = (df['Cholesterol'] == 0) & (df['HeartDisease'] == 0)
zero_cholesterol_heartdisease_cond = (df['Cholesterol'] == 0) & (df['HeartDisease'] == 1)
df['Cholesterol'] = np.where(zero_cholesterol_no_heartdisease_cond, mean_positive_cholesterol_no_heartdisease, df['Cholesterol'])
df['Cholesterol'] = np.where(zero_cholesterol_heartdisease_cond, mean_positive_cholesterol_heartdisease, df['Cholesterol'])

# Correcting 'Oldpeak' values
df.loc[df['Oldpeak'] < 0, 'Oldpeak'] = df['Oldpeak'] * -1

# Save clean dataset
df.to_csv(r'./data/heart_clean.csv')
