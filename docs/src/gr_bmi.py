import gradio as gr

def bmi(height, weight):
  return weight / (height / 100) ** 2

demo = gr.Interface(
  fn=bmi,
  inputs=[
    gr.Number(label="身長 (cm)"),
    gr.Number(label="体重 (kg)")
  ],
  outputs=gr.Number(label="BMI")
)

demo.launch()
