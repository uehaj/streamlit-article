# gr_chatai.py
import gradio as gr
from typing import Generator, List, Dict
from chatai_util import chat_completion_stream, SYSTEM_PROMPT  # ①

def chat_response(message: str, history: List[Dict[str, str]]) -> Generator:
  user_message = {"role": "user", "content": message}
  response = chat_completion_stream([
    SYSTEM_PROMPT,
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
