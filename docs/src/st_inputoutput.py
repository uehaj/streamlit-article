# st_inputoutput.py
import streamlit as st

a = st.number_input("A") # ①
b = st.number_input("B") # ②
if b != 0:
  st.write("A/B = ", a / b)
else:
  st.write("error")
