import gradio as gr
import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

# OpenAI APIキーを環境変数から取得
load_dotenv()

client = OpenAI(
  # base_url='http://localhost:1337/v1',
  api_key=os.getenv("OPENAI_API_KEY")
)

client1 = OpenAI(
  #  base_url='http://localhost:11434/v1',
  api_key=os.getenv("OPENAI_API_KEY")
)

history: list[str] = []

def chat_response(messages, history):
  # OpenAI(互換)APIを使用して応答を生成
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    # model="llama3",
    # model="gemma-2-2b-it",
    messages=[{"role": "user", "content": messages}],
    # stream=True,
  )
  # reply = response.choices[0].text.strip()
  reply = response.choices[0].message.content
  history.append({"role": "assistant", "content": reply})
  return history

with gr.Blocks() as demo:
  chatbot = gr.Chatbot(
    type="messages",
    placeholder="なんでも聞いて下さい")
  gr.ChatInterface(fn=chat_response, type="messages", chatbot=chatbot)

demo.launch()
