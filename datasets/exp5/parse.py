import pandas as pd 

train_path = 'train.csv'
test_path  = 'test.csv'

train = pd.read_csv(train_path)
test  = pd.read_csv(test_path)

print(train['Class'].value_counts())
print(test['Class'].value_counts())