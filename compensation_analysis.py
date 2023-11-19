import streamlit as st
import pandas as pd
import numpy as np

# import viz_utility as vutil
import altair as alt

st.set_page_config(
    page_title="Peer Support Analysis",
    page_icon="💰",
)

st.title("Peer Support Analysis")

st.markdown(
    """
    Howdy there 🤠  
    Welcome to a half-baked Peer Support analysis  *(fueled by [Streamlit](https://streamlit.io))*   
    definitely not created by JB because they have a life and hobbies and stuff outside of data probably

    ### Click on the links to the left to navigate through different analysis views
    #### Market Analysis: A text comparison of recent Peer Support Specialist job postings in Colorado
    #### NPI Lookup: A quick search of active NPIs in Colorado with the Peer Support taxonomy
"""
)

