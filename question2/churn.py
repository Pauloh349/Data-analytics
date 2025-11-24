import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# --- DATA LOADING ---
file='../Q2 Dataset.csv'
df=pd.read_csv(file)

# --- CLEANING ---

# Clean TotalCharges BEFORE dropna
df['TotalCharges'] = df['TotalCharges'].replace(' ', np.nan)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df['Churn'] = df['Churn'].map({'Yes':1,'No':0})

df.drop('customerID',axis=1,inplace=True)

# --- VISUALIZATION ---
plt.figure(figsize=(6, 4))
sns.countplot(x='Churn', data=df)
plt.title('Churn Distribution (0=No, 1=Yes)')
plt.show()

# --- FEATURE ENGINEERING ---
bins=[0, 12, 24, 48, 72, np.inf]
labels=['0-1 YR','1-2 YRS','2-4 YRS','4-6 YRS','6+ YRS']
df['Tenure_Group'] = pd.cut(df['tenure'], bins=bins, labels=labels)

df.drop('tenure',axis=1,inplace=True)

# --- ENCODING ---
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
# DO NOT add SeniorCitizen – it's numeric already

df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# --- SPLIT ---
X = df_encoded.drop('Churn', axis=1)
y = df_encoded['Churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --- TRAIN ---
model = LogisticRegression(solver='liblinear', max_iter=1000)
model.fit(X_train, y_train)

# --- EVALUATE ---
print(classification_report(y_test, model.predict(X_test)))

# --- FEATURE IMPORTANCE ---
feature_importances = pd.Series(model.coef_[0], index=X.columns).sort_values()

plt.figure(figsize=(10, 8))
sns.barplot(x=feature_importances.tail(10).values,
            y=feature_importances.tail(10).index)
plt.title("Top Positive Features (Churn Risk)")
plt.show()

plt.figure(figsize=(10, 8))
sns.barplot(x=feature_importances.head(10).values,
            y=feature_importances.head(10).index)
plt.title("Top Negative Features (Retention)")
plt.show()
