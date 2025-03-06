# gr_chatai.py
import time
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import Generator, Any, List, Dict

# OpenAI APIキーを環境変数に設定
load_dotenv()

client = OpenAI()

system_prompt = {"role": "system",
                 "content": "あなたは親切なAIチャットボットです。日本語で回答してください。"}

def chat_completion_stream(messages: List[Dict[str, str]]) -> Generator:
  response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=messages,
    stream=True,
  )
  return response

def chat_response(message: str, history: List[Dict[str, str]]) -> Generator:
  user_message = {"role": "user", "content": message}
  response = chat_completion_stream(
    [
      system_prompt,
      *history,
      user_message
    ])
  ai_message = ""
  for item in response:
    chunk = item.choices[0].delta.content
    if chunk is not None:
      ai_message += chunk
    yield ai_message

demo = gr.ChatInterface(fn=chat_response, type="messages",
                        title="チャットAI(Gradio)")
demo.launch()
