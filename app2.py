import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pickle','rb'))
st.title("Revenue Prediction")
x=st.number_input('Input Temperature')
if st.button('Predict'):
  x=np.array(x)
  result=model.predict(x.reshape(-1,1))
  st.caption('Revenue Prediction')
  ket_qua=result[0]
  ket_qua=str(ket_qua)
  st.success(ket_qua)


