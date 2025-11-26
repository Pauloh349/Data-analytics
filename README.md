---

# **Data Analytics Project – Summary of Question 1 to Question 5**

This repository contains five independent data analysis tasks, each stored in its own folder (`question1` … `question5`).
The work includes data cleaning, exploratory analysis, simple modeling, and visualization.

A full project summary is also saved in the root as **`QUESTION_SUMMARY_REPORT.md`**.

---

## **📁 Project Structure**

```
project-root/
│
├── question1/
│   ├── sales.py
│   ├── cleanSales.csv
│   └── cleanSales_final.csv
│
├── question2/
│   └── churn.py
│
├── question3/
│   └── movie.py
│
├── question4/
│   └── crime.py
│
├── question5/
│   └── health.py
│
├── Q2-Dataset.csv
├── crimes.csv
├── MovieDB.xlsx
├── heart_disease_uci.csv
└── QUESTION_SUMMARY_REPORT.md
```

---

# **1. Question 1 – Sales Data Cleaning & Visualization**

**Files**: `sales.py`, `cleanSales.csv`, `cleanSales_final.csv`
**Goal**: Clean the sales dataset and visualize the top-selling products.

### **What the script does**

* Loads the cleaned sales file.
* Standardizes region, country, and category names.
* Converts `Order Date` and `Ship Date` into proper datetime formats.
* Removes missing entries and duplicates.
* Saves a fully cleaned dataset (`cleanSales_final.csv`).
* Produces a bar chart showing the top 10 products by total sales.

### **Outputs**

* `cleanSales_final.csv`
* Top-10 products bar chart (displayed via `plt.show()`)

---

# **2. Question 2 – Customer Churn Prediction**

**Files**: `churn.py`, `Q2-Dataset.csv`
**Goal**: Clean telecom churn data and build a logistic regression model.

### **What the script does**

* Cleans the `TotalCharges` column and converts it to numeric.
* Drops missing values and duplicates.
* Converts `Churn` into binary labels.
* Removes non-useful columns like `customerID`.
* Bins `tenure` and one-hot encodes categorical features.
* Splits data (train/test), trains logistic regression, and prints a classification report.
* Plots churn distribution and key model coefficients.

### **Outputs**

* Classification report in console
* Churn countplot
* Barplots for top positive and negative feature coefficients

### **Recommendations**

* Add scaling for numeric features
* Tune model regularization
* Save the trained model using `joblib.dump()`

---

# **3. Question 3 – Movie Ratings Analysis**

**Files**: `movie.py`, `MovieDB.xlsx`
**Goal**: Perform EDA on movie ratings and identify top-rated titles.

### **What the script does**

* Reads the Excel file and cleans missing/duplicate rows.
* Standardizes movie names (uppercase + stripped spaces).
* Computes mean ratings per movie.
* Creates plots for the top 10 movies and a correlation heatmap.

### **Outputs**

* `Movies.png` (top-10 highest-rated movies)
* `Corr.png` (ratings correlation heatmap)

### **Suggestions**

* Keep original movie names in a separate column.
* Add checks for sheet names and required columns.

---

# **4. Question 4 – Crime Data Cleaning & Analysis**

**Files**: `crime.py`, `crimes.csv`
**Goal**: Clean crime incident data and analyze crime patterns.

### **What the script does**

* Cleans and standardizes text fields (`LOCATION`, `AREA NAME`, `Crm Cd Desc`).
* Converts occurrence and reporting dates to datetime.
* Aggregates crimes by area and by month.
* Produces a bar chart for top 15 crime-prone areas.
* Creates a time-series chart showing monthly crime trends.

### **Outputs**

* `CrimeArea.png`
* `Time.png`

### **Suggestions**

* If coordinates exist, create a simple crime location map using **folium**.
* Save a cleaned dataset (`crimes_clean.csv`) for reusability.

---

# **5. Question 5 – Heart Disease Analysis**

**Files**: `health.py`, `heart_disease_uci.csv`
**Goal**: Explore relationships between heart disease indicators and the outcome.

### **What the script does**

* Cleans dataset and drops missing values.
* Converts `num` into a binary `heart_disease` column.
* Computes correlations between features and the target.
* Saves a heatmap and a scatter plot of the strongest predictor.

### **Outputs**

* `Correlation.png`
* `Strongest.png`
* Console summary of correlation values

### **Recommendations**

* Add a modeling section (e.g., logistic regression, decision tree).
* Use cross-validation and check class balance.

---

# **📌 General Observations & Best Practices**

### **Dependencies**

The project mainly uses:

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn (Question 2)

Add these to a **requirements.txt** to improve reproducibility.

### **Reproducibility**

Consider adding:

* A top-level `README.md` (this file)
* An `outputs/` folder for all plots and cleaned files
* Clear run instructions for each script
* Optional Jupyter notebooks for extended analysis

### **Input Validation**

You can improve robustness by checking:

* Whether required files exist
* Whether columns are present
* Whether date parsing succeeds

---

# **🚀 Running the Scripts**

From the project root:

```powershell
cd .\question1
python sales.py

cd ..\question2
python churn.py
```

### **Using a virtual environment**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

# **📄 Files Created by Scripts**

* `cleanSales_final.csv`
* `Movies.png`
* `Corr.png`
* `CrimeArea.png`
* `Time.png`
* `Correlation.png`
* `Strongest.png`

---
