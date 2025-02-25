import streamlit as st

a = st.number_input("a")
b = st.number_input("b")
if b != 0:
  st.write(a / b)
else:
  st.write("error")

