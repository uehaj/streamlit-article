# gr_invert.py
import gradio as gr
import numpy as np

# 色を反転させる関数
def invert_colors(img: np.ndarray) -> np.ndarray:
    return 255 - img

demo = gr.Interface(fn=invert_colors, # ラッピングしたい関数fn
                    inputs=gr.Image(), # fnの引数に対するUIコンポーネント指定
                    outputs=gr.Image()) # fnの返り値に対するUIコンポーネント指定
demo.launch()
