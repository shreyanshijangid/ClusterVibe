import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import plotly.express as px

# Setting the page config for that "Premium" feel
st.set_page_config(page_title="ClusterVibe: AI Segmenter", layout="wide")

# Custom CSS for the aesthetic
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button:first-child { background-color: #ff4b4b; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ ClusterVibe: The AI Segmenter")
st.write("Grouping data points based on their 'vibe' (features) using Machine Learning.")

# 1. Generating a Random "Festival" Dataset
np.random.seed(42)
n_points = 300
data = pd.DataFrame({
    'Spending_Score': np.random.randint(1, 100, n_points),
    'Hype_Level': np.random.randint(1, 100, n_points)
})

# Sidebar for User Interaction
st.sidebar.header("🎛️ Adjust Settings")
k_value = st.sidebar.slider("Select 'K' (Number of Clusters)", min_value=2, max_value=8, value=3)
show_centroids = st.sidebar.checkbox("Show Cluster Centers", value=True)

# 2. The ML Logic (K-Means)
kmeans = KMeans(n_clusters=k_value, random_state=42, n_init=10)
data['Cluster'] = kmeans.fit_predict(data)
data['Cluster'] = data['Cluster'].astype(str) # For discrete colors in Plotly

# 3. Visualizing the Magic
fig = px.scatter(
    data, 
    x='Spending_Score', 
    y='Hype_Level', 
    color='Cluster',
    title=f"Result: {k_value} Groups Identified",
    template="plotly_dark",
    color_discrete_sequence=px.colors.qualitative.Pastel
)

if show_centroids:
    centers = kmeans.cluster_centers_
    fig.add_scatter(
        x=centers[:, 0], y=centers[:, 1], 
        mode='markers', 
        marker=dict(color='white', size=15, symbol='x'),
        name="Cluster Centers"
    )

st.plotly_chart(fig, use_container_width=True)

# 4. Insights Table
st.subheader("📊 Data Breakdown")
col1, col2 = st.columns(2)
with col1:
    st.write("Last 5 Data Points:")
    st.dataframe(data.tail())
with col2:
    st.write("Cluster Counts:")
    st.bar_chart(data['Cluster'].value_counts())