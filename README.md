# 📊 FUTURE_DS_02 — Customer Retention & Churn Analysis

> **Task 2** | Future Interns — Data Science & Analytics Track

---

## 📌 Project Overview

This project analyzes customer data for a subscription-based business to identify churn patterns, retention drivers, and customer lifetime trends. The analysis provides actionable insights to reduce customer churn and improve retention strategies.

---

## 🎯 Key Objectives

- Identify customer churn patterns and drivers
- Analyze retention trends across customer segments
- Examine contract, payment, and service impacts on churn
- Segment high-risk customers for targeted retention
- Deliver an interactive dashboard for stakeholder insights

---

## 📊 Key Metrics

| Metric | Value |
|--------|-------|
| **Total Customers** | 7,032 |
| **Churn Rate** | 26.58% |
| **Retention Rate** | 73.42% |
| **Average Tenure** | 32.42 months |
| **Avg Monthly Charge** | R64.80 |

---

## 📈 Churn Rate Overview
Overall Churn Rate: 26.58%
├── Churned: ████████████████████████░░░░░░░░░░░░░░ 26.58% (1,869 customers)
└── Retained: ██████████████████████████████████████ 73.42% (5,163 customers)

### Churn by Category
Contract Type:
├── Month-to-month ████████████████████████████████ 42.71%
├── One year ████████████░░░░░░░░░░░░░░░░░░░░ 11.28%
└── Two year ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 2.85%

Payment Method:
├── Electronic check ██████████████████████████████ 45.29%
├── Mailed check ████████████████░░░░░░░░░░░░░░ 19.20%
├── Bank transfer ██████████████░░░░░░░░░░░░░░░░ 16.73%
└── Credit card █████████████░░░░░░░░░░░░░░░░░ 15.25%

Internet Service:
├── Fiber optic ████████████████████████████████ 41.89%
├── DSL ████████████████████░░░░░░░░░░░░ 19.00%
└── No service ████████░░░░░░░░░░░░░░░░░░░░░░░░ 7.43%

Tenure Group:
├── 0-12 months ████████████████████████████████ 47.68%
├── 13-24 months ████████████████████████░░░░░░░░ 28.71%
├── 25-48 months ██████████████████░░░░░░░░░░░░░░ 20.39%
└── 49-72 months ████████░░░░░░░░░░░░░░░░░░░░░░░░ 9.51%

---

## 🔍 Key Insights

| Category | Highest Churn Rate | Key Takeaway |
|----------|-------------------|--------------|
| **Contract** | Month-to-month: 42.71% | Customers without long-term contracts are 15x more likely to churn |
| **Payment** | Electronic check: 45.29% | Manual payment methods correlate with higher churn |
| **Internet** | Fiber optic: 41.89% | Premium service customers churn more despite higher value |
| **Tenure** | 0-12 months: 47.68% | New customers are most vulnerable to churn |
| **Demographic** | Senior citizens: 41.68% | Age segment shows significantly higher churn |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| **Python** | Data processing & analysis |
| **Pandas / NumPy** | Data manipulation |
| **Matplotlib / Seaborn** | Static visualizations |
| **Plotly** | Interactive charts |
| **Streamlit** | Interactive dashboard |
| **Jupyter Notebook** | Exploratory analysis |

---

## 📁 Project Structure
FUTURE_DS_02/
│
├── 📄 README.md # Project documentation
├── 📄 requirements.txt # Python dependencies
│
├── 📂 dashboard/
│ └── 🐍 app.py # Streamlit interactive dashboard
│
├── 📂 data/
│ └── 📊 WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── 📂 images/ # Generated visualizations
│ ├── 🖼️ 01_churn_by_contract.png
│ ├── 🖼️ 02_churn_by_payment_method.png
│ ├── 🖼️ 03_churn_by_internet_service.png
│ ├── 🖼️ 04_churn_by_senior_citizen.png
│ ├── 🖼️ 05_churn_by_tenure.png
│ ├── 🖼️ 06_monthly_charges_vs_churn.png
│ └── 🖼️ 07_tenure_distribution.png
│
├── 📂 notebooks/
│ └── 📓 Customer_Retention_Churn_Analysis.ipynb
│
└── 📂 scripts/
└── 🐍 analysis.py # Complete analysis script

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/siphemhlongo21-ctrl/FUTURE_DS_02.git
cd FUTURE_DS_02
### 2️⃣ Install Dependencies
pip install -r requirements.txt
### 3️⃣ Run the Dashboard
streamlit run dashboard/app.py
### 4️⃣ Run Analysis Script
python scripts/analysis.py
📊 Dashboard Features
Feature	Status	Description
🔍 Interactive Filters	✅	Contract Type & Payment Method
📊 Real-time KPIs	✅	Updated instantly on filter change
📈 Churn by Contract	✅	Bar chart with color gradient
💳 Churn by Payment	✅	Bar chart by payment method
🌐 Churn by Service	✅	Pie chart for internet services
👴 Senior Citizen Churn	✅	Bar chart comparison
📉 Tenure Analysis	✅	Interactive histogram
📋 Raw Data Viewer	✅	Expandable data table
📈 Visualization Gallery
Chart	Description
https://images/01_churn_by_contract.png	Churn rate by contract type
https://images/02_churn_by_payment_method.png	Churn rate by payment method
https://images/03_churn_by_internet_service.png	Churn rate by internet service
https://images/04_churn_by_senior_citizen.png	Churn by senior citizen status
https://images/05_churn_by_tenure.png	Churn by customer tenure
https://images/06_monthly_charges_vs_churn.png	Monthly charges by churn
https://images/07_tenure_distribution.png	Tenure distribution by churn
💡 Actionable Recommendations
#	Recommendation	Impact
1	Target new customers early — Onboarding campaigns in first 12 months	High
2	Encourage longer contracts — Incentives for month-to-month customers	High
3	Investigate electronic-check customers — Promote automatic payments	Medium
4	Promote TechSupport & OnlineSecurity — Lower churn rates observed	Medium
5	Monitor high-risk segment — 816 customers identified	High
🎯 High-Risk Customer Segment
High-Risk Segment Characteristics:
├── Contract: Month-to-month
├── Tenure: ≤ 12 months
└── Monthly Charges: Above median (≥ R64.80)

📊 Count: 816 customers identified
⚠️  Priority: Immediate retention intervention recommended
📊 Churn Driver Analysis
Top Churn Drivers:
├── 1. Contract Type (Month-to-month)    ████████████ 42.71%
├── 2. Payment Method (Electronic check) ████████████ 45.29%
├── 3. Short Tenure (0-12 months)        ████████████ 47.68%
├── 4. Internet Service (Fiber optic)    ████████████ 41.89%
└── 5. Senior Citizen Status             ████████████ 41.68%
🔗 Links
GitHub: https://github.com/siphemhlongo21-ctrl/FUTURE_DS_02

Live Dashboard: (Deploy on Streamlit Cloud)

👨‍💻 Author
Siphesihle Mhlongo
Data Science & Analytics Intern @ Future Interns
📧 contact@futureinterns.com
🔗 https://github.com/siphemhlongo21-ctrl

📜 License
This project is part of the Future Interns Data Science Internship program.

🙏 Acknowledgments
Future Interns — For the opportunity and guidance

Dataset: Telco Customer Churn Dataset (IBM)

Last Updated: August 2026

Siphesihle Mhlongo
Future Interns — Data Science & Analytics
