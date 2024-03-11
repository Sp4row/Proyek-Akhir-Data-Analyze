import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')


#Load Data
data_df= pd.read_csv('./Data/PRSA_Data_Dongsi_20130301-20170228.csv')
data_df.head()

#Titles
st.set_page_config(page_title="Air Quality Dongsi by Ariajuna")
st.title('Air Quality Anlysis Dashboard : Dongsi Station')

#Description
st.write('Welcome to this dashboard where we provide interactive ways to explore the air quality data. We center it down to the data of PM(PM2.5 and PM10) and their corelation between others parameters')

#Sidebar
st.sidebar.header('Data Filter')
year_filter = st.sidebar.selectbox('Year', list(data_df['year'].unique()))
month_filter = st.sidebar.selectbox('Month', list(data_df['month'].unique()))

data_filtered = data_df[(data_df['year']==year_filter) & (data_df['month']==month_filter)].copy()

#main
st.subheader('Data Overview selected by Filter')
st.write(data_filtered.describe())

#Linechart bulanan
st.subheader('Daily PM levels')
col1, col2 = st.columns(2)
with col1:
    fig, ax1 =plt.subplots()
    ax1.plot(data_filtered['day'], data_filtered['PM2.5'])
    plt.xlabel('Days')
    plt.ylabel('PM2.5')
    st.pyplot(fig)

with col2:
    fig, ax2 =plt.subplots()
    ax2.plot(data_filtered['day'], data_filtered['PM10'])
    plt.xlabel('Days')
    plt.ylabel('PM10')
    st.pyplot(fig)

#Heatmap Polutan dengan Envinroment
st.subheader('Correlation Heatmap of Polutan w/ Envinroment')
corr_matrix = data_filtered[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'RAIN']].corr()
fig, ax =plt.subplots()
sns.heatmap(corr_matrix, annot=True, ax=ax)
plt.title('Correlation Heatmap')
st.pyplot(fig)

#Trend Bulanan
col3, col4 = st.columns(2)
with col3:
    st.subheader('Seasonal Trend')
    trend = data_df.groupby('month')['PM2.5'].mean()
    fig, ax =plt.subplots()
    trend.plot(kind='bar', ax=ax)
    plt.xlabel('Month')
    plt.ylabel('PM2.5')
    st.pyplot(fig)

with col4:
    st.subheader('Seasonal Trend')
    trend = data_df.groupby('month')['PM10'].mean()
    fig, ax =plt.subplots()
    trend.plot(kind='bar', ax=ax)
    plt.xlabel('Month')
    plt.ylabel('PM10')
    st.pyplot(fig)

#Polutan vs Rain
st.subheader('Polutan reacts to Rain')
polutan = st.selectbox('select pollutant', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'])
fig, ax =plt.subplots()
sns.scatterplot(
    x='RAIN',
    y=polutan, 
    data=data_filtered,
    ax=ax
)
st.pyplot(fig)

#Kesimpulan
st.subheader('Conclusion')
st.write("""
+ dashboard provides an interactive analysis of air quality data
+ The correlation heatmap shows the relationship between different environmental condition (Temperature, Rainfall)
+ Users may explore the data by selecting specific parameters such as date range  
""")

st.caption('Copyright (c) Sp4row 2024')
