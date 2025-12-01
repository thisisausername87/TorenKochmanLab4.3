import streamlit as st
import pandas as pd
import plotly.express as px

data_path = os.path.join(os.getcwd(), "data", "degrees_that_pay_back.csv")
df = pd.read_csv(data_path)
df_sorted = df.sort_values(by="Starting Median Salary")

fig = px.bar(df_sorted, x="Undergraduate Major", y="Starting Median Salary", title="Starting Salary by Major")
fig.show()

fig = px.histogram(df_sorted, x="Starting Median Salary", nbins=20, title="Counts of Starting Salaries")
fig.update_layout(
    xaxis_title="Starting Median Salary",
    yaxis_title="Count"
)
fig.show()

fig = px.scatter(df_sorted, x="Starting Median Salary", y="Percent change from Starting to Mid-Career Salary", title="Percent Salary Increase Based on Starting Salary")
fig.update_layout(
    xaxis_title="Starting Median Salary",
    yaxis_title="Salary Percent Increase"
)
fig.show()

fig = px.line(df_sorted, x="Starting Median Salary", y="Mid-Career 90th Percentile Salary", title="Upper Salary Limit Based On Starting Salary")
fig.show()
