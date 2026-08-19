import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Churn Dashboard", layout="wide")

# Load data
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Clean data
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna(subset=['TotalCharges'])
df['ChurnFlag'] = df['Churn'].map({'No': 0, 'Yes': 1})
df['SeniorCitizenLabel'] = df['SeniorCitizen'].map({0: "No", 1: "Yes"})

# ---- SIDEBAR FILTERS ----
st.sidebar.header("🔍 Filter Data")
contract_filter = st.sidebar.multiselect(
    "Contract Type",
    options=df['Contract'].unique(),
    default=df['Contract'].unique()
)

payment_filter = st.sidebar.multiselect(
    "Payment Method",
    options=df['PaymentMethod'].unique(),
    default=df['PaymentMethod'].unique()
)

# Apply filters
filtered_df = df[
    (df['Contract'].isin(contract_filter)) &
    (df['PaymentMethod'].isin(payment_filter))
]

# ---- MAIN DASHBOARD ----
st.title("📊 Customer Churn Dashboard")
st.markdown("### Interactive Retention Analysis")

# ---- KPIs ----
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", f"{len(filtered_df):,}")
col2.metric("Churn Rate", f"{filtered_df['ChurnFlag'].mean()*100:.1f}%")
col3.metric("Avg Tenure", f"{filtered_df['tenure'].mean():.1f} months")
col4.metric("Avg Monthly Charge", f"R{filtered_df['MonthlyCharges'].mean():,.2f}")

# ---- INTERACTIVE CHARTS ----
tab1, tab2, tab3, tab4 = st.tabs(["📈 Churn by Contract", "💳 Churn by Payment", "🌐 Churn by Service", "👴 Senior Citizens"])

with tab1:
    contract_churn = filtered_df.groupby('Contract')['ChurnFlag'].mean().mul(100).reset_index()
    fig = px.bar(contract_churn, x='Contract', y='ChurnFlag', title="Churn Rate by Contract",
                 color='ChurnFlag', color_continuous_scale='Reds',
                 labels={'ChurnFlag': 'Churn Rate (%)'})
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    payment_churn = filtered_df.groupby('PaymentMethod')['ChurnFlag'].mean().mul(100).reset_index()
    fig = px.bar(payment_churn, x='PaymentMethod', y='ChurnFlag', title="Churn Rate by Payment Method",
                 color='ChurnFlag', color_continuous_scale='Reds',
                 labels={'ChurnFlag': 'Churn Rate (%)'})
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    internet_churn = filtered_df.groupby('InternetService')['ChurnFlag'].mean().mul(100).reset_index()
    fig = px.pie(internet_churn, values='ChurnFlag', names='InternetService', 
                 title="Churn by Internet Service",
                 labels={'ChurnFlag': 'Churn Rate (%)'})
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    senior_churn = filtered_df.groupby('SeniorCitizenLabel')['ChurnFlag'].mean().mul(100).reset_index()
    fig = px.bar(senior_churn, x='SeniorCitizenLabel', y='ChurnFlag', 
                 title="Churn by Senior Citizen Status",
                 color='ChurnFlag', color_continuous_scale='Reds',
                 labels={'ChurnFlag': 'Churn Rate (%)'})
    st.plotly_chart(fig, use_container_width=True)

# ---- TENURE ANALYSIS ----
st.subheader("📉 Tenure vs Churn")
fig = px.histogram(filtered_df, x='tenure', color='Churn', nbins=30, 
                   title="Customer Tenure Distribution by Churn Status",
                   barmode='overlay',
                   labels={'tenure': 'Tenure (Months)'})
st.plotly_chart(fig, use_container_width=True)

# ---- RAW DATA ----
with st.expander("📋 View Raw Data"):
    st.dataframe(filtered_df.head(100))
