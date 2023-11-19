import streamlit as st
import pandas as pd
import numpy as np

# import viz_utility as vutil
import altair as alt

@st.cache_data
def load_data():
    data = pd.read_csv("full_output.csv")
    return data


#Load in data
data = load_data()

data['min_transformed']=data['salary_min']
data.loc[data['pay_type']=='Annual', 'min_transformed'] = data['salary_min'].astype('float')/(12*52*5*8)

data['max_transformed']=data['salary_max']
data.loc[data['pay_type']=='Annual', 'max_transformed'] = data['salary_max'].astype('float')/(12*52*5*8)


st.markdown(
"""
### View distribution of current Peer Specialist jobs
"""
)
ch = (
        alt.Chart(data)
        .mark_circle(size=50)
        .encode(alt.X("min_transformed",title="Minimum Salary"), alt.Y("max_transformed",title="Maximum Salary"), text="require_certification_before_hire")
        .encode(alt.Color("require_certification_before_hire"))
        .properties(height=250)
        .interactive()
    )

bars = (
        alt.Chart(data)
        .mark_bar()
        .encode(
            alt.X("min_transformed",title="Minimum Salary").bin(),
            alt.Y("count()",title="Count of Jobs"),
            alt.Color("require_certification_before_hire",title="Type of Role"),
            text="require_certification_before_hire",
        )
        .properties(height=100)
        .interactive()
        
    )


chart = alt.vconcat(ch, bars)

st.altair_chart(chart, use_container_width=True)
