import streamlit as st
import pandas as pd
import numpy as np
st.title('Machine Learning App: Diabetes Predict')
st.info('Hello')

with st.expander('Dataset'):
  st.write('**Raw Data**')
  st.write('This Dataset from : https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset')
  df = pd.read_csv('diabetes_prediction_dataset.csv')
  df

  st.write('**X**')
  X_raw = df.drop('diabetes',axis=1)
  X_raw

  st.write('**y**')
  y_raw = df['diabetes']
  y_raw

#with st.expander('EDA'):
    

with st.sidebar:
  st.header('Input Features')
  gender = st.selectbox('Gender',{'Male','Female'})
  age = st.slider('Age',0,100,30)
  hypertension = st.selectbox('Hypertension',{'Yes','No'})
  heart_disease = st.selectbox('Heart Disease',{'Yes','No'})
  smoking_history = st.selectbox('Smoking History',{'Never','Current','Former'})
  bmi = st.slider('BMI',0,50,25)
  HbA1c_level = st.slider('HbA1c Level',0,10,5)
  blood_glucose_level = st.slider('Blood Glucose Level',50,400,100)
