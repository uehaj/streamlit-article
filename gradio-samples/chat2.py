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

print(os.getenv("OPENAI_API_KEY"))
history: list[str] = []

def yes(message, history):
  # OpenAI APIを使用して応答を生成
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    # model="llama3",
    # model="gemma-2-2b-it",
    messages=[{"role": "user", "content": "こんにちは"}],
    # stream=True,
  )

  # reply = response.choices[0].text.strip()
  reply = response.choices[0].message.content
  history.append({"role": "assistant", "content": reply})
  return history

def vote(data: gr.LikeData):
  if data.liked:
    print("You upvoted this response: ", data.value)
  else:
    print("You downvoted this response: ", data.value)

with gr.Blocks() as demo:
  chatbot = gr.Chatbot(
    type="messages",
    placeholder="<strong>Your Personal Yes-Man</strong><br>Ask Me Anything")
  chatbot.like(fn=vote, inputs=None, outputs=None)
  gr.ChatInterface(fn=yes, type="messages", chatbot=chatbot)

demo.launch()
