import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# カラーピッカーを表示
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

# ランダムなデータを生成
x = np.random.rand(100)
y = np.random.rand(100)

# 散布図を描画
plt.scatter(x, y, color=color)

# グラフのタイトルと軸ラベルを設定
plt.title('Random Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')

# グラフを表示
st.pyplot(plt)
