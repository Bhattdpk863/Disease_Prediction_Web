import streamlit as st
import numpy as np
import pickle


#Importing our pickle file
model = pickle.load(open('diab_pred.pkl', 'rb'))

#Title of app
st.title('The person is diabetic or not')

Pregnancies = st.text_input('Number of Pregnancies')
Glucose = st.text_input('Glucose Level')
BloodPressure = st.text_input('Blood Pressure value')
SkinThickness = st.text_input('Skin Thickness value')
Insulin = st.text_input('Insulin Level')
BMI = st.text_input('BMI value')
DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
Age = st.text_input('Age of the Person')


#Pridiction function
def predict():
    float_features = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    label = prediction[0]
    
    print(type(label))
    print(label)

#Printing the output 
    if(int(label)==0):
        st.success('The person is not diabetic'  + ' :thumbsup:')
    else:
        st.success('The person is diabetic '  + ' :thumbsup:')

trigger = st.button('Predict', on_click=predict)

