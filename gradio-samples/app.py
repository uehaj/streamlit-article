import gradio as gr

from pages import main_page, second_page, graph

with gr.Blocks() as demo:
    main_page.demo.render()
with demo.route("Second Page"):
    second_page.demo.render()
with demo.route("Graph"):
    graph.interface.render()

if __name__ == "__main__":
    demo.launch()
