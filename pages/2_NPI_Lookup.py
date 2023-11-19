import streamlit as st
import pandas as pd
import numpy as np

# import viz_utility as vutil
import altair as alt

@st.cache_data
def load_data():
    data = pd.read_csv("npi_data.csv")
    return data

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

#Load in data
data = load_data()

st.markdown(
"""
### View active NPIs with Peer Specialist taxonomy
"""
)

st.metric(label="Number of active individual NPIs", value=data[data.enumeration_type == 'NPI-1'].shape[0])
st.metric(label="Number of active organization NPIs", value=data[data.enumeration_type == 'NPI-2'].shape[0])

st.markdown(
"""
#### Map of active NPIs based on mailing zipcode
Mapping is hard - this is just to get a sense of the distribution of peer support specialists in CO
"""
)
mapping = data[['enumeration_type','lat','lon','number']].groupby(['enumeration_type','lat','lon']).count().reset_index()
mapping['number']=mapping['number']*100

st.map(mapping,size='number')

st.markdown(
"""
#### Barchart of active NPIs based on mailing city  
NPI-1: Individual  
NPI-2: Organization
"""
)
city_count = data[['enumeration_type','mailing_city','number']].groupby(['enumeration_type','mailing_city']).count().reset_index()

st.bar_chart(city_count,x='mailing_city',y='number',color='enumeration_type')

st.markdown(
"""
#### Raw NPI data
"""
)

csv = convert_df(data)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='wfd-analysis-npi.csv',
    mime='text/csv',
)
