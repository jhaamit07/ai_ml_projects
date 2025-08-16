import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your cleaned CSV file
data = pd.read_csv('cleaned_gdp_dataset.csv')

# Title for the Streamlit app
st.title('GDP Prediction Project')

# Description of the app
st.write("""
This is an interactive app that shows a preview of the cleaned GDP dataset. You can use the widgets below to filter and explore the data.
""")

# Display the dataframe
st.write("Cleaned Data Preview:")
st.dataframe(data.head())

# Slider to select number of rows to display
rows_to_show = st.slider("Select number of rows to display", 1, 100, 10)
st.write(f"Showing top {rows_to_show} rows:")
st.dataframe(data.head(rows_to_show))

# Dropdown to select a column for visualization
column = st.selectbox("Select a column to visualize", data.columns)
st.write(f"You selected {column}.")

# Button to display basic statistics
if st.button('Show Statistics'):
    st.write("Descriptive Statistics:")
    st.write(data.describe())

# Filter based on a specific column (e.g., filtering countries based on GDP)
country_filter = st.text_input("Filter by Country (leave empty for all)", "")
if country_filter:
    filtered_data = data[data['Country'].str.contains(country_filter, case=False, na=False)]
    st.write(f"Filtered Data (Countries matching '{country_filter}'):")
    st.dataframe(filtered_data.head())
else:
    st.write("Showing all countries.")

# Option to plot data (choose columns for plotting)
if st.checkbox('Show data plot'):
# You can plot a column against another for example

    fig, ax = plt.subplots(figsize=(10, 6))
    data.plot(x='Country', y=column, kind='hist', ax=ax)
    ax.set_xlabel('Country')
    ax.set_ylabel(column)
    ax.set_title(f'{column} vs Country')
    st.pyplot(fig)


# # Display additional insights (like missing values)

if st.checkbox('Show Data Info'):
    st.subheader("Data Info Summary")

    # Create a more readable DataFrame
    info_df = pd.DataFrame({
        'Column': data.columns,
        'Data Type': data.dtypes.values,
        'Non-Null Count': data.notnull().sum().values,
        'Missing Values': data.isnull().sum().values
    })

    st.dataframe(info_df)
    st.write(f"🔢 Total Columns: {data.shape[1]}")
    st.write(f"🧮 Total Rows: {data.shape[0]}")


# # Show feature importance (if you have a trained model available)
# if st.checkbox('Show Feature Importance'):
#     # If you have a trained model, you can show feature importances here.
#     # Example (replace with actual trained model):
#     # feature_importances = model.feature_importances_
#     # feature_df = pd.DataFrame({'feature': data.columns, 'importance': feature_importances})
#     st.write("Feature importance details can be shown here if the model is available.")

if st.checkbox('Show Feature Importance'):
    st.subheader("📊 Feature Importance from Random Forest Model")

    try:
        import joblib

        # Load model and feature columns
        model = joblib.load('../models/best_random_forest.pkl')
        feature_columns = joblib.load('../models/feature_columns.pkl')  # List of columns used in training

        # Use only those columns for feature importance
        feature_data = data[feature_columns]

        importances = model.feature_importances_
        if len(importances) != len(feature_columns):
            raise ValueError("Mismatch between model features and dataset columns.")

        importance_df = pd.DataFrame({
            'Feature': feature_columns,
            'Importance': importances
        }).sort_values(by='Importance', ascending=False)

        st.dataframe(importance_df)

        # Plotting
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(importance_df['Feature'], importance_df['Importance'], color='skyblue')
        ax.set_xlabel('Importance')
        ax.set_ylabel('Features')
        ax.set_title('Feature Importance')
        st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Could not load model or calculate feature importances.\n\n{e}")
