# st_graph.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("2次関数のグラフ描画")

col1, col2 = st.columns(2)
with col1:
  a = st.number_input("係数 a", value=1.0)
  b = st.number_input("係数 b", value=0.0)
  c = st.number_input("係数 c", value=0.0)
with col2:
  x = np.linspace(-10, 10, 400)
  y = a * x**2 + b * x + c

  fig, ax = plt.subplots()
  ax.plot(x, y, label=f'y = a x^2 + bx + c\na={a}, b={b}, c={c}')
  ax.axhline(0, color='black', linewidth=0.5)
  ax.axvline(0, color='black', linewidth=0.5)
  ax.grid(color='gray', linestyle='--', linewidth=0.5)
  ax.legend()

  st.pyplot(fig)
