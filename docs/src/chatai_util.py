# chatai_util.py
from typing import Generator, List, Dict  # ①
from openai import OpenAI  # ②
from dotenv import load_dotenv  # ②
import os

load_dotenv()  # ⑤

client = OpenAI(
  base_url=os.getenv("BASE_URL"),       # ⑥
  api_key=os.getenv("OPENAI_API_KEY")   # ⑦
)

SYSTEM_PROMPT = {"role": "system",
                 "content": "あなたは親切なAIチャットボットです。\
                 日本語で回答してください。"}  # ⑧

def chat_completion_stream(messages: List[Dict[str, str]]) -> Generator:
  response = client.chat.completions.create(
    model=os.getenv("MODEL"),  # ⑩
    messages=messages,
    stream=True,               # ⑫
  )
  return response               # ⑬
