import streamlit as st
import pandas as pd
import plotly.express as px
import os

data_path = os.path.join(os.getcwd(), "data", "MrBeast_youtube_stats.csv")
df = pd.read_csv(data_path)

st.sidebar.header("Filters")

# Create a view-count slider from min–max values in the dataset
min_views = int(df["viewCount"].min())
max_views = int(df["viewCount"].max())

view_filter = st.sidebar.slider(
    "Filter by View Count",
    min_value=min_views,
    max_value=max_views,
    value=(min_views, max_views)
)

# Apply the filter
filtered_df = df[
    (df["viewCount"] >= view_filter[0]) &
    (df["viewCount"] <= view_filter[1])
]

st.title("📊 MrBeast Videos Dashboard")
st.write("Interactive dashboard powered by Plotly Express + Streamlit.")

st.write(f"Filtered rows: {len(filtered_df)}")

# -----------------------------------
# Charts
# -----------------------------------

# Scatter: Duration vs Views
fig1 = px.scatter(
    filtered_df,
    x="duration_seconds",
    y="viewCount",
    size="likeCount",
    color="commentCount",
    hover_data=["likeCount", "commentCount"],
    title="Duration vs View Count (Bubble size = likes)"
)
st.plotly_chart(fig1, use_container_width=True)

# Bar chart: Likes vs Views
fig2 = px.bar(
    filtered_df.sort_values("viewCount", ascending=False),
    x="viewCount",
    y="likeCount",
    hover_data=["commentCount", "duration_seconds"],
    title="Like Count by View Count",
)
st.plotly_chart(fig2, use_container_width=True)

# Scatter: Likes vs Comments
fig3 = px.scatter(
    filtered_df,
    x="likeCount",
    y="commentCount",
    trendline="ols",
    title="Like Count vs Comment Count"
)
st.plotly_chart(fig3, use_container_width=True)

# Histogram of video durations
fig4 = px.histogram(
    filtered_df,
    x="duration_seconds",
    nbins=20,
    title="Distribution of Video Duration"
)
st.plotly_chart(fig4, use_container_width=True)
