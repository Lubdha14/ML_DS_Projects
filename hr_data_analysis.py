# -*- coding: utf-8 -*-
"""HR Data Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vO-ISMjnG1OEKI65gBTYR_JTrLhjpEaF
"""

import numpy as np
import pandas as pd
import seaborn as sns
import os

# Reading the dataset
df = pd.read_csv("HR Data.csv")

df

"""###### **Data Cleansing - Removing Unnecessary Columns**"""

columns_remove = ['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours']
df = df.drop(columns=columns_remove)

df

"""###### **Giving the columns new names**



"""

new_column_names = {
    'Attrition': 'Left',
    'BusinessTravel': 'Business_Travel',
    'DailyRate': 'Daily_Rate',
    'Department': 'Dept',
    'DistanceFromHome': 'Distance_From_Home',
    'Education': 'Education_Level',
    'EducationField': 'Education_Field',
    'EnvironmentSatisfaction': 'Environment_Satisfaction',
    'JobInvolvement': 'Job_Involvement',
    'JobLevel': 'Job_Level',
    'JobRole': 'Job_Role',
    'JobSatisfaction': 'Job_Satisfaction',
    'MaritalStatus': 'Marital_Status',
    'MonthlyIncome': 'Monthly_Income',
    'MonthlyRate': 'Monthly_Rate',
    'NumCompaniesWorked': 'Num_Companies_Worked',
    'OverTime': 'Over_Time',
    'PercentSalaryHike': 'Percent_Salary_Hike',
    'PerformanceRating': 'Performance_Rating',
    'RelationshipSatisfaction': 'Relationship_Satisfaction',
    'StockOptionLevel': 'Stock_Option_Level',
    'TotalWorkingYears': 'Total_Working_Years',
    'TrainingTimesLastYear': 'Training_Times_Last_Year',
    'WorkLifeBalance': 'Work_Life_Balance',
    'YearsAtCompany': 'Years_At_Company',
    'YearsInCurrentRole': 'Years_In_Current_Role',
    'YearsSinceLastPromotion': 'Years_Since_Last_Promotion',
    'YearsWithCurrManager': 'Years_With_Curr_Manager'
}

df = df.rename(columns=new_column_names)
df

"""###### **Eliminating redundant entries**

"""

# Identifying duplicate rows
duplicates = df[df.duplicated()]

# Display the duplicate rows
duplicates

# Removing duplicate rows
df = df.drop_duplicates()

"""
###### **Sanitizing specific columns**"""

# Ensuring consistent formatting for categorical variables
df['Business_Travel'] = df['Business_Travel'].str.replace('_', ' ')
df['Dept'] = df['Dept'].str.replace('&', 'and')

# Title-casing the 'Education_Field' column
df['Education_Field'] = df['Education_Field'].str.title()

# Ensuring numerical data is valid (no negative values)
numerical_columns = ['Years_At_Company', 'Total_Working_Years', 'Years_In_Current_Role', 'Years_Since_Last_Promotion', 'Years_With_Curr_Manager']
for col in numerical_columns:
    df = df[df[col] >= 0]

print(df.head())

"""###### **Eliminate the dataset's NaN values**

"""

df = df.dropna()

"""###### **Some more changes**

"""

# Standardizing format
categorical_columns = ['Business_Travel', 'Dept', 'Education_Field', 'Gender', 'Job_Role', 'Marital_Status', 'Over_Time']
for col in categorical_columns:
    df[col] = df[col].str.strip().str.lower()

# Define realistic ranges and ensure values are non-negative
numerical_columns = ['Years_At_Company', 'Total_Working_Years', 'Years_In_Current_Role', 'Years_Since_Last_Promotion', 'Years_With_Curr_Manager', 'Daily_Rate', 'HourlyRate', 'Monthly_Income', 'Monthly_Rate', 'Percent_Salary_Hike']
for col in numerical_columns:
    df = df[df[col] >= 0]

# Converting categorical columns to the 'category' data type
for col in categorical_columns:
    df[col] = df[col].astype('category')

# Displaying Data Types
print(df.dtypes)