import streamlit as st
# run in terminal
# cd data analysis
# streamlit run dapp.py

import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns

st.set_page_config(layout="centered")

pd.set_option('display.precision', 2)

# title of the app
st.title('Data Analysis App')

st.cache_data()
def load_data():
    df = sns.load_dataset('titanic')
    return df

with st.spinner('Loading Data...'):
    df = load_data()
    st.write("🎉🎉🎉")

cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()
num_cols = df.select_dtypes(include=np.number).columns.tolist()
if st.checkbox("View All Data"):
    st.dataframe(df)

if st.checkbox("Show Some Statistics"):
   
    c1, c2 = st.columns(2)
    c1.metric(label="Average Age of Passengers", 
              value=df['age'].mean().astype(int))
    c2.metric(label="Average Fare", 
              value=df['fare'].mean().astype(int), 
              delta=round(df['fare'].std(),1))
    
    c1, c2 = st.columns(2)
    c1.text("Number of Survivors")
    survivors = df['survived'].value_counts()
    c1.dataframe(survivors)
    fig = px.pie(survivors, survivors.index, survivors.values)
    c1.plotly_chart(fig, use_container_width=True)
    c2.text("Number of Passengers in Each Class")
    classes = df['pclass'].value_counts()
    c2.dataframe(classes)
    fig = px.bar(classes, classes.index, classes.values)
    c2.plotly_chart(fig, use_container_width=True)

if st.checkbox("visualize categorical data"):
    st.subheader("Categorical Data Visualization")
    sel_col = st.radio("Select Column", cat_cols, horizontal=True)
    sel_col_count = df[sel_col].value_counts()
    fig = px.pie(sel_col_count, sel_col_count.index, 
                 sel_col_count.values, title=f"Distribution of {sel_col}")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("visualize numerical data"):
    graph_types = ['Area','Line','Histogram','Boxplot','Violinplot']
    st.subheader("Numerical Data Visualization")
    sel_col = st.selectbox("Select Column", num_cols)
    graph_type = st.radio("Select Graph Type", graph_types,
                            horizontal=True)
    if graph_type == graph_types[0]:
        fig = px.area(df, y=sel_col, title=f"Area Plot of {sel_col}")
        fig2 = px.histogram(df, x=sel_col, title=f"Histogram of {sel_col}")
        c1, c2 = st.columns(2)
        c1.plotly_chart(fig, use_container_width=True)
        c2.plotly_chart(fig2, use_container_width=True)
    if graph_type == graph_types[1]:
        fig = px.line(df, y=sel_col, title=f"Line Plot of {sel_col}")
        st.plotly_chart(fig, use_container_width=True)
    if graph_type == graph_types[2]:
        fig = px.histogram(df, x=sel_col, title=f"Histogram of {sel_col}")
        st.plotly_chart(fig, use_container_width=True)
    if graph_type == graph_types[3]:
        fig = px.box(df, x=sel_col, title=f"Boxplot of {sel_col}")
        st.plotly_chart(fig, use_container_width=True)
    if graph_type == graph_types[4]:
        fig = px.violin(df, x=sel_col, title=f"Violinplot of {sel_col}")
        st.plotly_chart(fig, use_container_width=True)
    