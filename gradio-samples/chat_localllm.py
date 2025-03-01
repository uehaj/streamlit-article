import os
from openai import OpenAI
import gradio as gr

# OpenAIのAPIキーを設定（環境変数から取得する例）

async def chat(message, history):
  """
  ユーザーからの入力(message)とこれまでの会話の履歴(history)を元に、
  OpenAIのChat APIを呼び出し、返信を生成します。
  historyは会話履歴としてユーザーとアシスタントの発言ペアのリスト[(user, assistant), ...]です。
  """
  if history is None:
    history = []

  # 過去の会話をAPI用のメッセージ形式に変換
  messages = []
  for user_msg, assistant_msg in history:
    messages.append({"role": "user", "content": user_msg})
    messages.append({"role": "assistant", "content": assistant_msg})
  messages.append({"role": "user", "content": message})

  # OpenAI ChatCompletion APIを呼び出す
  openai = OpenAI(
    base_url='http://10014343-0.local:11434/v1',
    api_key=os.environ.get("OPENAI_API_KEY")
  )

  response = openai.chat.completions.create(
    # model="gpt-3.5-turbo",
    model="llama3",
    messages=messages
  )
  reply = response.choices[0].message.content

  # 会話履歴に追加
  history.append((message, reply))
  # テキストボックスはクリアして、更新したhistoryを返す
  return "", history

# Gradioのインターフェースを構築
with gr.Blocks(title="OpenAIチャット") as demo:
  gr.Markdown("## Gradio×OpenAIチャットアプリ")
  chatbot = gr.Chatbot(elem_classes="chatbox")
  with gr.Row():
    txt = gr.Textbox(
      show_label=False,
      placeholder="メッセージを入力してEnterキーを押すか「送信」ボタンをクリックしてください",
      elem_classes="textbox"
    )
    send_btn = gr.Button("送信", elem_classes="send-btn")

  # テキストボックスのEnter送信とボタン送信の両方に対応
  txt.submit(chat, [txt, chatbot], [txt, chatbot])
  send_btn.click(chat, [txt, chatbot], [txt, chatbot])

# アプリケーションを起動
demo.launch()
