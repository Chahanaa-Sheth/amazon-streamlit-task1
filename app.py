import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('amazon.csv')

# Show column names to debug if needed
st.write("Available columns:", df.columns.tolist())

# Use existing 'category' column (update name if needed)
if 'category' in df.columns:
    df['category'] = df['category']  # Optional alias for clarity
else:
    st.error("❌ Column 'category' not found in dataset.")
    st.stop()

# Title
st.title("📦 Amazon Product Sales Dashboard")

# Show raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw Dataset")
    st.write(df)

# Filter by product category
categories = df['category'].dropna().unique()
selected_category = st.selectbox("Select a Product Category", categories)

filtered_df = df[df['category'] == selected_category]

# Display summary
st.subheader(f"Summary for '{selected_category}'")
st.write(f"Number of Products: {filtered_df.shape[0]}")
st.write(filtered_df.describe())

# Show top-rated products
st.subheader("🌟 Top Rated Products")
top_rated = filtered_df.sort_values(by='rating', ascending=False).head(10)
st.write(top_rated[['product_name', 'rating', 'rating_count', 'discounted_price']])

# Price distribution chart
st.subheader("💰 Price Distribution")
st.bar_chart(filtered_df['discounted_price'].value_counts().head(20))

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Chahanaa")
