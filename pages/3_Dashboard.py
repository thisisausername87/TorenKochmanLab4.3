import streamlit as st
import pandas as pd
import plotly.express as px
import os

data_path = os.path.join(os.getcwd(), "data", "MrBeast_youtube_stats.csv")
df = pd.read_csv(data_path)


st.sidebar.header("Filters")

# --- View Count Filter ---
min_views = int(df["viewCount"].min())
max_views = int(df["viewCount"].max())

view_filter = st.sidebar.slider(
    "Filter by View Count",
    min_value=min_views,
    max_value=max_views,
    value=(min_views, max_views)
)

# --- Like Count Filter ---
min_likes = int(df["likeCount"].min())
max_likes = int(df["likeCount"].max())

like_filter = st.sidebar.slider(
    "Filter by Like Count",
    min_value=min_likes,
    max_value=max_likes,
    value=(min_likes, max_likes)
)

# --- Duration Filter (seconds) ---
min_dur = int(df["duration_seconds"].min())
max_dur = int(df["duration_seconds"].max())

duration_filter = st.sidebar.slider(
    "Filter by Video Duration (seconds)",
    min_value=min_dur,
    max_value=max_dur,
    value=(min_dur, max_dur)
)

# -----------------------------------
# Apply Filters
# -----------------------------------
filtered_df = df[
    (df["viewCount"].between(*view_filter)) &
    (df["likeCount"].between(*like_filter)) &
    (df["duration_seconds"].between(*duration_filter))
]

# -----------------------------------
# Dashboard Title
# -----------------------------------
st.title("📊 MrBeast Videos Dashboard")
st.write("Interactive dashboard using 3 filters (views, likes, duration).")

st.write(f"**Videos matching filters:** {len(filtered_df)}")

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

# Bar: Likes vs Views
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
    title="Like Count vs Comment Count"
)
st.plotly_chart(fig3, use_container_width=True)

# Histogram: Duration distribution
fig4 = px.histogram(
    filtered_df,
    x="duration_seconds",
    nbins=20,
    title="Distribution of Video Duration"
)
st.plotly_chart(fig4, use_container_width=True)
