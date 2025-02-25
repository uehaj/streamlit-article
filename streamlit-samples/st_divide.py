import streamlit as st

a = st.number_input("A")
b = st.number_input("B")
if b != 0:
  st.write("A/B = ", a / b)
else:
  st.write("error")

