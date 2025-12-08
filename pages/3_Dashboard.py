import streamlit as st
import pandas as pd
import plotly.express as px
import os

data_path = os.path.join(os.getcwd(), "data", "MrBeast_youtube_stats.csv")
df = pd.read_csv(data_path)

st.title("Mr Beast Video Analytics")
st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

chart_visual = st.sidebar.selectbox('Select Charts/Plot type', ('Line Chart', 'Bar Chart', 'Bubble Chart'))
st.sidebar.checkbox("Show Analysis by View Count", True, key=1)

selected_status = st.sidebar.selectbox('Select View Values', options=['Less than 100M', 'Less than 50M', 'Less than 25m'])
