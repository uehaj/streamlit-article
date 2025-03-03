import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# バックエンドを変更
matplotlib.use('Agg')

def quadratic_plot(a, b, c):
  x = np.linspace(-10, 10, 400)
  y = a * x**2 + b * x + c
  fig, ax = plt.subplots()
  ax.plot(x, y)
  ax.set_title(f"Graph of y = {a}x² + {b}x + {c}")
  ax.set_xlabel("x")
  ax.set_ylabel("y")
  ax.grid(True)
  return fig

with gr.Blocks() as demo:
  gr.Markdown("# 二次関数グラフ表示アプリ")
  gr.Markdown("係数 \(a\), \(b\), \(c\) を入力してグラフを表示します。")

  a_slider = gr.Slider(minimum=-10, maximum=10, step=0.1, value=1, label="a")
  b_slider = gr.Slider(minimum=-10, maximum=10, step=0.1, value=0, label="b")
  c_slider = gr.Slider(minimum=-10, maximum=10, step=0.1, value=0, label="c")

  graph = gr.Plot()

  update_button = gr.Button("グラフを更新")
  update_button.click(fn=quadratic_plot, inputs=[
                      a_slider, b_slider, c_slider], outputs=graph)

demo.launch()
