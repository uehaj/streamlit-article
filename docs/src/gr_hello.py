# gr_hello.py
import gradio as gr # ①

with gr.Blocks() as demo:   # ②
  gr.Markdown("Hello, world!")   # ③

demo.launch() # ④
