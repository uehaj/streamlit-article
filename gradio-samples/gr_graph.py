import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# バックエンドを変更
matplotlib.use('Agg')

def quadratic_plot(a, b, c):
  # x軸の値を-10から10まで生成
  x = np.linspace(-10, 10, 400)
  # 二次関数の計算
  y = a * x**2 + b * x + c

  # グラフ描画
  fig, ax = plt.subplots()
  ax.plot(x, y)
  ax.set_title(f"Graph of y = {a}x² + {b}x + {c}")
  ax.set_xlabel("x")
  ax.set_ylabel("y")
  ax.grid(True)
  return fig

# Gradioインターフェースの定義
with gr.Blocks() as demo:
  gr.Markdown("# 二次関数グラフ表示アプリ")
  gr.Markdown("下のスライダーで係数 \(a\), \(b\), \(c\) を調整するとグラフが自動更新されます。")

  with gr.Row():
    a_slider = gr.Slider(minimum=-10, maximum=10, step=0.1, value=1, label="a")
    b_slider = gr.Slider(minimum=-10, maximum=10, step=0.1, value=0, label="b")
    c_slider = gr.Slider(minimum=-10, maximum=10, step=0.1, value=0, label="c")

  graph = gr.Plot(value=quadratic_plot(1, 0, 0))  # 初期表示で描画

  # スライダーの値が変更されたときに自動更新するようにlive=Trueを設定
  a_slider.change(fn=quadratic_plot, inputs=[
                  a_slider, b_slider, c_slider], outputs=graph)
  b_slider.change(fn=quadratic_plot, inputs=[
                  a_slider, b_slider, c_slider], outputs=graph)
  c_slider.change(fn=quadratic_plot, inputs=[
                  a_slider, b_slider, c_slider], outputs=graph)

  # 初回表示用にボタンも用意（もしくは初回の自動実行も可能）
  update_button = gr.Button("更新")
  update_button.click(fn=quadratic_plot, inputs=[
                      a_slider, b_slider, c_slider], outputs=graph)

demo.launch()
