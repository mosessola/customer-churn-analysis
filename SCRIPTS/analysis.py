import pandas as pd

# ==========================================
# 1. LOAD CLEANED DATASET
# ==========================================

df = pd.read_csv("Lab_cleaned.csv")

print("Cleaned dataset loaded successfully.")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")


# ==========================================
# 2. CUSTOMER OVERVIEW
# ==========================================

total_customers = df["customerID"].nunique()

churned_customers = (df["Churn"] == "Yes").sum()

retained_customers = (df["Churn"] == "No").sum()

churn_rate = (churned_customers / total_customers) * 100

retention_rate = (retained_customers / total_customers) * 100


print("\n========== CUSTOMER OVERVIEW ==========")

print(f"Total customers: {total_customers:,}")
print(f"Churned customers: {churned_customers:,}")
print(f"Retained customers: {retained_customers:,}")
print(f"Churn rate: {churn_rate:.2f}%")
print(f"Retention rate: {retention_rate:.2f}%")


# ==========================================
# 3. TENURE
# ==========================================

print("\n========== TENURE ==========")

print(f"Average tenure: {df['tenure'].mean():.2f} months")
print(f"Median tenure: {df['tenure'].median():.2f} months")
print(f"Minimum tenure: {df['tenure'].min()} months")
print(f"Maximum tenure: {df['tenure'].max()} months")


# ==========================================
# 4. MONTHLY CHARGES
# ==========================================

print("\n========== MONTHLY CHARGES ==========")

print(f"Average monthly charge: ${df['MonthlyCharges'].mean():.2f}")
print(f"Median monthly charge: ${df['MonthlyCharges'].median():.2f}")
print(f"Minimum monthly charge: ${df['MonthlyCharges'].min():.2f}")
print(f"Maximum monthly charge: ${df['MonthlyCharges'].max():.2f}")


# ==========================================
# 5. TOTAL CHARGES
# ==========================================

print("\n========== TOTAL CHARGES ==========")

print(f"Average total charges: ${df['TotalCharges'].mean():.2f}")
print(f"Median total charges: ${df['TotalCharges'].median():.2f}")
print(f"Minimum total charges: ${df['TotalCharges'].min():.2f}")
print(f"Maximum total charges: ${df['TotalCharges'].max():.2f}")
# ==========================================
# 6. CHURN RATE BY SEGMENT
# ==========================================

def churn_by_segment(column):
    result = (
        df.groupby(column)["Churn"]
        .agg(
            total_customers="count",
            churned_customers=lambda x: (x == "Yes").sum()
        )
    )

    result["churn_rate"] = (
        result["churned_customers"] /
        result["total_customers"] * 100
    )

    return result.sort_values("churn_rate", ascending=False)


# ==========================================
# GENDER
# ==========================================

print("\n========== CHURN BY GENDER ==========")
print(churn_by_segment("gender"))


# ==========================================
# SENIOR CITIZEN
# ==========================================

print("\n========== CHURN BY SENIOR CITIZEN ==========")
print(churn_by_segment("SeniorCitizen"))


# ==========================================
# PARTNER
# ==========================================

print("\n========== CHURN BY PARTNER ==========")
print(churn_by_segment("Partner"))


# ==========================================
# DEPENDENTS
# ==========================================

print("\n========== CHURN BY DEPENDENTS ==========")
print(churn_by_segment("Dependents"))
# ==========================================
# 7. CHURN BY CONTRACT TYPE
# ==========================================

print("\n========== CHURN BY CONTRACT TYPE ==========")
print(churn_by_segment("Contract"))
# ==========================================
# 8. TENURE GROUPS
# ==========================================

df["tenure_group"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=[
        "New (0-12 months)",
        "Developing (13-24 months)",
        "Established (25-48 months)",
        "Long-term (49-72 months)"
    ]
)

print("\n========== CHURN BY TENURE GROUP ==========")
print(churn_by_segment("tenure_group"))
# ==========================================
# 9. CHURN BY SERVICES
# ==========================================

service_columns = [
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "PhoneService",
    "MultipleLines"
]

for service in service_columns:
    print(f"\n========== CHURN BY {service.upper()} ==========")
    print(churn_by_segment(service))
    # ==========================================
# 10. CHURN BY PAYMENT METHOD
# ==========================================

print("\n========== CHURN BY PAYMENT METHOD ==========")
print(churn_by_segment("PaymentMethod"))
# ==========================================
# 11. CHURN BY MONTHLY CHARGES
# ==========================================

df["monthly_charge_group"] = pd.cut(
    df["MonthlyCharges"],
    bins=[0, 40, 70, 100, float("inf")],
    labels=[
        "Low ($0-$40)",
        "Medium ($40-$70)",
        "High ($70-$100)",
        "Very High ($100+)"
    ]
)

print("\n========== CHURN BY MONTHLY CHARGE GROUP ==========")
print(churn_by_segment("monthly_charge_group"))
# ==========================================
# 12. CONTRACT × TENURE
# ==========================================

contract_tenure = pd.crosstab(
    df["tenure_group"],
    df["Contract"],
    values=df["Churn"].eq("Yes"),
    aggfunc="mean"
) * 100

print("\n========== CHURN RATE: CONTRACT × TENURE ==========")
print(contract_tenure.round(2))
# ==========================================
# 13. CONTRACT × TENURE SAMPLE SIZE
# ==========================================

contract_tenure_count = pd.crosstab(
    df["tenure_group"],
    df["Contract"]
)

print("\n========== CUSTOMER COUNT: CONTRACT × TENURE ==========")
print(contract_tenure_count)
# ==========================================
# 14. HIGH-RISK SEGMENT: NEW + MONTH-TO-MONTH
# ==========================================

high_risk = df[
    (df["tenure_group"] == "New (0-12 months)") &
    (df["Contract"] == "Month-to-month")
]

high_risk_total = len(high_risk)
high_risk_churned = (high_risk["Churn"] == "Yes").sum()
high_risk_churn_rate = (
    high_risk_churned / high_risk_total
) * 100

print("\n========== HIGH-RISK SEGMENT ==========")
print(f"Customers: {high_risk_total:,}")
print(f"Churned: {high_risk_churned:,}")
print(f"Churn rate: {high_risk_churn_rate:.2f}%")
high_risk = df[
    (df["tenure_group"] == "New (0-12 months)") &
    (df["Contract"] == "Month-to-month")
]

high_risk_total = len(high_risk)
high_risk_churned = (high_risk["Churn"] == "Yes").sum()
high_risk_churn_rate = (
    high_risk_churned / high_risk_total
) * 100

print("\n========== HIGH-RISK SEGMENT ==========")
print(f"Customers: {high_risk_total:,}")
print(f"Churned: {high_risk_churned:,}")
print(f"Churn rate: {high_risk_churn_rate:.2f}%")
# ==========================================
# 15. PROFILE HIGH-RISK CUSTOMERS
# ==========================================

profile_columns = [
    "PaymentMethod",
    "InternetService",
    "OnlineSecurity",
    "TechSupport",
    "SeniorCitizen",
    "Partner",
    "Dependents"
]

print("\n========== HIGH-RISK CUSTOMER PROFILE ==========")

for column in profile_columns:
    print(f"\n--- {column} ---")

    profile = high_risk.groupby(column).agg(
        customers=("customerID", "count"),
        churned=("Churn", lambda x: (x == "Yes").sum())
    )

    profile["churn_rate"] = (
        profile["churned"] / profile["customers"] * 100
    )

    profile["segment_share"] = (
        profile["customers"] / len(high_risk) * 100
    )

    print(profile.round(2))