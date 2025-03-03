import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# タイトル
st.title('リサージュ図形表示アプリ')

# 2つのカラムを作成
col1, col2 = st.columns(2)

with col1:
  # スライダーで2つの整数値を入力
  a = st.slider('x軸の係数', 1, 10, 1)
  b = st.slider('y軸の係数', 1, 10, 1)

with col2:
  # リサージュ図形を描画
  t = np.linspace(0, 2 * np.pi, 100)
  x = np.sin(a * t)
  y = np.sin(b * t)

  fig, ax = plt.subplots()
  ax.plot(x, y)
  ax.axhline(0, color='black', linewidth=0.5)
  ax.axvline(0, color='black', linewidth=0.5)

  ax.set_aspect('equal')
  st.pyplot(fig)
