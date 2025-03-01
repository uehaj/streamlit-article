import streamlit as st
import openai
from dotenv import load_dotenv
import os

# OpenAI APIキーを環境変数から取得
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("チャットAI")

# システムプロンプトを初期設定
if "message_history" not in st.session_state:
  st.session_state.message_history = [
    {"role": "system", "content": "あなたは親切なAIチャットボットです。"}
  ]

def chat_completion(messages) -> str:
  response = openai.chat.completions.create(
    base_url="http://127.0.0.1:/v1",
    model="gpt-4o-mini",
    messages=messages,
  )
  return response.choices[0].message.content

if user_input := st.chat_input("聞きたいことを入力してね！"):
  st.session_state.message_history.append(
    {"role": "user", "content": user_input})
  for message in st.session_state.message_history:
    if message["role"] != "system":
      with st.chat_message(message["role"]):
        st.markdown(message["content"])

  with st.spinner("ChatGPT is typing ..."):
    # AIの応答を取得
    answer = chat_completion(st.session_state.message_history)
    with st.chat_message("ai"):
      st.markdown(answer)
  st.session_state.message_history.append(
    {"role": "assistant", "content": answer})
