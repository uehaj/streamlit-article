import streamlit as st
import openai
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()

# OpenAI APIキーを環境変数から取得
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("チャットAI")

# チャット履歴の初期化（辞書形式）
if "message_history" not in st.session_state:
  st.session_state.message_history = [
    {"role": "system", "content": "あなたは親切なAIチャットボットです。"}
  ]

def get_chat_completion(user_input: str, messages) -> str:
  """OpenAI API を使用してチャットのレスポンスを取得する"""
  response = openai.chat.completions.create(
    model="gpt-4",
    messages=messages
  )
  return response.choices[0].message.content

# ユーザーの入力を監視
if user_input := st.chat_input("聞きたいことを入力してね！"):
  with st.spinner("ChatGPT is typing ..."):
    # ユーザーの入力を追加
    st.session_state.message_history.append(
      {"role": "user", "content": user_input})

    # ChatGPT の応答を取得
    answer = get_chat_completion(user_input, st.session_state.message_history)

    # 応答を辞書形式で追加
    st.session_state.message_history.append(
      {"role": "assistant", "content": answer})

# チャット履歴の表示
for message in st.session_state.get("message_history", []):
  st.chat_message(message["role"]).markdown(message["content"])
