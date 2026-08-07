import pandas as pd

# Load the dataset
df = pd.read_csv("Lab.csv")

# Display the first 5 rows
print(df.head())
# Dataset dimensions
print("\nDataset shape:")
print(df.shape)

# Column names
print("\nColumn names:")
print(df.columns.tolist())

# Data types
print("\nData types:")
print(df.dtypes)
# ==========================================
# 3. DUPLICATE INSPECTION
# ==========================================

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

print("\nNumber of duplicate customer IDs:")
print(df["customerID"].duplicated().sum())
# ==========================================
# 4. UNIQUE VALUES
# ==========================================

categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].unique())
    # ==========================================
# 5. MISSING VALUE ANALYSIS
# ==========================================

print("\nMissing values:")
missing_values = df.isnull().sum()
print(missing_values)

print("\nTotal missing values in dataset:")
print(missing_values.sum())
# Check for blank/empty values
print("\nBlank values:")
for column in df.columns:
    blank_count = (df[column].astype(str).str.strip() == "").sum()
    if blank_count > 0:
        print(f"{column}: {blank_count}")
        # ==========================================
# 6. TOTAL CHARGES INVESTIGATION
# ==========================================

print("\nTotalCharges data type:")
print(df["TotalCharges"].dtype)

print("\nNumber of blank TotalCharges:")
print((df["TotalCharges"].astype(str).str.strip() == "").sum())

print("\nFirst 20 TotalCharges values:")
print(df["TotalCharges"].head(20))
print("\nCustomers with blank TotalCharges:")
print(
    df[df["TotalCharges"].astype(str).str.strip() == ""]
    [["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Churn"]]
)
# ==========================================
# 7. INVESTIGATE ZERO-TENURE CUSTOMERS
# ==========================================

zero_tenure = df[df["tenure"] == 0]

print("\nNumber of customers with zero tenure:")
print(len(zero_tenure))

print("\nZero-tenure customers:")
print(
    zero_tenure[
        ["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Churn"]
    ]
)
print("\nTotalCharges status for zero-tenure customers:")
print(zero_tenure["TotalCharges"].value_counts(dropna=False))