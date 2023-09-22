import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd



def show_plots():
    df = pd.read_csv("/Users/kumarrohit/Desktop/Road-Accident-Severity/Road-Traffic-Accident-Prediciton/Dataset/Processed Data.csv")
    grouped_counts = df['TimeLine'].value_counts().reset_index()
    grouped_counts.columns = ['TimeLine', 'Count']

    fig = px.bar(grouped_counts, x='TimeLine', y='Count', title='No of accidents occured in each timeline',template='plotly_dark')
    fig.update_xaxes(title_text="Time of the day")
    fig.update_yaxes(title_text="Number of accidents")
    st.plotly_chart(fig)
    
    
    grouped_counts = df.groupby(['TimeLine','Day_of_week']).size().reset_index()
    grouped_counts.columns = ['TimeLine', 'Day_of_week', 'Number of Accidents']

    grouped_Df = pd.DataFrame(grouped_counts,columns=['TimeLine', 'Day_of_week', 'Number of Accidents'])
    
    fig = px.bar(grouped_Df, x='TimeLine', y='Number of Accidents', title='No of accidents occured in each timeline',template='plotly_dark',color='Day_of_week')
    fig.update_xaxes(title_text="Time of the day")
    fig.update_yaxes(title_text="Number of accidents")
    st.plotly_chart(fig)
    
    
    fig = go.Figure(go.Sunburst(
    labels=grouped_Df['TimeLine'] + ' - ' + grouped_Df['Day_of_week'],
    parents=[''] * len(grouped_Df),
    values=grouped_Df['Number of Accidents']
    ))

    fig.update_layout(title='Sunburst Chart of Accidents by Timeline and Day of Week')
    st.plotly_chart(fig)
    