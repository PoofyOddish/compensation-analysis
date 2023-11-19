import streamlit as st
import pandas as pd
import numpy as np

# import viz_utility as vutil
import altair as alt

st.set_page_config(
    page_title="Peer Support Analysis",
    page_icon="🧑‍🤝‍🧑",
)

st.title("Peer Support Analysis")

st.markdown(
    """
    Howdy there 🤠  
    Welcome to a half-baked Peer Support analysis  *(fueled by [Streamlit](https://streamlit.io))*   
    *definitely not created by JB because they have a life and hobbies and stuff outside of data probably...*

    ### 👈 Click on the links to the left to navigate through different analysis views
    Market Analysis: A text comparison of recent Peer Support Specialist job postings in Colorado  
    NPI Lookup: A quick search of active NPIs in Colorado with the Peer Support taxonomy

    ### Half-baked insights so far
    * 💸 Jobs that require a certification seem to correlate with higher hourly wages
    * 🏫 Entry level peer specialist (Peer Specialist 1) do not require a certification as often as Peer Specialist 2 and Peer Specialist Coach roles
    * ⏫ Looks like there are 450+ individuals that may be registered with NPI numbers to offer peer support services
    * 🚇 There is a high clustering of NPIs that use peer support taxonomies in Grand Junction and Greeley

    ### Additional research opportunities
    * 🤔 Interested in regional demand for certification - does Metro Denver have a higher demand for peer certification vs. rural/frontier locations?
    * 😭 Would have been interesting to dig into OEWC data, but figured I should do some homework this weekend
    * 💵 Curious how wages for Peer Specialist role compare in Denver vs. outside of Denver vs. outside of Colorado
"""
)

