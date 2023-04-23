import streamlit as st
import numpy as np
import pickle


#Importing our pickle file
model = pickle.load(open('C:/Users/Deepak Bhatt/Desktop/ML Dataset/diab_pred.pkl', 'rb'))

#Title of app
st.title('Will the person make a purchase or not')

#Range of paramenters
PageValues = st.slider("PageValues",0.00,200.76)
ExitRates = st.slider("ExitRates",0.000,0.200,step=0.001,format="%.3f")
ProductRelated_Duration = st.slider("ProductRelated_Duration",0.00,15000.00)
ProductRelated = st.slider("ProductRelated",0,200)

#Pridiction function
def predict():
    float_features = [float(x) for x in [PageValues, ExitRates, ProductRelated_Duration, ProductRelated]]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    label = prediction[0]
    
    print(type(label))
    print(label)

#Printing the output 
    if(int(label)==1):
        st.success('Hureyyyy!! The costomer will make a purchase '  + ' :thumbsup:')
    else:
        st.success('Ohhh The costomer wont make a purchase '  + ' :thumbsup:')

trigger = st.button('Predict', on_click=predict)

