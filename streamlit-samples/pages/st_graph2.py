import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("二次関数グラフ表示")

col1, col2 = st.columns(2)
with col1:
  st.markdown("下のスライダーで係数a,b,cを調整するとy=ax^2+b+cのグラフが自動更新されます。")
  a = st.slider("係数 a", min_value=-10.0, max_value=10.0, step=0.1, value=1.0)
  b = st.slider("係数 b", min_value=-10.0, max_value=10.0, step=0.1, value=0.0)
  c = st.slider("係数 c", min_value=-10.0, max_value=10.0, step=0.1, value=0.0)
with col2:
  x = np.linspace(-10, 10, 400)
  y = a * x**2 + b * x + c

  fig, ax = plt.subplots()
  ax.plot(x, y, label=f'y = {a} x^2 + {b}x + {c}')
  ax.axhline(0, color='black', linewidth=0.5)
  ax.axvline(0, color='black', linewidth=0.5)
  ax.set_xlabel("x")
  ax.set_ylabel("y")

  ax.grid(True)
  ax.legend()

  st.pyplot(fig)
