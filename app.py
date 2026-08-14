import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(
    page_title = "Customer Behavior Analytics",
    layout = "wide"
)

df = pd.read_csv("customer_segmented.csv")

st.title("Customer Behavior Analytics Dashboard")
st.markdown(
  """
This interactive dashboard analyzes customer purchasing behavior, product preferences, payment patterns, subscription activity, and customer segments using K-Means clustering.
"""
)

st.divider()

# ------------------
# Sidebar Filters
# ------------------

st.sidebar.header("Filters")

gender_filter = st.sidebar.multiselect(
    "Gender",
    options = df["Gender"].unique(),
    default = df["Gender"].unique()
)

category_filter = st.sidebar.multiselect(
    "Category",
    options = df["Category"].unique(),
    default = df["Category"].unique()
)

season_filter = st.sidebar.multiselect(
    "Season",
    options = df["Season"].unique(),
    default = df["Season"].unique()
)

payment_filter = st.sidebar.multiselect(
    "Payment Method",
    options = df["Payment Method"].unique(),
    default = df["Payment Method"].unique()
)

subscription_filter = st.sidebar.multiselect(
    "Subscription Status",
    options = df["Subscription Status"].unique(),
    default = df["Subscription Status"].unique()
)

# Apply Filters

filtered_df = df[
    (df["Gender"].isin(gender_filter)) &
    (df["Category"].isin(category_filter)) &
    (df["Season"].isin(season_filter)) &
    (df["Payment Method"].isin(payment_filter)) &
    (df["Subscription Status"].isin(subscription_filter))
]

if filtered_df.empty:
  st.warning("No customers match the selected filters. Please select different filters.")
  st.stop()

# ----------------------
# KPI Calculations
# ----------------------
st.header("Key Perfomance Indicators")

total_customers = filtered_df["Customer ID"].nunique()
total_revenue = filtered_df["Purchase Amount (USD)"].sum()
average_purchase = filtered_df["Purchase Amount (USD)"].mean()
average_rating = filtered_df["Review Rating"].mean()

st.caption(
  f"Currently analyzing {len(filtered_df):,} customer purchase records."
)

# ===== KPI Cards =====

col1, col2, col3, col4 = st.columns(4)

with col1:
  st.metric("Total Customers", f"{total_customers:,}")

with col2:
  st.metric("Total Revenue", f"${total_revenue:,.2f}")

with col1:
  st.metric("Average Purchase", f"${average_purchase:,.2f}")

with col1:
  st.metric("Average Rating", f"{average_rating:,.2f}")

#  -------Customer Overview--------

st.header("Customer Overview")

col1, col2 = st.columns(2)

# Gender Distribution
with col1:
  st.subheader("Customer by Gender")
  gender_counts = filtered_df["Gender"].value_counts()

  fig, ax = plt.subplots(figsize=(6,4))
  gender_counts.plot(kind="bar", ax=ax)

  ax.set_xlabel("Gender")
  ax.set_ylabel("Number of Customers")
  ax.set_title("Customer Distribution by Gender")

  plt.xticks(rotation=0)
  plt.tight_layout()
  st.pyplot(fig)

# Age Group Distribution
with col2:
  st.subheader("Customers by Age Group")
  age_counts = filtered_df["Age Group"].value_counts()

  fig, ax = plt.subplots(figsize=(6,4))
  age_counts.plot(kind="bar", ax=ax)

  ax.set_xlabel("Age Group")
  ax.set_ylabel("Number of Customers")
  ax.set_title("Customer Distribution by Age Group")

  plt.xticks(rotation=45)
  plt.tight_layout()
  st.pyplot(fig)

# ---------PRODUCT ANALYSIS-----------

st.header("Product Analysis")

col1, col2 = st.columns(2)

# Revenue by Category
with col1:

  st.subheader("Product Category Revenue")

  category_revenue = (
    filtered_df.groupby("Category")["Purchase Amount (USD)"]
    .sum()
    .sort_values(ascending=False)
  )

  fig, ax = plt.subplots(figsize=(6,4))

  category_revenue.plot(kind="bar", ax=ax)

  ax.set_xlabel("Category")
  ax.set_ylabel("Revenue (USD)")
  ax.set_title("Revenue by Product Category")

  plt.xticks(rotation=45)
  plt.tight_layout()
  st.pyplot(fig)

# Top 10 Purchased Items

with col2:

  st.subheader("Top 10 Purchased Items")

  top_items = (
    filtered_df["Item Purchased"]
    .value_counts()
    .head(10)
    .sort_values()
  )

  fig, ax = plt.subplots(figsize=(6,4))
  top_items.plot(kind="barh", ax=ax)

  ax.set_xlabel("Number of Purchases")
  ax.set_ylabel("Item")
  ax.set_title("Top 10 Purchased Items")
      
  plt.tight_layout()
  st.pyplot(fig)

# ========= Purchase & Payment Analysis ===========

st.header("Purchase & Payment Analysis")

col1, col2 = st.columns(2)

# Payment Method
with col1:
  st.subheader("Payment Method Distribution")

  payment_counts = (
    filtered_df["Payment Method"]
    .value_counts()
  )

  fig, ax = plt.subplots(figsize=(6,4))

  payment_counts.plot(kind="bar", ax=ax)

  ax.set_xlabel("Payment Method")
  ax.set_ylabel("Number of Purchases")
  ax.set_title("Purchases by Payment Method")

  plt.xticks(rotation=45)
  plt.tight_layout()

  st.pyplot(fig)

# Shipping Type
with col2:
  st.subheader("Distribution by Shipping Type")

  shipping_counts = (
    filtered_df["Shipping Type"]
    .value_counts()
  )

  fig, ax = plt.subplots(figsize=(6,4))
  shipping_counts.plot(kind="bar", ax=ax)

  ax.set_xlabel("Shipping Type")
  ax.set_ylabel("Number of Purchases")
  ax.set_title("Purchases by Shipping Type")

  plt.xticks(rotation=45)
  plt.tight_layout()
  st.pyplot(fig)

# ========= Subscription & Discount Analysis =========

st.header("Subscription & Discount Analysis")

col1, col2 = st.columns(2)

# Subscription Status
with col1:
  st.subheader("Subscription Status")

  subscription_counts = (
    filtered_df["Subscription Status"]
  .value_counts()
  )

  fig, ax = plt.subplots(figsize=(6,4))
  subscription_counts.plot(kind="bar", ax=ax)

  ax.set_xlabel("Subscription Status")
  ax.set_ylabel("Number of Customers")
  ax.set_title("Subscribers vs Non-Subscribers")

  plt.xticks(rotation=0)
  plt.tight_layout()
  st.pyplot(fig)

# Discount Usage
with col2:

  st.subheader("Discount Usage")

  discount_counts = (
    filtered_df["Discount Applied"]
    .value_counts()
  )

  fig, ax = plt.subplots(figsize=(6,4))
  discount_counts.plot(kind="bar", ax=ax)

  ax.set_xlabel("Discount Applied")
  ax.set_ylabel("Number of Purchases")
  ax.set_title("Discount Usage")

  plt.xticks(rotation=0)
  plt.tight_layout()
  st.pyplot(fig)

# === Average Purchase by Subscription ===

st.subheader("Average Purchase Amount by Subscription Status")

subscription_purchase = (
  filtered_df.groupby("Subscription Status")["Purchase Amount (USD)"]
  .mean()
  .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,4))
subscription_purchase.plot(kind="bar", ax=ax)

ax.set_xlabel("Subscription Status")
ax.set_ylabel("Average Purchase Amount (USD)")
ax.set_title("Average Purchase Amount: Subscribers vs Non-Subscribers")

plt.xticks(rotation=0)
plt.tight_layout()
st.pyplot(fig)

# ======== CUSTOMER SEGMENTATION ==========

st.header("Customer Segmentation")  

cluster_names = {
  0: "High-Value Mature Customers",
  1: "Young Satisfied Customers",
  2: "Young Moderate-Spending Customers",
  3: "Loyal Low-Spending Customers"
}

# Cluster Distribution
st.subheader("Customer Distribution by Segment")

cluster_counts = (
  filtered_df["Cluster"]
  .value_counts()
  .sort_index()
)

fig, ax = plt.subplots(figsize=(8,4))
cluster_counts.plot(kind="bar", ax=ax)

ax.set_xlabel("Customer Segment")
ax.set_ylabel("Number of Customers")
ax.set_title("Customer Distribution by K-Means Cluster")

plt.xticks(rotation=0)
plt.tight_layout()
st.pyplot(fig)

# Customer Segment Profile
st.subheader("Customer Segment Profile")

cluster_profile = (
  filtered_df.groupby("Cluster")
  .agg(
    Customers = ("Customer ID", "nunique"),
    Avg_Age = ("Age", "mean"),
    Avg_Purchase = ("Purchase Amount (USD)", "mean"),
    Avg_Previous_Purchases = ("Previous Purchases", "mean"),
    Avg_Rating = ("Review Rating", "mean")
  )
  .round(2)
  .reset_index()
)

# Add business-friendly segment name
cluster_profile["Segment Name"] = cluster_profile["Cluster"].map(cluster_names)

# Arrange Columns
cluster_profile = cluster_profile[
  [
    "Cluster",
   "Segment Name",
   "Customers",
   "Avg_Age",
   "Avg_Purchase",
   "Avg_Previous_Purchases",
   "Avg_Rating"
   ]
]

# Set clean column names
cluster_profile.columns = [
  "Cluster Index",
  "Segment Name",
  "Customers",
  "Avg Age",
  "Avg Purchase",
  "Avg Previous Purchases",
  "Avg Rating"
]

st.dataframe(
  cluster_profile, use_container_width=True
)

# Spending vs Previous Purchases
st.subheader("Customer Segments: Spending vs Purchase History")

fig, ax = plt.subplots(figsize=(9,5))

for cluster in sorted(filtered_df["Cluster"].unique()):
  cluster_data = filtered_df[
    filtered_df["Cluster"] == cluster
  ]

  ax.scatter(
    cluster_data["Previous Purchases"],
    cluster_data["Purchase Amount (USD)"],
    label=f"Cluster {cluster}"
  )

ax.set_xlabel("Previous Purchases")
ax.set_ylabel("Purchase Amount (USD)")
ax.set_title("Customer Segmentation by Spending and Purchase History")
ax.legend()
plt.tight_layout()
st.pyplot(fig)

# ===== DOWNLOAD FILTERED DATA ======

st.header("Download Data")

csv = filtered_df.to_csv(index=False)

st.download_button(
  label = "Download Filtered Customer Data",
  data = csv,
  file_name = "filtered_customer_data.csv",
  mime = "text/csv"
)

