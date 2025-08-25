import pandas as pd

# =================== HOMEWORK 2 ===================

# CSV faylni o'qish
df = pd.read_csv("task\\stackoverflow_qa.csv")

# creationdate ustunini datetime ga o'zgartirish
df['creationdate'] = pd.to_datetime(df['creationdate'])

# --task-1
# Find all questions that were created before 2014
print("--task-1")
print(df[df['creationdate'] < '2014-01-01'])

# --task-2
# Find all questions with a score more than 50
print("--task-2")
print(df[df['score'] > 50])

# --task-3
# Find all questions with a score between 50 and 100
print("--task-3")
print(df[(df['score'] >= 50) & (df['score'] <= 100)])

# --task-4
# Find all questions answered by Scott Boston
print("--task-4")
print(df[df['ans_name'] == 'Scott Boston'])

# --task-5
# Find all questions answered by the following 5 users
print("--task-5")
users = ['Unutbu', 'Scott Boston', 'Mike Pennington', 'Demitri', 'doug']
print(df[df['ans_name'].isin(users)])

# --task-6
# Find all questions created between March 2014 and October 2014, answered by Unutbu and have score < 5
print("--task-6")
print(df[(df['creationdate'] >= '2014-03-01') &
         (df['creationdate'] <= '2014-10-31') &
         (df['ans_name'] == 'Unutbu') &
         (df['score'] < 5)])

# --task-7
# Find all questions with score between 5 and 10 OR viewcount > 10,000
print("--task-7")
print(df[((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)])


# --task-8
# Find all questions not answered by Scott Boston
print("--task-8")
print(df[df['ans_name'] != 'Scott Boston'])


# =================== HOMEWORK 3 ===================

# Titanic CSV faylni o'qish
titanic_df = pd.read_csv("task\\titanic.csv")



# --task-9
# Select Female Passengers in Class 1 with Ages between 20 and 30
print("--task-9")
print(titanic_df[(titanic_df['Sex'] == 'female') &
                 (titanic_df['Pclass'] == 1) &
                 (titanic_df['Age'].between(20, 30))])



# --task-10
# Filter Passengers Who Paid More than $100
print("--task-10")
print(titanic_df[titanic_df['Fare'] > 100])



# --task-11
# Select Passengers Who Survived and Were Alone
print("--task-11")
print(titanic_df[(titanic_df['Survived'] == 1) &
                 (titanic_df['SibSp'] == 0) &
                 (titanic_df['Parch'] == 0)])



# --task-12
# Filter Passengers Embarked from 'C' and Paid More Than $50
print("--task-12")
print(titanic_df[(titanic_df['Embarked'] == 'C') & (titanic_df['Fare'] > 50)])



# --task-13
# Select Passengers with Siblings or Spouses AND Parents or Children
print("--task-13")
print(titanic_df[(titanic_df['SibSp'] > 0) & (titanic_df['Parch'] > 0)])



# --task-14
# Filter Passengers Aged 15 or Younger Who Didn't Survive
print("--task-14")
print(titanic_df[(titanic_df['Age'] <= 15) & (titanic_df['Survived'] == 0)])



# --task-15
# Select Passengers with Cabins and Fare Greater Than $200
print("--task-15")
print(titanic_df[(titanic_df['Cabin'].notna()) & (titanic_df['Fare'] > 200)])



# --task-16
# Filter Passengers with Odd-Numbered Passenger IDs
print("--task-16")
print(titanic_df[titanic_df['PassengerId'] % 2 == 1])



# --task-17
# Select Passengers with Unique Ticket Numbers
print("--task-17")
print(titanic_df[titanic_df['Ticket'].map(titanic_df['Ticket'].value_counts()) == 1])



# --task-18
# Filter Passengers with 'Miss' in Their Name and Were in Class 1
print("--task-18")
print(titanic_df[(titanic_df['Name'].str.contains('Miss')) &
                 (titanic_df['Pclass'] == 1)])
