**Project Summary**
- **Scope**: Concise review of `question1` .. `question5` folders: data files, scripts, cleaning steps, analyses, outputs, and recommended next steps.
- **Location**: Report saved at `QUESTION_SUMMARY_REPORT.md` in the workspace root.

**Question 1**
- **Files**: `question1/sales.py`, `question1/cleanSales.csv`, `question1/cleanSales_final.csv` (created by script)
- **Dataset**: Cleaned sales data in `cleanSales.csv` (script writes `cleanSales_final.csv`).
- **Script purpose**: Loads cleaned sales data, inspects and further cleans it, standardizes categories, converts date columns, drops missing values and duplicates, saves cleaned file, and produces a Top-10-products-by-sales bar chart.
- **Key steps**:
  - `pd.read_csv('./cleanSales.csv')`
  - Drop NaNs and duplicates, standardize `Region`, `Category`, `Country` values.
  - Convert `Order Date` and `Ship Date` to datetimes.
  - Save cleaned dataset to `cleanSales_final.csv`.
  - Plot top 10 products by total sales using `seaborn`.
- **Outputs**: `cleanSales_final.csv` and a displayed bar chart (plot shown via `plt.show()`).
- **Notes / Recommendations**: Consider adding argument parsing to point to raw vs cleaned CSVs and save plots to `outputs/` folder rather than directly in the working directory. Add unit tests for date parsing edge cases.

**Question 2**
- **Files**: `question2/churn.py`, dataset referenced at `../Q2 Dataset.csv` (workspace root `Q2-Dataset.csv`)
- **Dataset**: Telecom churn dataset (CSV). Script expects `TotalCharges` may contain blanks and coerces to numeric.
- **Script purpose**: Clean data, encode categorical variables, build a logistic regression model for customer churn, and visualize feature importances and churn distribution.
- **Key steps**:
  - Replace blank `TotalCharges` with NaN and coerce to numeric; drop NaNs and duplicates.
  - Map `Churn` to binary, drop `customerID`.
  - Create tenure bins and drop original `tenure`.
  - One-hot encode categorical columns (`pd.get_dummies`, `drop_first=True`).
  - Train/Test split (stratified), train `LogisticRegression`, print classification report.
  - Plot top positive/negative features by coefficient magnitude.
- **Outputs**: Console classification report, countplot of churn, two barplots of feature coefficients.
- **Notes / Recommendations**: Consider scaling numeric features or using regularization tuning. Keep a reproducible `requirements.txt` and a model serialization step (`joblib.dump`) for later reuse.

**Question 3**
- **Files**: `question3/movie.py`, dataset referenced at `../MovieDB.xlsx` (Excel)
- **Dataset**: MovieDB Excel file; script drops NA and duplicates and standardizes movie names.
- **Script purpose**: Basic EDA on movie ratings, compute average rating per movie, plot top-10 highest rated movies, analyze release years and correlations among rating columns.
- **Key steps**:
  - Read Excel file, `df.dropna()` and `df.drop_duplicates()`.
  - Upper-case and strip `Movie Name` for consistency.
  - Group by `Movie Name` to compute mean `Rating` and select top-10.
  - Save `Movies.png` and `Corr.png` for visualization.
- **Outputs**: `Movies.png` (top-10 barh plot), `Corr.png` (heatmap), console prints.
- **Notes / Recommendations**: Preserve original movie name column when standardizing (create `movie_name_clean`) to avoid losing data. Add checks for Excel sheet names and column presence to make script robust.

**Question 4**
- **Files**: `question4/crime.py`, dataset referenced at `../crimes.csv` (workspace root `crimes.csv`)
- **Dataset**: Crime incidents CSV (fields include `LOCATION`, `AREA NAME`, `Crm Cd Desc`, `DATE OCC`, `Date Rptd`).
- **Script purpose**: Clean and standardize crime records, produce area-level counts, a top-15 areas bar plot, and monthly time-series of incidents.
- **Key steps**:
  - Drop NA, upper-case and strip `LOCATION`/`AREA NAME`, lowercase `Crm Cd Desc`.
  - Convert `DATE OCC` and `Date Rptd` to datetime, aggregate by `AREA NAME` and by month.
  - Save `CrimeArea.png` and `Time.png` plots.
- **Outputs**: `CrimeArea.png`, `Time.png`, and console prints of aggregates.
- **Notes / Recommendations**: Consider creating a small geographic map (folium) if coordinates available. Store cleaned dataset (e.g., `crimes_clean.csv`) for repeatable EDA.

**Question 5**
- **Files**: `question5/health.py`, dataset referenced at `../heart_disease_uci.csv` (workspace root `heart_disease_uci.csv`)
- **Dataset**: UCI Heart Disease dataset (CSV). Script computes a binary `heart_disease` target from `num`.
- **Script purpose**: Clean dataset, drop NA, create `heart_disease` (binary), compute correlations with outcome, plot correlations and scatter plots for the strongest correlate.
- **Key steps**:
  - `df.dropna()`, binarize `num` into `heart_disease`.
  - Compute correlation matrix for numeric features vs `heart_disease`.
  - Save `Correlation.png` and `Strongest.png` plots.
- **Outputs**: `Correlation.png`, `Strongest.png`, console summary of correlation values and strongest indicator.
- **Notes / Recommendations**: Add a train/test modeling step (logistic regression or tree-based) to quantify predictive power. Consider stratified cross-validation and class-balance checks.

**Common observations & recommendations**
- **Dependencies**: All scripts use `pandas`, `matplotlib`, `seaborn`. `question2/churn.py` also uses `scikit-learn` and `numpy`. Consider adding a `requirements.txt` listing pinned versions:

  - pandas
  - matplotlib
  - seaborn
  - numpy
  - scikit-learn (for question2)

- **Reproducibility**: Add a top-level `requirements.txt` and a `README.md` with run instructions. Scripts should save outputs (plots, cleaned CSVs) under an `outputs/` folder.
- **Robustness**: Add basic input validation (check file existence and required columns) and argument parsing (`argparse`) so scripts can be run from different working directories.
- **Modeling**: For `question2` and `question5`, add model serialization (e.g., `joblib`) and an evaluation notebook to track experiments.

**How to run (quick)**
- From the workspace root (`C:\Users\Paul Muiruri\Downloads\Data Analytics`), run each question script from its folder. Example (PowerShell):

```powershell
cd .\question1
python sales.py

cd ..\question2
python churn.py
```

- Recommended: create and install a virtual environment and install requirements:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Files created**
- `QUESTION_SUMMARY_REPORT.md` (this file)
- `question1/cleanSales_final.csv` (created by `sales.py` when run)
- Plot files created by scripts: `Movies.png`, `Corr.png`, `CrimeArea.png`, `Time.png`, `Correlation.png`, `Strongest.png` (in respective folders or working dir)

**Next suggested steps**
- Add `requirements.txt` and a short `README.md` with per-question run instructions.
- Add small CLI wrappers (or notebook examples) that save outputs to `outputs/` and support `--save-plots` and `--save-cleaned-data` flags.

---
Report generated programmatically by code inspection on current workspace.
