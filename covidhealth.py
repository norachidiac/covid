# Importing Libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
# Importing Dataset
df = pd.read_csv('state_wise.csv')
df_new = df.sort_values(by="Confirmed", ascending=False)
# Setting the title and sidebar title for the dashboard
st.title("Covid-19 Dashboard For India")
st.markdown('The dashboard will visualize the Covid-19 Situation in India through the years 2020 and 2021')
st.markdown('Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.')
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")


# Creating first Visualizations 
select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
if not st.sidebar.checkbox("Hide", True, key='1'):
    if select == 'Pie chart':
        st.title("Selected Top 5 States")
        fig = px.pie(df_new, values=df_new['Confirmed'][1:6], names=df_new['State'][1:6], title='Total Confirmed Cases 2020-2021')
        st.plotly_chart(fig)

    if select=='Bar plot':
        st.title("Selected Top 5 States")
        fig = go.Figure(data=[
        go.Bar(name='Confirmed', x=df_new['State'][1:6], y=df_new['Confirmed'][1:6]),
        go.Bar(name='Recovered', x=df_new['State'][1:6], y=df_new['Recovered'][1:6]),
        go.Bar(name='Active', x=df_new['State'][1:6], y=df_new['Active'][1:6])])
        st.plotly_chart(fig)
# For this part, another dataset was used which contains the number of cases according to the date   
df2 = pd.read_csv('case_time_series.csv')
df2['Date'] =  df2['Date'].astype('datetime64[ns]')
# Configuring 2 options for the sidebar (Confirmed Cases and Recovered Cases) depending which one the user clicks
select1 = st.sidebar.selectbox('Select', ['Confirmed Cases', 'Recovered Cases'], key='2')
if not st.sidebar.checkbox("Hide", True, key='2'):
    if select1 == 'Confirmed Cases':
        fig = px.line(df2, x="Date", y="Total Confirmed")
        st.plotly_chart(fig)
    elif select1 == 'Recovered Cases':
        fig = px.line(df2, x="Date", y="Total Recovered")
        st.plotly_chart(fig)
# Configuring 2 options for the sidebar (Daily Deceased and Recovered) depending which one the user clicks
select2 = st.sidebar.selectbox('Select', ['Daily Deceased', 'Daily Recovered'], key='2')
if not st.sidebar.checkbox("Hide", True, key='4'):
    if select2 == 'Daily Deceased':
         fig = px.area(df2, x="Date", y="Daily Deceased")
         st.plotly_chart(fig)
    elif select2 == 'Daily Recovered':
        fig = px.area(df2, x="Date", y="Daily Recovered")
        st.plotly_chart(fig)

   
