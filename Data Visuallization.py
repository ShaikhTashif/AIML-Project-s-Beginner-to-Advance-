# I'm Using a Pandas and matplotlib for Python Creating a Project 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")
# Clean data 
df = df.dropna(subset=['type','release_year', 'rating', 'country', 'duration'])

type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['skyblue', 'orange'])
plt.title('Number of Movies and TV Shows on Netflix')
plt.xlabel('Name Type')
plt.ylabel('No')
plt.tight_layout()
plt.savefig('movies_vs_tvshows_vs_.png')
plt.show()

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage Of Content Rating')
plt.tight_layout()
plt.savefig('Netflix_Data_pie.png')
plt.show()

release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values, color='red')
plt.title('Release year VC Number of shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('Release_year_Scatter.png')
plt.show()

country_counts = df['country'].values_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.title('Top 10 countries by number of Shows')
plt.xlabel('Number of shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('Top_Ten_countries.png')
plt.show()

