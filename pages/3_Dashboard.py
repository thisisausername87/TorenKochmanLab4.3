import streamlit as st
import pandas as pd
import plotly.express as px
import os

data_path = os.path.join(os.getcwd(), "data", "MrBeast_youtube_stats.csv")
df = pd.read_csv(data_path)

st.sidebar.header("Filters")
min_views = int(df["viewCount"].min())
max_views = int(df["viewCount"].max())

view_filter = st.sidebar.slider(
    "Filter by View Count",
    min_value=min_views,
    max_value=max_views,
    value=(min_views, max_views)
)

min_likes = int(df["likeCount"].min())
max_likes = int(df["likeCount"].max())

like_filter = st.sidebar.slider(
    "Filter by Like Count",
    min_value=min_likes,
    max_value=max_likes,
    value=(min_likes, max_likes)
)

min_dur = int(df["duration_seconds"].min())
max_dur = int(df["duration_seconds"].max())

duration_filter = st.sidebar.slider(
    "Filter by Video Duration (seconds)",
    min_value=min_dur,
    max_value=max_dur,
    value=(min_dur, max_dur)
)

filtered_df = df[
    (df["viewCount"].between(*view_filter)) &
    (df["likeCount"].between(*like_filter)) &
    (df["duration_seconds"].between(*duration_filter))
]

st.title("Analytics of Mr Beast YouTube Videos")
st.write("Adjust the filters of likes, duration, and views to show the desired subset of videos.")
st.write(f"**Videos matching filters:** {len(filtered_df)}")

fig1 = px.scatter(
    filtered_df,
    x="Video Duration in Seconds",
    y="Views",
    size="likeCount",
    color="commentCount",
    hover_data=["likeCount", "commentCount"],
    title="View Count by Video Duration"
)
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(
    filtered_df.sort_values("viewCount", ascending=False),
    x="Views",
    y="Likes",
    hover_data=["commentCount", "duration_seconds"],
    title="Like Count by View Count",
)
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.scatter(
    filtered_df,
    x="Likes",
    y="Number of Comments",
    title="Likes on a Video by Comments"
)
st.plotly_chart(fig3, use_container_width=True)

fig4 = px.histogram(
    filtered_df,
    x="Video Duration in Seconds",
    nbins=20,
    title="Distribution of Video Duration"
)
st.plotly_chart(fig4, use_container_width=True)
