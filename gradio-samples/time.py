import time as t
import gradio as gr

def slow_echo(message, history):
  for i in range(len(message)):
    t.sleep(0.3)
    yield "You typed: " + message[: i + 1]

with gr.Blocks() as demo:
  gr.ChatInterface(
    fn=slow_echo,
    type="messages"
  )

demo.launch()
