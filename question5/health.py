import pandas as pd
import matplotlib
import matplotlib.pyplot as plot
import seaborn as sns

file='../heart_disease_uci.csv'

df=pd.read_csv(file)
print("\n\tDataset Information")
df.info()

print("\n\tFirst 5 rows")
print(df.head())

print("\n\tStatistical SUmmary")
print(df.describe())

print("\n\tDataset Shape")
print(df.shape)

print("\n\tChecking for missing values")
print(df.isnull().sum())

#Handling missing values
df.dropna(inplace=True)

print("\n\tChecking for duplicates")
print(df.duplicated().sum())

print("Final Datset Information")
df.info()

print("Dataset is now ready for exploration")
#Binarize the outcome num
df['heart_disease']=df['num'].apply(lambda x:1 if x>0 else 0)
df.drop(columns=['num'],inplace=True)
#Statistical analysis"Correlation calculation
#Correlation measures the linear relationship between numeric variables
#is there a significant correlation between age,trestbps,chol and the lkelyhood of heart disease
corr_matrix=df[['age','trestbps','chol','thalch','oldpeak','heart_disease']].corr()
disease_correlations=corr_matrix['heart_disease'].drop('heart_disease').sort_values(ascending=False)

#Visualization
plot.figure(figsize=(10,6))
sns.barplot(
        x=disease_correlations.values,
        y=disease_correlations.index,
        palette='coolwarm'
        )
plot.title('Correlation with heart disease outcome')
plot.xlabel('Correlation Coefficient r')
plot.ylabel('Indicator variable')
plot.axvline(0,color='black',linestyle='--',linewidth=0.8)
plot.grid(axis='x',linestyle='--',alpha=0.5)
plot.tight_layout()
plot.savefig("Correlation.png")
plot.show()

#Scatter plot for the striongest correlation against age
strongest=disease_correlations.abs().idxmax()

plot.figure(figsize=(12,7))
sns.scatterplot(
        data=df,
        x='age',
        y=strongest,
        hue='heart_disease',
        palette=['skyblue','red'],
        style='heart_disease',
        s=100,
        alpha=0.6
        )
plot.title(f"Scatter plot: Age vs {strongest}")
plot.xlabel('Age')
plot.ylabel(strongest.capitalize())
plot.legend(title='Heart Disease',labels=['No disease(0)','Disease(1)'])
plot.grid(linestyle='--',alpha=0.5)
plot.tight_layout()
plot.savefig('Strongest.png')
plot.show()

print("\n\t\tCorrelation Results-------")
print(disease_correlations)

print(f"The strongest correlation indicator with heart disease is {strongest}")

