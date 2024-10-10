import pandas as pd

# Load dataset
data = pd.read_csv('data/Dataset-FRT-Discipline-behavior.csv')

# Descriptive statistics
print("Descriptive Statistics:")
print(data.describe())

# Gender distribution
gender_counts = data['Gender'].value_counts()
print("\nGender Distribution:")
print(gender_counts)

# School location distribution
location_counts = data['School Location'].value_counts()
print("\nSchool Location Distribution:")
print(location_counts)
