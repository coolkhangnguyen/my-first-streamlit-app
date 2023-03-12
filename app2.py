import streamlit as st
import pickle
model=pickle.load(open('model.pickle','rb'))
st.title("Revenue Prediction")
x=st.number_input('Input Temperature')
if st.button('Predict'):
  result=model.predict(x)
  st.caption('Revenue Prediction')
  st.success(result)


