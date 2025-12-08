import streamlit as st
import pandas as pd
import plotly.express as px
import os

data_path = os.path.join(os.getcwd(), "data", "MrBeast_youtube_stats.csv")
df = pd.read_csv(data_path)
views = df["viewCount"]
df_sorted = df.sort_values(by="viewCount")

st.title("Different Types of Charts")
st.subheader("This page shows various examples of different charts relating to the data and how to read them, along with some insights that can be gained from looking at the data.")

fig = px.box(views)
fig.update_layout(
    xaxis_title="View Count",
    yaxis_title="Value"
)
st.plotly_chart(fig)
st.write("This box plot shows the summary statistics for the view counts of Mr Beast videos.. The plot is understood by looking at the five lines of the plot, being the minimum, first quartile, median, third quartile, and maximum from bottom to top. More information can be seen by hovering over the plot.") 
st.write("This data shows that the median amount of views of a Mr Beast video is about 49 million. There are a few significant values, although none seem to be outliers. One conclusion that can be drawn from this is that on average a video published by Mr Beast will get anywhere from about 14 to 81 million views.")

fig = px.histogram(df_sorted, x="viewCount", nbins=20, title="Counts of Starting Salaries")
fig.update_layout(
    xaxis_title="Number of Views",
    yaxis_title="Count"
)
st.plotly_chart(fig)
st.write("This histogram shows the number of videos that are in different ranges of number of views. The number of videos in each view range can be seen by correlating the count value on the left with the blocks of view counts at the bottom. More detailed information can be seen by hovering over the blocks.")
st.write("This data shows that most videos made by Mr Beast are in a right skewed data formation. The largest bin is from 0 to 9.9 million views, and the amount of views above 109.99 million views drops off significantly with much fewer videos surpassing this. This can be analyzed as the highest amount of views to be expected on an average video, and anything about around 109.99 million is a very well performing video.")

fig = px.scatter(df_sorted, x="duration_seconds", y="viewCount", title="Percent Salary Increase Based on Starting Salary")
fig.update_layout(
    xaxis_title="Video Duration",
    yaxis_title="Nunber of Views"
)
st.plotly_chart(fig)
st.write("This scatterplot shows the relationship between the duration of Mr Beast videos and the number of views on each video. This plot can be understood by correlating the number of views on the left with the video duration values at the bottom of the plot. More information can be seen by hovering over any given point.")
st.write("This data shows that there is a very standard video duration for the videos, and there is a slight correlation of number of views with the duration of the video. This trend changes for longer videos, with the six exceptions to the video length having lower numbers of views on average. Within the standard video range, it seems that the videos that perform the best are on average a maximum of about 1550 or less seconds, or about 25 minutes or less on average.")

fig = px.line(df_sorted, x="viewCount", y="likeCount", title="Upper Salary Limit Based On Starting Salary")
st.plotly_chart(fig)
fig.update_layout(
    xaxis_title="View Count",
    yaxis_title="Like Count"
)
st.write("This line chart shows the relationship between the view counts of different videos and the number of likes on each of the videos. This plot can be understood by correlating the number of likes on the left with the correlating view count on the bottom and seeing where they intersect on the line. More information can be seen by hovering over the line.")
st.write("This data shows that the like counts for a video tend to have a positive linear correlation with the view count of a video with a few notable outliers. Most videos tend to follow somewhat of a trend of 1 million likes per every 50 million views, however there is one extremely unusual statistic with 19 million likes for 96.5 million views. The other most significant statistic is 12.25 million likes for 178.75 million views.") 
