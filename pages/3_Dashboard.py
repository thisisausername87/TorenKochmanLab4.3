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

st.title("Mr Beast Video Statistics Analysis")
st.write("Filter videos by subset using the sliders on the left side pannel.")

st.write(f"**Videos matching filters:** {len(filtered_df)}")

fig1 = px.scatter(
    filtered_df,
    x="duration_seconds",
    y="viewCount",
    size="likeCount",
    color="commentCount",
    hover_data=["likeCount", "commentCount"],
    title="Duration vs View Count (Bubble size = likes)"
)
fig.update_layout(
    xaxis_title="Video Duration",
    yaxis_title="Nunber of Views"
)
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(
    filtered_df.sort_values("viewCount", ascending=False),
    x="viewCount",
    y="likeCount",
    hover_data=["commentCount", "duration_seconds"],
    title="Like Count by View Count",
)
fig.update_layout(
    xaxis_title="Views",
    yaxis_title="Likes"
)
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.scatter(
    filtered_df,
    x="likeCount",
    y="commentCount",
    title="Like Count vs Comment Count"
)
fig.update_layout(
    xaxis_title="Likes",
    yaxis_title="Nunber of Comments"
)
st.plotly_chart(fig3, use_container_width=True)

fig4 = px.histogram(
    filtered_df,
    x="duration_seconds",
    nbins=20,
    title="Distribution of Video Duration"
)
fig.update_layout(
    xaxis_title="Video Duration",
    yaxis_title="Count"
)
st.plotly_chart(fig4, use_container_width=True)
