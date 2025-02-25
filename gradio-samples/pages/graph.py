import gradio as gr
import matplotlib.pyplot as plt
import numpy as np


# 二次関数のグラフを生成する関数
def plot_quadratic(a, b, c):
    # xの範囲を設定
    x = np.linspace(-10, 10, 400)
    # 二次関数 y = ax^2 + bx + c
    y = a * x**2 + b * x + c
    # グラフを描画
    plt.figure()
    plt.plot(x, y, label=f"{a}x**2 + {b}x + {c}")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.title("Quadratic Function")
    return plt


# Gradioインターフェースを作成
interface = gr.Interface(
    fn=plot_quadratic,
    inputs=[
        gr.Number(label="a (x**2 の係数)", value=1),
        gr.Number(label="b (xの係数)", value=0),
        gr.Number(label="c (定数項)", value=0),
    ],
    outputs="plot",
    title="二次関数のグラフ",
    description="a, b, cの値を入力して二次関数y=ax²+bx+cのグラフを描きます。",
)

# アプリを起動
if __name__ == "__main__":
    interface.launch()
