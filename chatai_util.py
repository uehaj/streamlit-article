from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
  base_url=os.getenv("BASE_URL"),
  api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = {"role": "system",
                 "content": "あなたは親切なAIチャットボットです。\
                 日本語で回答してください。"}

def chat_completion_stream(messages):
  response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=messages,
    stream=True,
  )
  return response
