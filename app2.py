import streamlit as st
import pickle
model=pickle.load(open('model.pickle','rb'))
st.title("Revenue Prediction")
x=st.number_input('Input Temperature')
if st.button('Predict'):
  x=np.array(x)
  result=model.predict(x.reshape(-1,1)
  
  st.success(result)


