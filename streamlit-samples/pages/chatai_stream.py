import streamlit as st
import openai
from dotenv import load_dotenv
import os

# OpenAI APIキーを環境変数から取得
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
st.title("チャットAI")

if "message_history" not in st.session_state:
  st.session_state.message_history = [
    {"role": "system", "content": "あなたは親切なAIチャットボットです。"}
  ]

def get_chat_completion(user_input: str, messages) -> str:
  """OpenAI API を使用してチャットのレスポンスを取得する"""
  response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    stream=True,
  )
  return response

if user_input := st.chat_input("聞きたいことを入力してね！"):
  for message in st.session_state.message_history:
    if message["role"] != "system":
      st.chat_message(message["role"]).write(message["content"])
  st.session_state.message_history.append(
    {"role": "user", "content": user_input})
  st.chat_message('user').write(user_input)
  with st.chat_message('ai'):
    answer = st.write_stream(get_chat_completion(
      user_input, st.session_state.message_history))
  st.session_state.message_history.append(
    {"role": "assistant", "content": answer})
