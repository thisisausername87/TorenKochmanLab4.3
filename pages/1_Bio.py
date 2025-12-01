import streamlit as st

st.title("My Bio")

INTRO = "My name is Toren and I am a computer science major at MSU Denver. I take interest in having a greater understanding of the world around me and being able to navigate the complexities that I see around me every day. While some of my main hobbies are video games and other online media, I also have a strong interest in mathematics and sciences which is where I tend to focus my studies."
TOOLS = "I utilize python along with various libraries such as Pandas, MatPlotLib, and Plotly to name a few in order to analyze data files into easily understandable and accessible interpretations of their contents."
VIEWS = "When visualizing data, I believe that it is always best to have the most accurate and well conceptualized data and interpretations possible so that the most truthful possible understandings can be drawn from a strong analysis of information."

st.write(INTRO)
st.write(TOOLS)
st.write(VIEWS)
