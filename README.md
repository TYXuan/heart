# Heart Disease Prediction

By Tan Yu Xuan

email: yxtan05@gmail.com

## Project Organisation


    ├── run.sh            <- .sh file which preprocesses the raw data and performs predictions.
    |
    ├── README.md          <- The top-level README for users of this project.
    |
    ├── data               <- Where heart.csv should be placed in & processed results are stored in.
    | 
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    |
    ├── eda.ipynb          <- Exploratory data analysis.
    |
    ├── src                <- Source code for use in this project.
    |   ├── __init__.py    <- Makes src a Python module
    |   │   
    |   |── dataprocessing.py <- Script to ingest and process dataset
    |   |
    |   |── modelling.py   <- Script to perform predictions based on processed dataset.
    |   |
    |   └── models         <- Dumps of trained models
    |         ├── randomforest_model.joblib
    |         |
    |         ├── decisiontree_model.joblib
    |         |
    |         └── knn_model.joblib
    |
    └── algorithm_used.txt <- Input the algorithm to be used (random forest / decision tree / knn).
--------

# Instructions

## 1. Setting up the enviroment

### Install the required libraries from your terminal

- In your command shell/terminal locate the directory where requirements.txt is located and type in the following:

      conda create --name heart --file requirements.txt

### Once all packages/libraries are installed activate the installed enviroment

- Key in the following code into your shell:

      conda activate heart

## 2. Placing your data

- Place the data into the `data` folder of this directory

## 3. Running the model

- In your command shell/terminal move to where run.sh is located and key in the following command
    
      ./run.sh
--------

# Engineering Pipeline

1. Import dataset
2. Checking for duplicates & missing values
3. Correcting abnormal data
4. Build additional features 
5. Converting categorical data into booleans and/or dummies
6. Saving processed dataset out as .csv
7. fit model & pickle it out
8. Predict with features & unpickled model
9. Output results in .csv file

# EDA Overview

The EDA contains overview of key findings from the dataset. Choices made in the pipeline are based on those findings, particularly any feature engineerings for modelling. Please keep the details of the EDA in the `.ipynb` which serves as a quick summary.

# Model choice

The following classification models are chosen for this project:
 
  1. Random Forest Classifier
  2. Decision Tree Classifier
  3. K Nearest Neighbors Classifier

  # Model Evaluation

For classification models the baseline was set to an accuracy of 0.5 where the model has a 50:50 chance of a correct prediction.
The goal is for our models to perform better than a coin toss.

In addition, recall where HeartDisease=1 will be looked at as it is the true positives.

It is essential to correctly identify those with heart disease so that they can monitor their condition and seek further help ahead of time.

### Scoring metrics
**ROC AUC scores**

| model               | training set | test set|
|---------------------|--------------|---------|
|KNN (n_neighbors = 6)|    0.77     |   0.72 |
|Decision Tree (min_samples_leaf = 8)|0.89|0.81|
|`Random Forest Classifier`|1|`0.86`|

From the ROC AUC scores we see that the Random Forest Classifier had better scores compared to Decision Tree Classifier and K-Nearest Neighbors Classifier. 

Based on the test set we see that the classifier has a 86% probability of identifying the correct HeartDisease which better than our baseline.

Comparing the scores from the training set and test set, there might be some overfitting has the model performs worse on the unseen data.

### K Nearest Neighbors
#### a. Confusion Matrix
|                | HeartDisease=0 | HeartDisease=1|
|----------------|----------------|---------------|
| HeartDisease=0 |        62      |       20      | 
| HeartDisease=1 |       `31`     |      `71`     |

#### b. Classification Report

|      label     | precision | recall | f1-score|
|----------------|-----------|--------|---------|
| HeartDisease=0 |  0.67     |  0.76  |   0.71  |
| HeartDisease=1 |  0.78     | `0.70` |   0.74  |

### Decision Tree Classifier
#### a. Confusion Matrix
|                | HeartDisease=0 | HeartDisease=1 |
|----------------|----------------|----------------|
| HeartDisease=0 |        67      |       15       | 
| HeartDisease=1 |       `20`     |      `82`      |

#### b. Classification Report

|      label     | precision | recall | f1-score|
|----------------|-----------|--------|---------|
| HeartDisease=0 |  0.77     |  0.82  |   0.79  |
| HeartDisease=1 |  0.85     | `0.80` |   0.82  |

### Random Forest Classifier
#### a. Confusion Matrix
|                | HeartDisease=0 | HeartDisease=1 |
|----------------|----------------|----------------|
| HeartDisease=0 |       70       |       12       | 
| HeartDisease=1 |      `14`      |      `88`      |

#### b. Classification Report

|      label     | precision | recall | f1-score|
|----------------|-----------|--------|---------|
| HeartDisease=0 |  0.83     |  0.85  |   0.84  |
| HeartDisease=1 |  0.88     | `0.86` |   0.87  |

Based on the classification report, Random Forest Classifier has the highest recall value of 0.86.
It outperforms the other two models - K Nearest Neighbors Classifier and Decision Tree Classifier.

# Conclusion
Comparing the types of models, Random Forest Classifier is definitely the most accurate in predicting those with heart disease (HeartDisease=1).
