import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
st.title('Medical Diagnostic WebAPP:')


#step1 -- load the model

model = open('rfc.pickle', 'rb')
clf = pickle.load(model)
model.close()

#step2 : get the front end user input

pregs = st.number_input('Pregnancies',1,20, step=1)
glucose= st.slider('Glucose',40.0, 200.0, 40.0)
bp= st.slider('BloodPressure',24,122,24)
skin= st.slider('SkinThickness',7,99,7)
insulin= st.slider('Insulin',14,846,14)
bmi= st.slider('BMI',18.2,67.1,18.2)
dpf=st.slider('DiabetesPedigreeFunction',0.05,2.5,0.05)
age=st.slider('Age',21,81,21)



# step3   -- converting user input to model input:

data={'Pregnancies':pregs, 'Glucose':glucose, 
      'BloodPressure':bp, 'SkinThickness':skin, 
      'Insulin':insulin, 'BMI':bmi, 'DiabetesPedigreeFunction':dpf, 'Age':age    
}
input_data = pd.DataFrame([data])



#step4- get the predictions:

preds= clf.predict(input_data)[0]
if st.button('Predict:'):
    if preds==1:
        st.error('The person has Diabetes')
    if preds==0:
        st.success('The person is Diabetes free.')
