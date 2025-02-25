import streamlit as st
import openai
from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()

# OpenAI APIキーを環境変数から取得
openai.api_key = os.getenv('OPENAI_API_KEY')

st.title('Chat AI with OpenAI')

if "message_history" not in st.session_state:
    st.session_state.message_history = [
        # System Prompt を設定 ('system' はSystem Promptを意味する)
        ("system", "You are a helpful assistant.")
    ]
# OpenAI APIを使用して応答を生成
# 応答を表示
# st.text_area("AI: ", response.choices[0].message['content'].strip())
# ユーザーの入力を監視
if user_input := st.chat_input("聞きたいことを入力してね！"):
    with st.spinner("ChatGPT is typing ..."):
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        answer = response.choices[0].message

#            response = chain.invoke({"user_input": user_input})

    # ユーザーの質問を履歴に追加 ('user' はユーザーの質問を意味する)
    st.session_state.message_history.append(("user", user_input))

    # ChatGPTの回答を履歴に追加 ('assistant' はChatGPTの回答を意味する)
    st.session_state.message_history.append(("ai", answer))

# チャット履歴の表示
for role, message in st.session_state.get("message_history", []):
    st.chat_message(role).markdown(message)
