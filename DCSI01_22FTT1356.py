# Main dashboard 

import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt 

st.set_page_config(layout="wide")

df = pd.read_csv('jobs_in_data.csv')

title_col, year_col, location_col = st.columns([3, 1, 2])  

title_col.title(" :female-technologist: JOBS IN DATA")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

with year_col:
    year = st.selectbox("Choose a year", df["work_year"].unique())

with location_col:
    location = st.selectbox("Choose a location", df["company_location"].unique())

col1, col2, col3 = st.columns((3))

filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location)]

figsize_bar = (12, 8.5)
figsize_line = (10, 6)
figsize_pie = (10, 6)

with col1:
    plt.figure(figsize=figsize_bar)
    top_job_title = filtered_df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(10)
    sns.barplot(y=top_job_title.index, x=top_job_title.values)
    plt.xlabel('Salary') 
    plt.ylabel('Job Title')
    plt.grid(True, alpha=0.3)
    st.pyplot(plt)
    plt.close()

with col1:
    plt.figure(figsize=figsize_bar)
    job_category = filtered_df.groupby('job_category')['salary_in_usd'].mean().sort_values(ascending=False)
    sns.barplot(y=job_category.index, x=job_category.values)
    plt.xlabel('Salary')  
    plt.ylabel('Job Category')
    plt.grid(True, alpha=0.3)
    st.pyplot(plt)
    plt.close()

with col2:
    plt.figure(figsize=figsize_line)
    experience_level = filtered_df.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False)
    sns.lineplot(x=experience_level.index, y=experience_level.values) 
    plt.xlabel('Experience Level')
    plt.ylabel('Salary')
    plt.grid(True, alpha=0.3)
    st.pyplot(plt)
    plt.close()

with col2:
    plt.figure(figsize=figsize_line)
    work_setting = filtered_df.groupby('work_setting')['salary_in_usd'].mean().sort_values(ascending=False)
    sns.lineplot(x=work_setting.index, y=work_setting.values) 
    plt.xlabel('Work_Setting')
    plt.ylabel('Salary')
    plt.grid(True, alpha=0.3)
    st.pyplot(plt)
    plt.close()

with col3:
    plt.figure(figsize=figsize_pie)
    experience_level = filtered_df.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False)
    plt.pie(experience_level.values, labels=experience_level.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    st.pyplot(plt)
    plt.close()

with col3:
    plt.figure(figsize=figsize_pie)
    company_size = filtered_df.groupby('company_size')['salary_in_usd'].mean().sort_values(ascending=False)
    plt.pie(company_size.values, labels=company_size.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    st.pyplot(plt)
    plt.close()