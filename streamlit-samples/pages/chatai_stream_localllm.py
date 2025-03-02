import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# OpenAI APIキーを環境変数から取得
load_dotenv()

client = OpenAI(
  base_url=os.getenv("BASE_URL"),
  api_key=os.getenv("OPENAI_API_KEY")
)

st.title("チャットAI(Streaming)")

# システムプロンプトを初期設定
if "message_history" not in st.session_state:
  st.session_state.message_history = [
    {"role": "system", "content": "あなたは親切なAIチャットボットです。"}
  ]

def chat_completion_stream(messages):
  response = client.chat.completions.create(
    model=os.getenv("MODEL")
    messages=messages,
    stream=True,
  )
  return response

if user_input := st.chat_input("聞きたいことを入力してね！"):
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
  st.session_state.message_history.append(
    {"role": "assistant", "content": answer})
