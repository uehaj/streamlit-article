import streamlit as st

if name := st.text_input("あなたの名前を入力してください"):
  st.write(f"こんにちは{name}さん!")
