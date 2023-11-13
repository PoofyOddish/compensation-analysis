import streamlit as st
import pandas as pd
import numpy as np

# import viz_utility as vutil
import altair as alt

st.set_page_config(
    page_title="Director Compensation Analysis",
    page_icon="💰",
)

st.title("Director Compensation Analysis")

st.markdown(
    """
    Howdy there 🤠  
    Welcome to JB's Director of Data Science compensation analysis  *(fueled by [Streamlit](https://streamlit.io))*   
    ### Want to learn more?
    - 🤖 [Meet the dev](http://www.jordan-serna.com) behind this analysis
"""
)


@st.cache_data
def load_data():
    data = pd.read_csv("full_output.csv")
    return data


#Load in data
data = load_data()

#Define bigram data to load in
domains = [
    ("data_science", "Data Science"),
    ("data_engineering", "Data Engineering"),
    ("database_design", "Database Design"),
    ("data_analysis", "Data Analysis"),
    ("collaborate_stakeholders", "Collaboration with Stakeholders"),
    ("data_quality", "Data Quality"),
    ("strong_communication", "Strong Communication"),
    ("communication_skills", "Communication Skills"),
    ("data_pipelines", "Data Pipelines"),
    ("unstructured_data", "Unstructured Data"),
    ("data_lake", "Data Lake"),
    ("data_model", "Data Modeling"),
    ("data_scientist", "Data Scientist"),
    ("data_requirements", "Data Requirements"),
    ("team_management", "Team Management"),
    ("data_manipulation", "Data Manipulation"),
    ("data_warehouse", "Data Warehousing"),
    ("machine_learning", "Machine Learning"),
]

#Iterate through bigram domains and create charts as relevant
for i in range(0, len(domains)):
    with st.expander(domains[i][1]):
        domain_data = data[data[domains[i][0]] == 1][
            ["job_title", "org_name", "salary_min", "salary_max", "tokens", "JobType"]
        ]

        jd_db = domain_data[domain_data.job_title != "Director of Data Science"]
        director = domain_data[domain_data.job_title == "Director of Data Science"]
        # print(director)

        ch = (
            alt.Chart(jd_db)
            .mark_circle(size=50)
            .encode(alt.X("salary_min",title="Minimum Salary"), alt.Y("salary_max",title="Maximum Salary"), text="JobType")
            .encode(alt.Color("JobType"))
            .properties(title=domains[i][1],height=250)
            .interactive()
        )

        annotation_layer = (
            alt.Chart(director)
            .mark_text(size=20, text="⭐", dx=-8, dy=-10, align="left")
            .encode(x="salary_min", y="salary_max")
            .interactive()
        )
        bars = (
            alt.Chart(domain_data)
            .mark_bar()
            .encode(
                alt.X("salary_min",title="Minimum Salary").bin(),
                alt.Y("count()",title="Count of Jobs"),
                alt.Color("JobType",title="Type of Role"),
                text="JobType",
            )
            .properties(height=100)
            .interactive()
            
        )
        annotation_layer_bars = (
            alt.Chart(director)
            .mark_text(size=20, text="⭐", dx=-8, dy=-10, align="left")
            .encode(x="salary_min", y="count()")
            .interactive()
        )

        chart = alt.vconcat(ch + annotation_layer, bars+annotation_layer_bars)

        st.altair_chart(chart, use_container_width=True)

        st.divider()