import gradio as gr

def bmi(height, weight):
    return weight / (height / 100) ** 2

demo = gr.Interface(
    fn=bmi,
    inputs=["slider", "slider"],
    outputs=["text"],
)

demo.launch()

