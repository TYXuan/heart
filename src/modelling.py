from joblib import load
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

print('Importing dataset from ./data/...')

df = pd.read_csv('./data/heart_clean.csv', index_col=[0])

print('Preprocessing dataset for predictions...')

# Converting features to booleans
sex_dict = {'F':0, 'M':1}
df['Sex'] = df['Sex'].replace(sex_dict)

exercise_dict = {'N':0, 'Y':1}
df['ExerciseAngina'] = df['ExerciseAngina'].replace(exercise_dict)

chestpain_dict = {'TA':3, 'ATA':2, 'NAP':1, 'ASY':0}
df['ChestPainType'] = df['ChestPainType'].replace(chestpain_dict)

ecg_dict = {'Normal':0, 'ST':1, 'LVH':2}
df['RestingECG'] = df['RestingECG'].replace(ecg_dict)

slope_dict = {'Up':0, 'Flat':1, 'Down':2}
df['ST_Slope'] = df['ST_Slope'].replace(slope_dict)

# Import heart.csv dataset
df_heart = pd.read_csv('./data/heart.csv', index_col=[0])
df_heart.reset_index(drop=True, inplace = True)

X = df.drop('HeartDisease', axis=1).values

model = input('Which algorithm is to be used? (random forest / decision tree / knn)')

if model.lower() == 'decision tree':
    print(f'Loading {model.lower()} model...')
    dt = load('./src/models/decisiontree_model.joblib')
    y_pred = dt.predict(X)
    y_pred_df = pd.DataFrame(data=y_pred, columns=["Predicted_HeartDisease"])
    results = df_heart.join(y_pred_df)
    results.to_csv(r'./data/decision_tree_results.csv')
    print('Results saved into csv format!')

elif model.lower() == 'knn':
    print(f'Loading {model.lower()} model...')
    knn = load('./src/models/knn_model.joblib')
    y_pred = knn.predict(X)
    y_pred_df = pd.DataFrame(data=y_pred, columns=["Predicted_HeartDisease"])
    results = df_heart.join(y_pred_df)
    results.to_csv(r'./data/knn_results.csv')
    print('Results saved into csv format!')

elif model.lower() == 'random forest':
    print(f'Loading {model.lower()} model...')
    rf = load('./src/models/randomforest_model.joblib')
    y_pred = rf.predict(X)
    y_pred_df = pd.DataFrame(data=y_pred, columns=["Predicted_HeartDisease"])
    results = df_heart.join(y_pred_df)
    results.to_csv(r'./data/rf_results.csv')
    print('Results saved into csv format!')

else:
    print('Please select a valid option. (random forest / decision tree / knn)')
