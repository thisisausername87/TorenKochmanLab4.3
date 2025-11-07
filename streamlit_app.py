import streamlit as st
import pandas as pd
import plotly.express as px

data_path = os.path.join(os.getcwd(), "data", "degrees_that_pay_back.csv")
df = pd.readcsv(data_path)
df
