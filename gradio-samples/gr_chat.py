import gradio as gr
import openai
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# OpenAI APIキーを環境変数から取得
load_dotenv()

client = OpenAI(
  base_url='http://localhost:1337/v1',
  #  base_url='http://localhost:11434/v1',
  api_key=os.getenv("OPENAI_API_KEY")
)

system_prompt = {"role": "system",
                 "content": "あなたは親切なAIチャットボットです。日本語で回答してください。"}

def chat_completion(messages) -> str:
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
  )
  return response.choices[0].message.content

def chat_response(message: str, history):
  print(json.dumps(history, indent=4, ensure_ascii=False))
  user_message = {"role": "user", "content": message}
  response = chat_completion([system_prompt, *history, user_message])
  answer = {"role": "assistant", "content": response}
  return [answer]

with gr.Blocks() as demo:
  gr.ChatInterface(fn=chat_response, type="messages", title="チャットAI")

demo.launch(pwa=True)
