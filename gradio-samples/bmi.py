import gradio as gr

with gr.Blocks() as demo:
  input_text = gr.Textbox(title="title")

  @gr.render(inputs=input_text)
  def show_split(text):
    print(type(input_text))
    if len(text) == 0:
      gr.Markdown("## No Input Provided")
    else:
      for letter in text:
        with gr.Row():
          text = gr.Textbox(letter)
          btn = gr.Button("Clear")
          btn.click(lambda: gr.Textbox(value=""), None, text)

demo.launch()
