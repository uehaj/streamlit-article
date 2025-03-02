import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
  base_url=os.getenv("BASE_URL"),
  api_key=os.getenv("OPENAI_API_KEY")
)

system_prompt = {"role": "system",
                 "content": "あなたは親切なAIチャットボットです。日本語で回答してください。"}

if "message_history" not in st.session_state:
  st.session_state.message_history = [system_prompt]

def chat_completion_stream(messages):
  response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=messages,
    stream=True,
  )
  return response

st.title("チャットAI(Streaming)")

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
