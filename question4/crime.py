import pandas as pd
import matplotlib
import matplotlib.pyplot as plot
import seaborn as sns

file='../crimes.csv'

df=pd.read_csv(file)
print("\n\tDataset Information")
df.info()

print("\n\tDataset Shape")
print(df.shape)

print("\n\tDataset First 5 rows")
print(df.head())

print("\n\tDataset Statistical Summary")
print(df.describe())

print("\n\tChecking for missing values")
print(df.isnull().sum())

print("\n\tChecking for duplicates")
print(df.duplicated().sum())

#Dealing with missing values
df.dropna(inplace=True)

#Standardizng importnat columns AREA NAME,LOCATION,Date Rptd, DATE OCC,,Crime Cd Desc
df['LOCATION']=df['LOCATION'].str.strip().str.upper()
df['AREA NAME']=df['AREA NAME'].str.strip().str.upper()
df['Crm Cd Desc']=df['Crm Cd Desc'].str.strip().str.lower()
df['DATE OCC']=pd.to_datetime(df['DATE OCC'])
df['Date Rptd']=pd.to_datetime(df['Date Rptd'])
print("Confirming the dataset again")
df.info()
print("Dataset is now clean and ready for EDA")
#Analyzing based on geopraphical distibution
#Aggregate by area for an object use .size() then sort the values
crime_counts=df.groupby('AREA NAME').size().sort_values(ascending=False)
print(crime_counts)
#Aggregate the crimes by area name and count incidents
area_counts=df['AREA NAME'].value_counts()
top_15=area_counts.sort_values(ascending=False).head(15)
plot.figure(figsize=(12,8))
sns.barplot(
        x=top_15.values,
        y=top_15.index,
        palette='viridis'
        )
plot.title("Top 15 LA areas by Total Crime Incidents",fontsize=16)
plot.xlabel('Total Incidents',fontsize=12)
plot.ylabel('Area Name',fontsize=12)
plot.grid(axis='x',linestyle='--',alpha=0.7)
plot.tight_layout()
plot.savefig('CrimeArea.png')
plot.show()
#Time Series Analysis
monthly_crimes=df['DATE OCC'].dt.to_period('M').value_counts().sort_index()
print(monthly_crimes)
monthly_crimes.index=monthly_crimes.index.to_timestamp()
plot.figure(figsize=(14,6))
plot.plot(
        monthly_crimes.index,
        monthly_crimes.values,
        marker='o',
        linestyle='--',
        color='r',
        alpha=0.7
        )
plot.title("Monthly Crime Incidents Over Time")
plot.xlabel('Date(Year-Month)')
plot.ylabel('Total Incidents')
plot.grid(axis='y',linestyle='--',alpha=0.7)
plot.xticks(rotation=45)
plot.tight_layout()
plot.savefig('Time.png')
plot.show()
