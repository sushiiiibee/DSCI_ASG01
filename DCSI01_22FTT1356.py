import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt 


st.set_page_config(layout="wide")

df = pd.read_csv('jobs_in_data.csv')


def home_page():
    columns = st.columns([3, 1, 2])  
    title_col = columns[0]

    title_col.title(" :female-technologist: JOBS IN DATA")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

    st.write('DATA SCIENCE')
    st.write('Nur Afifah Nabilah Binti Ahmad Yani')
    st.write('22FTT1356')
    st.write('DDAS02')
    

def main_dashboard():
    columns = st.columns([3, 1, 2])  
    title_col = columns[0]

    title_col.title(" :female-technologist: JOBS IN DATA")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

    figsize_bar = (12, 8.5)
    figsize_line = (10, 6)
    figsize_pie = (10, 6)


    # Visualization 01
    with st.expander("Salary based on Job Title"):
        plt.figure(figsize=figsize_bar)
        selected_titles = st.multiselect("Select title:", df["job_title"].unique())

        st.write('')
        col1, col2 = st.columns(2)

        with col1:
            year = st.radio("Year 01", df["work_year"].unique())

        with col2:
            location = st.selectbox("Location 01", df["company_location"].unique())

        if selected_titles: 
            filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location) & (df['job_title'].isin(selected_titles))]
        else:  
            filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location)]

        if not filtered_df.empty:
            top_job_title = filtered_df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(10)
            sns.barplot(y=top_job_title.index, x=top_job_title.values)
            plt.xlabel('Salary') 
            plt.ylabel('Job Title')
            plt.grid(True, alpha=0.3)
            st.pyplot(plt)
            plt.close()
        else:
            st.write("No data available for the selected filters!")



    # Visualization 02
    with st.expander("Salary based on Job Category"):
        plt.figure(figsize=figsize_bar)
        selected_category = st.multiselect("Select Categories:", df["job_category"].unique())

        st.write('')
        col1, col2 = st.columns(2)

        with col1:
            year = st.radio("Year 02", df["work_year"].unique())

        with col2:
            location = st.selectbox("Location 02", df["company_location"].unique())

        if selected_titles: 
            filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location) & (df['job_category'].isin(selected_category))]
        else:  
            filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location)]

        if not filtered_df.empty:
            job_category = filtered_df.groupby('job_category')['salary_in_usd'].mean().sort_values(ascending=False)
            sns.barplot(y=job_category.index, x=job_category.values)
            plt.xlabel('Salary')  
            plt.ylabel('Job Category')
            plt.grid(True, alpha=0.3)
            st.pyplot(plt)
            plt.close()
        else:
            st.write("No data available for the selected filters!")

    # Visualization 03
    with st.expander("Salary based on Entry Level"):
        plt.figure(figsize=figsize_line)
        selected_experience_level = st.multiselect("Select Entry Level:", df["experience_level"].unique())

        st.write('')
        col1, col2 = st.columns(2)

        with col1:
            year = st.radio("Year 03", df["work_year"].unique())

        with col2:
            location = st.selectbox("Location 03", df["company_location"].unique())

        if selected_titles: 
            filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location) & (df['experience_level'].isin(selected_experience_level))]
        else:  
            filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location)]

        if not filtered_df.empty:
            experience_level = filtered_df.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=False)
            sns.lineplot(x=experience_level.index, y=experience_level.values) 
            plt.xlabel('Experience Level')
            plt.ylabel('Salary')
            plt.grid(True, alpha=0.3)
            st.pyplot(plt)
            plt.close()
        else:
            st.write("No data available for the selected filters!")

    # Visualization 04
    with st.expander("Salary based on Work Setting"):
        plt.figure(figsize=figsize_line)
        selected_work_setting = st.multiselect("Select Work Setting:", df["work_setting"].unique())

        st.write('')
        col1, col2 = st.columns(2)

        with col1:
            year = st.radio("Year 04", df["work_year"].unique())

        with col2:
            location = st.selectbox("Location 04", df["company_location"].unique())

        if selected_titles: 
            filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location) & (df['work_setting'].isin(selected_work_setting))]
        else:  
            filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location)]

        if not filtered_df.empty:
            work_setting_salary = filtered_df.groupby('work_setting')['salary_in_usd'].mean().sort_values(ascending=False)
            sns.lineplot(x=work_setting_salary.index, y=work_setting_salary.values) 
            plt.xlabel('Work Setting')
            plt.ylabel('Salary')
            plt.grid(True, alpha=0.3)
            st.pyplot(plt)
            plt.close()
        else:
            st.write("No data available for the selected filters!")

    # Visualization 05
    with st.expander("Salary based on Employment Type"):
        plt.figure(figsize=figsize_pie)
        selected_employment_type = st.multiselect("Select Employment type:", df["employment_type"].unique())

        st.write('')
        col1, col2 = st.columns(2)

        with col1:
            year = st.radio("Year 05", df["work_year"].unique())

        with col2:
            location = st.selectbox("Location 05", df["company_location"].unique())

        if selected_titles: 
            filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location) & (df['work_year'].isin(selected_work_year))]
        else:  
            filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location)]

        if not filtered_df.empty:
            employment_type_salary = filtered_df.groupby('employment_type')['salary_in_usd'].mean().sort_values(ascending=False)
            plt.pie(employment_type_salary.values, labels=employment_type_salary.index, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            st.pyplot(plt)
            plt.close()
        else:
            st.write("No data available for the selected filters!")

    # Visualization 06
    with st.expander("Salary based on Company Size"):
        plt.figure(figsize=figsize_pie)
        selected_company_size = st.multiselect("Select Company Size:", df["company_size"].unique())

        st.write('')
        col1, col2 = st.columns(2)

        with col1:
            year = st.radio("Year 06", df["work_year"].unique())

        with col2:
            location = st.selectbox("Location 06", df["company_location"].unique())

        if selected_titles: 
            filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location) & (df['company_size'].isin(selected_company_size))]
        else:  
            filtered_df = df[(df['work_year'] == year) & (df['company_location'] == location)]

        if not filtered_df.empty:
            company_size_salary = filtered_df.groupby('company_size')['salary_in_usd'].mean().sort_values(ascending=False)
            plt.pie(company_size_salary.values, labels=company_size_salary.index, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            st.pyplot(plt)
            plt.close()
        else:
            st.write("No data available for the selected filters!")




def other_dashboard():
    columns = st.columns([3, 1, 2])  
    title_col = columns[0]

    title_col.title(" :female-technologist: JOBS IN DATA")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

    figsize_bar = (12, 8.5)
    figsize_line = (10, 6)
    figsize_pie = (10, 6)

    # Visualization 01
    with st.expander("Job Categories Distribution"):
        plt.figure(figsize=figsize_bar)
        selected_categories = st.multiselect("Select job categories", df["job_category"].unique())

        if selected_categories:
            filtered_df = df[df['job_category'].isin(selected_categories)]
            sns.countplot(data=filtered_df, y='job_category', order=filtered_df['job_category'].value_counts().index)
            plt.xlabel('Count')
            plt.ylabel('Job Category')
            plt.grid(True, alpha=0.3)
            st.pyplot(plt)
            plt.close()
        else:
            st.write("")

    # Visualization 02
    with st.expander("Job Title Distribution"):
        plt.figure(figsize=figsize_bar)
        top_10_job_titles = df['job_title'].value_counts().head(10).index
        selected_titles = st.multiselect("Select job titles", top_10_job_titles)

        if selected_titles:
            filtered_df = df[df['job_title'].isin(selected_titles)]
            sns.countplot(data=filtered_df, y='job_title', order=selected_titles)
            plt.xlabel('Count')
            plt.ylabel('Job Title')
            plt.grid(True, alpha=0.3)
            st.pyplot(plt)
            plt.close()
        else:
            st.write("")

    # Visualization 03
    with st.expander("Experience Level Distribution"):
        plt.figure(figsize=figsize_line)
        selected_experience_levels = st.multiselect("Select experience levels", df["experience_level"].unique())

        if selected_experience_levels:
            filtered_df = df[df['experience_level'].isin(selected_experience_levels)]
            experience_level_counts = filtered_df['experience_level'].value_counts()
            experience_level_counts = experience_level_counts.sort_index()
            experience_level_counts.plot(kind='line', marker='o', color='blue')
            plt.xlabel('Experience Level')
            plt.ylabel('Count')
            plt.grid(True, alpha=0.3)
            st.pyplot(plt)
            plt.close()
        else:
            st.write("")

    # Visualization 04
    with st.expander("Work Setting Distribution"):
        plt.figure(figsize=figsize_line)
        selected_work_settings = st.multiselect("Select work settings", df["work_setting"].unique())

        if selected_work_settings:
            filtered_df = df[df['work_setting'].isin(selected_work_settings)]
            work_setting_counts = filtered_df['work_setting'].value_counts()
            work_setting_counts = work_setting_counts.sort_index()
            work_setting_counts.plot(kind='line', marker='o', color='blue')
            plt.xlabel('Work Setting')
            plt.ylabel('Count')
            plt.grid(True, alpha=0.3)
            st.pyplot(plt)
            plt.close()
        else:
            st.write("")

    # Visualization 05
    with st.expander("Employment Type Distribution"):
        plt.figure(figsize=figsize_line)
        selected_employment_types = st.multiselect("Select employment types", df["employment_type"].unique())

        if selected_employment_types:
            filtered_df = df[df['employment_type'].isin(selected_employment_types)]
            employment_type_counts = filtered_df['employment_type'].value_counts()
            employment_type_counts = employment_type_counts.sort_index()
            employment_type_counts.plot(kind='line', marker='o', color='blue')
            plt.xlabel('Employment Type')
            plt.ylabel('Count')
            plt.grid(True, alpha=0.3)
            st.pyplot(plt)
            plt.close()
        else:
            st.write("")

    # Visualization 06
    with st.expander("Company Size Distribution"):
        plt.figure(figsize=figsize_pie)
        selected_company_sizes = st.multiselect("Select company sizes", df["company_size"].unique())

        if selected_company_sizes:
            filtered_df = df[df['company_size'].isin(selected_company_sizes)]
            company_size_counts = filtered_df['company_size'].value_counts()
            plt.pie(company_size_counts, labels=company_size_counts.index, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            st.pyplot(plt)
            plt.close()
        else:
            st.write("")

pages = {
    "Data Science": home_page,
    "Main Dashboard": main_dashboard,
    "Other Dashboard": other_dashboard
}

selection = st.sidebar.radio("JOBS IN DATA:", list(pages.keys()))

pages[selection]()
