import time
import gradio as gr

print(gr.__version__)

def slow_echo(message, history):
  for i in range(len(message)):
    time.sleep(0.3)
    yield "You typed: " + message[:i + 1]
# chatbot = gr.Chatbot()
with gr.Blocks() as demo:
  gr.ChatInterface(
    fn=slow_echo,
    type="messages",
    #    chatbot=chatbot,
  )

demo.launch()
