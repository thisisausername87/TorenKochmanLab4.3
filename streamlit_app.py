import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- FUNCTIONS ----------
@st.cache_data
def load_data():
    data_path = os.path.join(os.getcwd(), "data", "degrees_that_pay_back.csv")
    df = pd.read_csv(data_path)
    for col in df.columns:
        if df[col].dtype == 'object' and df[col].str.contains(r'\$').any():
            df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)
    return df

def salary_kpis(df):
    top_major = df.loc[df["Mid-Career Median Salary"].idxmax(), "Undergraduate Major"]
    top_salary = df["Mid-Career Median Salary"].max()
    avg_salary = df["Mid-Career Median Salary"].mean()
    growth = df["Percent change from Starting to Mid-Career Salary"].mean()
    return top_major, top_salary, avg_salary, growth

# ---------- MAIN APP ----------
st.set_page_config(page_title="Undergraduate Salary Dashboard", layout="wide")

st.title("🎓 Undergraduate Major Salary Dashboard")
df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
selected_majors = st.sidebar.multiselect(
    "Select Majors", options=df["Undergraduate Major"], default=df["Undergraduate Major"]
)
metric = st.sidebar.selectbox(
    "Choose Metric", 
    ["Starting Median Salary", "Mid-Career Median Salary", "Percent change from Starting to Mid-Career Salary"]
)
growth_filter = st.sidebar.slider(
    "Filter by Percent Growth", 
    min_value=0.0, max_value=150.0, value=(0.0, 150.0)
)

# Apply filters
filtered_df = df[df["Undergraduate Major"].isin(selected_majors)]
filtered_df = filtered_df[
    (filtered_df["Percent change from Starting to Mid-Career Salary"] >= growth_filter[0]) &
    (filtered_df["Percent change from Starting to Mid-Career Salary"] <= growth_filter[1])
]

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Growth Analysis", "Salary Distribution", "About"])

# ---------- TAB 1: OVERVIEW ----------
with tab1:
    st.subheader("📊 Overview")
    top_major, top_salary, avg_salary, avg_growth = salary_kpis(df)
    col1, col2, col3 = st.columns(3)
    col1.metric("Highest Paying Major", top_major, f"${top_salary:,.0f}")
    col2.metric("Avg Mid-Career Salary", f"${avg_salary:,.0f}")
    col3.metric("Avg % Growth", f"{avg_growth:.1f}%")

    fig = px.bar(
        filtered_df,
        x="Undergraduate Major",
        y=["Starting Median Salary", "Mid-Career Median Salary"],
        title="Starting vs Mid-Career Median Salary",
        barmode="group"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.info("💡 **Insight:** Engineering majors tend to start higher and maintain strong mid-career growth, while humanities show slower but steady increases.")

# ---------- TAB 2: GROWTH ANALYSIS ----------
with tab2:
    st.subheader("📈 Salary Growth Analysis")
    fig = px.scatter(
        filtered_df,
        x="Starting Median Salary",
        y="Mid-Career Median Salary",
        size="Percent change from Starting to Mid-Career Salary",
        color="Percent change from Starting to Mid-Career Salary",
        hover_name="Undergraduate Major",
        title="Percent Growth from Starting to Mid-Career Salary",
        color_continuous_scale="viridis"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.caption("Alt text: Scatter plot showing relationship between starting and mid-career salaries, with bubble size representing percent growth.")

# ---------- TAB 3: SALARY DISTRIBUTION ----------
with tab3:
    st.subheader("📊 Salary Distribution by Percentile")
    percentiles = [
        "Mid-Career 10th Percentile Salary",
        "Mid-Career 25th Percentile Salary",
        "Mid-Career 75th Percentile Salary",
        "Mid-Career 90th Percentile Salary"
    ]
    df_melted = filtered_df.melt(id_vars="Undergraduate Major", value_vars=percentiles,
                                 var_name="Percentile", value_name="Salary")
    fig = px.line(df_melted, x="Undergraduate Major", y="Salary", color="Percentile", markers=True)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Alt text: Line chart showing salary distribution across mid-career percentiles for selected majors.")

# ---------- TAB 4: ABOUT ----------
with tab4:
    st.markdown("""
    ### ℹ️ About This Dashboard
    - **Data Source:** CSV file hosted on GitHub  
    - **Purpose:** Visualize and compare salary trajectories by undergraduate major  
    - **Built with:** Streamlit + Plotly  
    - **Insights Panel:** Helps identify which majors yield higher long-term returns  
    """)
