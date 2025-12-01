import streamlit as st
import pandas as pd
import plotly.express as px
import os

data_path = os.path.join(os.getcwd(), "streamlit_CS", "data", "degrees_that_pay_back.csv")
df = pd.read_csv(data_path)
df_sorted = df.sort_values(by="Starting Median Salary")

st.title("Different Types of Charts")
st.subheader("This page shows various examples of different charts relating to the data and how to read them, along with some insights that can be gained from looking at the data.")

fig = px.bar(df_sorted, x="Undergraduate Major", y="Starting Median Salary", title="Starting Salary by Major")
st.plotly_chart(fig)
st.write("This bar graph shows the starting median salaries for each undergraduate major. The graph is understood by looking at the value on the left of the graph and correlating it with the major on the bottom under the bar.") 
st.write("This data shows that some of the highest paying majors are physicians assistant, chemical engineering, computer engineering, and electrical engineering. There are no outliers or otherwise unusual data points in the graph. One conclusion that can be found from the information is that STEM related majors that are more mathematically and scientifically technical tend to have higher paying positions as opposed to the more humanitarian jobs such as journalism and music.")

fig = px.histogram(df_sorted, x="Starting Median Salary", nbins=20, title="Counts of Starting Salaries")
fig.update_layout(
    xaxis_title="Starting Median Salary",
    yaxis_title="Count"
)
st.plotly_chart(fig)
st.write("This histogram shows the number of jobs that are in each starting median slary range. The number of jobs in each salary range can be seen by correlating the count value on the left with the blocks of salary ranges at the bottom. More detailed information can be seen by hovering over the blocks.")
st.write("This data shows that the vast majority of jobs have a starting median salary of below around 50k per year. Some of the most notable data points in the graph are the lowest and highest valued bins, with 3 jobs having a starting salary below 35k per year and only 1 job having a starting salary of above 70k per year. This distribution is heavily right skewed with most jobs having a starting salary in the range of about 35k to 45k.")

fig = px.scatter(df_sorted, x="Starting Median Salary", y="Percent change from Starting to Mid-Career Salary", title="Percent Salary Increase Based on Starting Salary")
fig.update_layout(
    xaxis_title="Starting Median Salary",
    yaxis_title="Salary Percent Increase"
)
st.plotly_chart(fig)

fig = px.line(df_sorted, x="Starting Median Salary", y="Mid-Career 90th Percentile Salary", title="Upper Salary Limit Based On Starting Salary")
st.plotly_chart(fig)
