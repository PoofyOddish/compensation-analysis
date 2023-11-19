import streamlit as st
import pandas as pd
import numpy as np

# import viz_utility as vutil
import altair as alt

@st.cache_data
def load_data():
    data = pd.read_csv("full_output.csv")
    return data

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


#Load in data
data = load_data()

data['min_transformed']=data['salary_min']
data.loc[data['pay_type']=='Annual', 'min_transformed'] = data['salary_min'].astype('float')/(52*40)

data['max_transformed']=data['salary_max']
data.loc[data['pay_type']=='Annual', 'max_transformed'] = data['salary_max'].astype('float')/(52*40)


st.markdown(
"""
### View distribution of current Peer Specialist jobs
"""
)

st.metric(label="Number of JDs included in analysis", value=data.shape[0])

ch = (
        alt.Chart(data)
        .mark_circle(size=50)
        .encode(alt.X("min_transformed",title="Minimum Salary (Hourly)"), alt.Y("max_transformed",title="Maximum Salary (Hourly)"), text="requirements")
        .encode(alt.Color("requirements"),tooltip=["job_title", "org_name", "url","requirements","min_transformed","max_transformed","college_required"])
        .properties(height=250)
        .interactive()
    )

bars = (
        alt.Chart(data)
        .mark_bar()
        .encode(
            alt.X("min_transformed",title="Minimum Salary").bin(),
            alt.Y("count()",title="Count of Jobs"),
            alt.Color("requirements",title="Requirements"),
            text="requirements",
            tooltip=["job_title", "org_name", "url","requirements","min_transformed","max_transformed","college_required"]
        )
        .properties(height=100)
        .interactive()
        
    )


chart = alt.vconcat(ch, bars)

st.altair_chart(chart, use_container_width=True)

## Download data
csv = convert_df(data[["job_title", "org_name", "url","requirements","min_transformed","max_transformed"]])

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='wfd-analysis-market-analysis.csv',
    mime='text/csv',
)