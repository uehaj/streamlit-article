# st_chatai.py
import streamlit as st
from chatai_util import chat_completion_stream, SYSTEM_PROMPT

if "message_history" not in st.session_state:
  st.session_state.message_history = [SYSTEM_PROMPT]

st.title("チャットAI(Streamlit)")

if user_input := st.chat_input("聞きたいことを入力してね！"):
  # 入力文字列をヒストリに追加
  st.session_state.message_history.append(
    {"role": "user", "content": user_input})
  for message in st.session_state.message_history:
    if message["role"] != "system":
      with st.chat_message(message["role"]):
        st.markdown(message["content"])

  with st.chat_message('ai'):
    # AIの応答を取得
    answer = st.write_stream(chat_completion_stream(
      st.session_state.message_history))
  # 回答文字列をヒストリに追加
  st.session_state.message_history.append(
    {"role": "assistant", "content": answer})
