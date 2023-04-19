import os

import pandas as pd
from sklearn import *

train_path = 'train.csv'
test_path  = 'test.csv'

train_df = pd.read_csv(train_path)

# 将Category进行整数编码
encoder = preprocessing.LabelEncoder()
crime_type_encode = encoder.fit_transform(train_df['Category'])

# 将时间进行one-hot编码
hour = pd.to_datetime(train_df['Dates']).dt.hour
hour = pd.get_dummies(hour)
day = pd.get_dummies(train_df['DayOfWeek'])

# 将所属警区进行one-hot编码
police_district = pd.get_dummies(train_df['PdDistrict'])

train_set = pd.concat([hour, day, police_district], axis = 1)
train_set['Crime type'] = crime_type_encode

print(train_set.head())
