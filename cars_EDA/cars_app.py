import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("CARS_1.csv")

st.set_page_config(page_title="Cars EDA Dashboard", layout="wide")

st.title("🚗 Cars Dataset Analysis Dashboard")

# Raw data preview
st.subheader("📋 Raw Dataset Preview")
st.dataframe(df.head())

# Basic statistics
st.subheader("📊 Dataset Statistics")
st.write(df.describe(include='all'))

# Average Starting Price by Fuel Type
st.subheader("💰 Average Starting Price by Fuel Type")
fuel_price = df.groupby("fuel_type")["starting_price"].mean().sort_values()
fig, ax = plt.subplots()
fuel_price.plot(kind="bar", ax=ax, color="gold")
ax.set_ylabel("Average Starting Price")
st.pyplot(fig)

# Car Count by Body Type
st.subheader("🚙 Car Count by Body Type")
body_count = df["body_type"].value_counts()
fig, ax = plt.subplots()
body_count.plot(kind="barh", ax=ax, color="skyblue")
ax.set_xlabel("Number of Cars")
st.pyplot(fig)

# Seating Capacity Distribution
st.subheader("🪑 Seating Capacity Distribution")
fig, ax = plt.subplots()
sns.countplot(data=df, x="seating_capacity", ax=ax, palette="viridis")
st.pyplot(fig)

# Correlation Heatmap (numerical features only)
st.subheader("📈 Correlation Heatmap")
numeric_df = df.select_dtypes(include="number")
fig, ax = plt.subplots(figsize=(8,5))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Price Range (Ending - Starting)
st.subheader("📏 Price Range of Cars")
df["price_range"] = df["ending_price"] - df["starting_price"]
fig, ax = plt.subplots()
sns.histplot(df["price_range"], bins=20, kde=True, color="green", ax=ax)
ax.set_xlabel("Price Range")
st.pyplot(fig)
