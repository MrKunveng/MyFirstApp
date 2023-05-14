#packages

import streamlit as st
import pickle

Pregnancies = st.number_input(label='Tape your Pregnancies ')
st.write('your Pregnancies  is', Pregnancies )
Glucose = st.number_input(label='Tape youur Glucose')
st.write('your Glucose is', Glucose)
BloodPressure = st.number_input(label='Tape your iBloodPressure')
st.write('your BloodPressure is', BloodPressure)
SkinThickness = st.number_input(label='Tape your SkinThickness')
st.write('your SkinThickness is', SkinThickness)
Insulin = st.number_input(label='Tape your Insulin')
st.write('your Insulin is', Insulin)
BMI = st.number_input(label='Tape your BMI')
st.write('your BMI is', BMI)
DiabetesPedigreeFunction = st.number_input(label='Tape your DiabetesPedigreeFunction')
st.write('your DiabetesPedigreeFunction is', DiabetesPedigreeFunction)
Age = st.number_input(label='Tape your Age')
st.write('your Age is', Age)

xtest= [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
st.write(xtest)

model_RFC= pickle.load(open('RFC.sav','rb'))
Result_RFC= model_RFC.predict(xtest)
st.write('your result for the diabetes with RFC is', Result_RFC)

model_SVM= pickle.load(open('svm.sav','rb'))
Result_SVM= model_SVM.predict(xtest)
st.write('your result for the diabetes with SVM is', Result_SVM)

model_Knn= pickle.load(open('knn.sav','rb'))
Result_Knn= model_Knn.predict(xtest)
st.write('your result for the diabetes with Knn is', Result_Knn)

