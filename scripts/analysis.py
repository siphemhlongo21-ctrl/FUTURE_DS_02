import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ---------------------------------------------------------
# FUTURE_DS_02 - Customer Retention & Churn Analysis
# Future Interns - Data Science & Analytics
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
IMAGE_DIR = BASE_DIR / "images"

IMAGE_DIR.mkdir(exist_ok=True)

# Load dataset
file_path = DATA_DIR / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
df = pd.read_csv(file_path)

print("=" * 60)
print("CUSTOMER RETENTION & CHURN ANALYSIS")
print("=" * 60)

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 records:")
print(df.head())

# ---------------------------------------------------------
# Data Cleaning
# ---------------------------------------------------------

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Remove missing TotalCharges values
df = df.dropna(subset=["TotalCharges"]).copy()

# Convert SeniorCitizen to readable labels
df["SeniorCitizenLabel"] = df["SeniorCitizen"].map({
    0: "No",
    1: "Yes"
})

# Churn numeric version
df["ChurnFlag"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

print("\nMissing values:")
print(df.isnull().sum())

# ---------------------------------------------------------
# KPI Analysis
# ---------------------------------------------------------

total_customers = len(df)
churned_customers = df["ChurnFlag"].sum()
retained_customers = total_customers - churned_customers

churn_rate = (churned_customers / total_customers) * 100
retention_rate = (retained_customers / total_customers) * 100

average_monthly_charges = df["MonthlyCharges"].mean()
average_total_charges = df["TotalCharges"].mean()
average_tenure = df["tenure"].mean()

print("\nKEY PERFORMANCE INDICATORS")
print("-" * 40)
print(f"Total Customers: {total_customers:,}")
print(f"Churned Customers: {churned_customers:,}")
print(f"Retained Customers: {retained_customers:,}")
print(f"Churn Rate: {churn_rate:.2f}%")
print(f"Retention Rate: {retention_rate:.2f}%")
print(f"Average Monthly Charges: ${average_monthly_charges:,.2f}")
print(f"Average Total Charges: ${average_total_charges:,.2f}")
print(f"Average Customer Tenure: {average_tenure:.2f} months")

# ---------------------------------------------------------
# Churn by Contract
# ---------------------------------------------------------

contract_churn = (
    df.groupby("Contract")["ChurnFlag"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

print("\nChurn Rate by Contract:")
print(contract_churn)

plt.figure(figsize=(9, 6))
contract_churn.plot(kind="bar")
plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(IMAGE_DIR / "01_churn_by_contract.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Churn by Payment Method
# ---------------------------------------------------------

payment_churn = (
    df.groupby("PaymentMethod")["ChurnFlag"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

print("\nChurn Rate by Payment Method:")
print(payment_churn)

plt.figure(figsize=(10, 6))
payment_churn.plot(kind="bar")
plt.title("Churn Rate by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "02_churn_by_payment_method.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Churn by Internet Service
# ---------------------------------------------------------

internet_churn = (
    df.groupby("InternetService")["ChurnFlag"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

print("\nChurn Rate by Internet Service:")
print(internet_churn)

plt.figure(figsize=(9, 6))
internet_churn.plot(kind="bar")
plt.title("Churn Rate by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(IMAGE_DIR / "03_churn_by_internet_service.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Churn by Senior Citizen
# ---------------------------------------------------------

senior_churn = (
    df.groupby("SeniorCitizenLabel")["ChurnFlag"]
    .mean()
    .mul(100)
)

print("\nChurn Rate by Senior Citizen Status:")
print(senior_churn)

plt.figure(figsize=(8, 6))
senior_churn.plot(kind="bar")
plt.title("Churn Rate by Senior Citizen Status")
plt.xlabel("Senior Citizen")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(IMAGE_DIR / "04_churn_by_senior_citizen.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Tenure Analysis
# ---------------------------------------------------------

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[0, 12, 24, 48, 72],
    labels=[
        "0-12 months",
        "13-24 months",
        "25-48 months",
        "49-72 months"
    ],
    include_lowest=True
)

tenure_churn = (
    df.groupby("TenureGroup", observed=True)["ChurnFlag"]
    .mean()
    .mul(100)
)

print("\nChurn Rate by Tenure:")
print(tenure_churn)

plt.figure(figsize=(9, 6))
tenure_churn.plot(kind="bar")
plt.title("Churn Rate by Customer Tenure")
plt.xlabel("Tenure Group")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(IMAGE_DIR / "05_churn_by_tenure.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Monthly Charges vs Churn
# ---------------------------------------------------------

plt.figure(figsize=(9, 6))
sns.boxplot(
    data=df,
    x="Churn",
    y="MonthlyCharges"
)
plt.title("Monthly Charges by Churn Status")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "06_monthly_charges_vs_churn.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Customer Lifetime / Tenure
# ---------------------------------------------------------

plt.figure(figsize=(9, 6))
sns.histplot(
    data=df,
    x="tenure",
    hue="Churn",
    bins=30,
    kde=True
)
plt.title("Customer Tenure Distribution by Churn Status")
plt.xlabel("Tenure (Months)")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "07_tenure_distribution.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Churn Drivers
# ---------------------------------------------------------

driver_columns = [
    "Contract",
    "InternetService",
    "PaymentMethod",
    "TechSupport",
    "OnlineSecurity",
    "PaperlessBilling"
]

print("\n" + "=" * 60)
print("POTENTIAL CHURN DRIVERS")
print("=" * 60)

for column in driver_columns:
    print(f"\n{column}")
    result = (
        df.groupby(column)["ChurnFlag"]
        .mean()
        .mul(100)
        .sort_values(ascending=False)
    )
    print(result)

# ---------------------------------------------------------
# High-Risk Customers
# ---------------------------------------------------------

high_risk = df[
    (df["Contract"] == "Month-to-month") &
    (df["tenure"] <= 12) &
    (df["MonthlyCharges"] >= df["MonthlyCharges"].median())
].copy()

print("\nHigh-Risk Customer Segment")
print("-" * 40)
print(f"High-risk customers: {len(high_risk):,}")

# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

highest_contract = contract_churn.idxmax()
highest_payment = payment_churn.idxmax()
highest_internet = internet_churn.idxmax()

print(f"\n1. Overall churn rate is {churn_rate:.2f}%.")

print(
    f"2. {highest_contract} contract customers "
    f"have the highest churn rate at "
    f"{contract_churn[highest_contract]:.2f}%."
)

print(
    f"3. {highest_payment} customers "
    f"have the highest churn rate among payment methods."
)

print(
    f"4. {highest_internet} internet service "
    f"has the highest churn rate among internet services."
)

print(
    f"5. Customers with short tenure should receive "
    f"early retention interventions."
)

print(
    f"6. High-risk customers identified using "
    f"contract, tenure and monthly charge characteristics: "
    f"{len(high_risk):,}."
)

print("\nAnalysis complete.")
print(f"Charts saved to: {IMAGE_DIR}")
