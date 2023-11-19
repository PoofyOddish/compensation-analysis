import streamlit as st
import pandas as pd
import numpy as np

# import viz_utility as vutil
import altair as alt

@st.cache_data
def load_data():
    data = pd.read_csv("npi_data.csv")
    return data


#Load in data
data = load_data()

st.table(data)
