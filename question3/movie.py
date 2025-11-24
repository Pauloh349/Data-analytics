import pandas as pd
import matplotlib
import matplotlib.pyplot as plot
import seaborn as sns

file='../MovieDB.xlsx'
df=pd.read_excel(file)
print("\n\t\tDataset Information")
df.info()

print("\n\t\tDataset shape")
print(df.shape)

print("\n\t\tStatistical Summary of the data")
print(df.describe())

print("\n\t\tFirst 5 lines of the data")
print(df.head())

print("\n\t\tCheck for missing values in all columns")
print(df.isnull().sum())
#If any drop all missing values
df.dropna(inplace=True)

print("\n\t\tCheck for duplicates in the data")
print(df.duplicated().sum())
#If any duplicates drop them
df.drop_duplicates(inplace=True)

#Clean the movie name to make them all upper case for uniformity
df['Movie Name']=df['Movie Name'].str.upper().str.strip()
print(df['Movie Name'])
#Lets standardize the data
print(df['Movie Name'].unique())
print("Now the data is clean for exploration")

#Lets now work on the data by aggregating the movie by movie name and checking ratings
movie_ratings=df.groupby('Movie Name')[['Rating']].mean().reset_index()
highest_rated=movie_ratings.sort_values(by='Rating',ascending=False).head(10)
print("\n\t\t\tTop 10 highest rated movies are")
print(highest_rated)
#Let's visualize average rating per movie
y_positions=range(len(highest_rated))

plot.barh(y_positions,highest_rated['Rating'])
plot.yticks(y_positions,highest_rated['Movie Name'])
plot.title('Top 10 Highest Rated Movies')
plot.xlabel('Average Rating')
plot.ylabel('Movie Name')
plot.gca().invert_yaxis()
plot.tight_layout()
plot.savefig('Movies.png')
plot.show()
#Let's find patterns based on release years
df['Date']=pd.to_datetime(df['Date'])
df['year']=df['Date'].dt.year
movie_by_years=df.groupby('Movie Name')['year']
print(movie_by_years.max())

corr_matrix=df[['Rating','DirectorsRating','WritersRating']].corr()
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm')
plot.title("Correlation between AudienceRating,Directors and Writers")
plot.savefig('Corr.png')
plot.show()
