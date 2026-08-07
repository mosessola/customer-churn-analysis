import pandas as pd

# ==========================================
# 1. LOAD RAW DATA
# ==========================================

df = pd.read_csv("Lab.csv")

print("Raw dataset loaded successfully.")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")


# ==========================================
# 2. CREATE CLEAN COPY
# ==========================================

df_clean = df.copy()


# ==========================================
# 3. CLEAN TOTALCHARGES
# ==========================================

df_clean["TotalCharges"] = pd.to_numeric(
    df_clean["TotalCharges"],
    errors="coerce"
)


# ==========================================
# 4. VALIDATE CLEANING
# ==========================================

print("\nTotalCharges data type:")
print(df_clean["TotalCharges"].dtype)

print("\nMissing TotalCharges values:")
print(df_clean["TotalCharges"].isnull().sum())


# ==========================================
# 5. CHECK DUPLICATES
# ==========================================

print("\nDuplicate rows:")
print(df_clean.duplicated().sum())

print("\nDuplicate customer IDs:")
print(df_clean["customerID"].duplicated().sum())


# ==========================================
# 6. SAVE CLEAN DATASET
# ==========================================

df_clean.to_csv("Lab_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully as Lab_cleaned.csv")