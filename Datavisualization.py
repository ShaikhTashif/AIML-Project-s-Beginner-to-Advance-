import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/content/sample_data/california_housing_train.csv')
sns.set(style = 'whitegrid')

# Corrected: Use an existing column from the dataframe, e.g., 'median_house_value'
sns.histplot(df['median_house_value'], kde = True, bins =10)
plt.title("Distribution of Median House Value") # Updated title to match the column
print("DataFrame 'df' loaded successfully:")
display(df.head(20)) # Display first 5 rows by default
I'm exploring the Data in inside to predict and explore for diagram form 
