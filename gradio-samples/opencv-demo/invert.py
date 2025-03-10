import gradio as gr
import numpy as np

def invert_colors(img: np.ndarray) -> np.ndarray:
    print(type(img))
    return 255 - img

gr.Interface(fn=invert_colors,
             inputs="image",
             outputs="image").launch()

