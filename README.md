# Customer Churn Analysis

## 📌 Project Overview

This project analyzes customer churn for **ABC Communications** to identify the customer characteristics and service patterns associated with customer attrition.

The project was completed as part of my **Analyst Lab Africa internship** and follows an end-to-end data analytics workflow, from data inspection and cleaning in Python to exploratory analysis, customer segmentation, business insights, and Power BI visualization.

The primary objective was to understand **who is most likely to churn, which factors are associated with higher churn, and where the company should prioritize retention efforts.**

---

## 🎯 Business Problem

ABC Communications is experiencing customer churn and needs to better understand the factors associated with customers leaving the company.

The analysis seeks to answer:

* What is the company's overall churn rate?
* Which customer groups have the highest churn?
* How does customer tenure relate to churn?
* How does contract type affect retention?
* Which services are associated with higher churn?
* Which payment methods are associated with customer attrition?
* Who represents the company's highest-risk customer segment?
* What actions can the company take to improve customer retention?

---

## 📊 Dataset

The dataset contains **7,043 customer records** and **21 variables** covering customer demographics, tenure, contracts, subscribed services, billing information, payment methods, and churn status.

### Key Variables

| Category              | Variables                                                                                                         |
| --------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Demographics          | Gender, Senior Citizen, Partner, Dependents                                                                       |
| Customer Relationship | Tenure, Contract                                                                                                  |
| Services              | Internet Service, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV, Streaming Movies |
| Phone Services        | Phone Service, Multiple Lines                                                                                     |
| Billing               | Monthly Charges, Total Charges, Paperless Billing, Payment Method                                                 |
| Target                | Churn                                                                                                             |

---

## 🛠️ Tools Used

* **Python**

  * Pandas
  * Data cleaning
  * Exploratory data analysis
  * Customer segmentation


  * Data visualization
  * Interactive dashboard
  * KPI reporting
  * Customer churn analysis

* **GitHub**

  * Project documentation
  * Version control
  * Portfolio presentation

---

## 🔎 Data Preparation

The raw dataset was inspected and prepared before analysis.

The data preparation process included:

1. Inspecting the dataset structure and dimensions.
2. Reviewing column names and data types.
3. Checking for duplicate records and duplicate customer IDs.
4. Identifying missing and blank values.
5. Investigating blank values in `TotalCharges`.
6. Converting `TotalCharges` from string to numeric format.
7. Saving the prepared dataset as `Lab_cleaned.csv`.

### Data Quality Findings

* **Rows:** 7,043
* **Columns:** 21
* **Duplicate rows:** 0
* **Duplicate customer IDs:** 0
* **Blank `TotalCharges` values:** 11
* **Zero-tenure customers:** 11

The 11 customers with blank `TotalCharges` all had a tenure of 0 months, which is consistent with customers who had not yet accumulated total charges.

---

## 📈 Key Findings

### Overall Churn

| Metric             |     Result |
| ------------------ | ---------: |
| Total Customers    |  **7,043** |
| Churned Customers  |  **1,869** |
| Retained Customers |  **5,174** |
| Churn Rate         | **26.54%** |
| Retention Rate     | **73.46%** |

---

### Contract Type

Contract type showed a strong difference in observed churn:

| Contract       | Churn Rate |
| -------------- | ---------: |
| Month-to-month | **42.71%** |
| One year       | **11.27%** |
| Two year       |  **2.83%** |

Month-to-month customers had substantially higher churn than customers on longer-term contracts.

---

### Customer Tenure

| Tenure Group               | Churn Rate |
| -------------------------- | ---------: |
| New (0–12 months)          | **47.44%** |
| Developing (13–24 months)  | **28.71%** |
| Established (25–48 months) | **20.39%** |
| Long-term (49–72 months)   |  **9.51%** |

Churn decreased substantially as customer tenure increased, making the early customer lifecycle an important area for retention efforts.

---

### Payment Method

| Payment Method   | Churn Rate |
| ---------------- | ---------: |
| Electronic check | **45.29%** |
| Mailed check     | **19.11%** |
| Bank transfer    | **16.71%** |
| Credit card      | **15.24%** |

Electronic-check customers had the highest observed churn rate among the payment methods analyzed.

---

### Internet Service

| Internet Service    | Churn Rate |
| ------------------- | ---------: |
| Fiber optic         | **41.89%** |
| DSL                 | **18.96%** |
| No internet service |  **7.40%** |

Fiber-optic customers showed substantially higher observed churn than DSL customers and customers without internet service.

---

## 🚨 High-Risk Customer Segment

A combined analysis of **tenure and contract type** identified the highest-risk customer segment as:

> **New customers (0–12 months) on month-to-month contracts**

### Segment Results

| Metric     |     Result |
| ---------- | ---------: |
| Customers  |  **1,994** |
| Churned    |  **1,024** |
| Churn Rate | **51.35%** |

This segment represents a particularly important retention opportunity because it is both **large and associated with a very high churn rate**.

### High-Risk Segment Profile

Further analysis of these 1,994 customers showed:

* **Electronic Check:** 954 customers; **63.10% churn**
* **Fiber Optic:** 916 customers; **70.20% churn**
* **No Online Security:** 1,370 customers; **61.68% churn**
* **No Tech Support:** 1,363 customers; **61.04% churn**

These characteristics provide useful direction for targeted customer retention strategies.

---

## 💡 Business Recommendations

Based on the analysis, the following actions are recommended:

### 1. Strengthen New-Customer Onboarding

Focus retention efforts on the first 12 months, particularly the first few months after acquisition.

### 2. Encourage Longer-Term Contracts

Develop incentives that encourage eligible month-to-month customers to move to one-year or two-year contracts.

### 3. Promote Automatic Payment Methods

Encourage customers using Electronic Check to adopt automatic payment options such as credit card or bank transfer.

### 4. Increase Adoption of Value-Added Services

Promote services such as Online Security and Tech Support through bundles, introductory offers, or targeted recommendations.

### 5. Prioritize High-Risk Customers

Develop targeted retention campaigns for new month-to-month customers, particularly those exhibiting additional high-risk characteristics.

---

## 📊  Dashboard

The dashboard provides an interactive view of:

* Customer and churn KPIs
* Churn by contract type
* Churn by tenure
* Churn by payment method
* Churn by internet service
* Churn by demographic characteristics
* Churn by subscribed services
* High-risk customer segments
* Key retention insights

The dashboard is designed to help stakeholders quickly understand **where churn is concentrated and which customer groups should receive greater retention attention.**

---

## 📁 Project Structure

```text
customer-churn-analysis/
│
├── data/
│   └── Lab_cleaned.csv
│
├── scripts/
│   ├── inspection.py
│   ├── cleaning.py
│   └── analysis.py
│
├── dashboard/
│   └── Customer_Churn_Dashboard.pbix
│
├── report/
│   └── Customer_Churn_Case_Study.pdf
│
└── README.md
```

> **Note:** The raw customer dataset is not included in this repository unless its distribution is permitted by the dataset owner.

---

## ⚠️ Limitations

The analysis identifies **associations**, not proven causal relationships.

For example, although customers without Online Security demonstrated higher churn, this analysis does not establish that the absence of Online Security directly caused customers to leave.

The dataset also does not contain potentially useful variables such as customer satisfaction, complaints, service quality, competitor activity, or promotional offers.

Future analysis could incorporate these variables and develop a predictive churn model to estimate the probability of churn for individual customers.

---

## 📌 Conclusion

The analysis demonstrates that customer churn is concentrated within identifiable customer segments rather than being evenly distributed across the customer base.

The most significant retention opportunity identified was the **New + Month-to-month customer segment**, which recorded a **51.35% churn rate across 1,994 customers**.

The findings provide ABC Communications with a data-driven foundation for prioritizing retention efforts around early customer engagement, contract migration, payment behavior, and adoption of value-added services.

---

## 👤 Author

**Moses Oluwatosin Olusola**

Data Analyst | Statistics Student | Analyst Lab Africa Intern

### Skills Demonstrated

`Python` `Pandas` `Data Cleaning` `Exploratory Data Analysis` `Customer Segmentation` `Power BI` `Data Visualization` `Business Intelligence` `Data Storytelling`
