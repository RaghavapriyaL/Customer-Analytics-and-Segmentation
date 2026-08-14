# Customer Data Analysis and Customer Segmentation

## Project Overview

This project focuses on analyzing customer purchase data to identify patterns in customer demographics, purchasing behavior, product preferences, customer satisfaction, and loyalty.

The project uses Exploratory Data Analysis (EDA), feature engineering, and K-Means clustering to identify distinct customer segments. An interactive Streamlit dashboard was also developed to present the analytical results and allow users to explore the customer data through visualizations and filters.

---

## Objectives

The main objectives of this project are:

- Analyze customer demographic characteristics.
- Understand customer purchasing behavior.
- Identify high-performing product categories and products.
- Analyze payment, shipping, subscription, discount, and promotional behavior.
- Analyze customer review ratings.
- Create meaningful customer-level features.
- Segment customers using the K-Means clustering algorithm.
- Develop an interactive dashboard using Streamlit.
- Generate business insights and recommendations from the analysis.

---

## Dataset

The project uses a publicly available customer shopping dataset containing **3,900 customer purchase records and 18 original attributes**.

The dataset contains information related to:

- Customer demographics
- Products purchased
- Product categories
- Purchase amounts
- Locations
- Product sizes and colors
- Seasons
- Review ratings
- Subscription status
- Shipping methods
- Discount and promotional code usage
- Previous purchases
- Payment methods
- Purchase frequency

### Dataset Dimensions

| Property | Value |
|---|---|
| Records | 3,900 |
| Original Attributes | 18 |
| Final Attributes | 22 |
| Dataset Type | Customer purchase data |
| Segmentation Algorithm | K-Means Clustering |

---

## Data Preprocessing

The dataset was inspected and prepared before performing analysis.

The preprocessing steps included:

- Inspecting the dataset structure.
- Checking data types.
- Checking for missing values.
- Checking the consistency of categorical variables.
- Verifying numerical variables.
- Preparing the dataset for exploratory analysis and clustering.

The dataset contained **no missing values**, so no missing-value imputation or deletion was required.

The cleaned dataset was saved as:

`cleaned_customer_data.csv`

---

## Feature Engineering

Three additional customer-level features were created to support customer profiling.

### Age Group

Customers were categorized into age groups:

- 18–25
- 26–35
- 36–45
- 46–55
- 56–65
- 65+

### Spending Level

Customers were categorized into:

- Low
- Medium
- High

The categories were created using quantile-based segmentation of purchase amounts.

### Loyalty Level

Customers were categorized based on their previous purchases:

- New
- Regular
- Loyal
- VIP

The resulting dataset was used for further analysis and customer profiling.

---

## Exploratory Data Analysis

Exploratory Data Analysis was performed to identify patterns and relationships in the customer dataset.

The analysis covered:

- Customer demographic analysis
- Product and category analysis
- Payment method analysis
- Shipping type analysis
- Subscription behavior
- Discount and promotional code usage
- Purchase frequency
- Spending levels
- Loyalty levels
- Customer review ratings

### Key EDA Findings

- Male customers represented approximately **68%** of the records, while female customers represented **32%**.
- Clothing was the highest-revenue product category.
- Total purchase revenue was approximately **$233,081**.
- The average purchase amount was approximately **$59.76**.
- The average review rating was approximately **3.75**.
- PayPal was the most frequently used payment method.
- Non-subscribed customers represented approximately **73%** of the records.

---

## Customer Segmentation

Customer segmentation was performed using the **K-Means clustering algorithm**.

Four numerical features were selected for clustering:

- Age
- Purchase Amount (USD)
- Previous Purchases
- Review Rating

### Data Standardization

The selected features were standardized using `StandardScaler` before applying K-Means clustering.

### Selecting the Number of Clusters

The Elbow Method was used to calculate the Within-Cluster Sum of Squares (WCSS) for different values of K.

Based on the Elbow Method, **K = 4** was selected.

### K-Means Configuration

```python
KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

### 👩‍💻 Author

**Raghavapriya L**

Aspiring Data Analyst & Machine Learning Enthusiast

GitHub: *https://github.com/RaghavapriyaL*

---

⭐ If you found this project useful or interesting, feel free to star this repository!
