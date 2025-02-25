import random
import time

import gradio as gr

# Blocksの作成
with gr.Blocks() as demo:
    # UI
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    # イベントリスナー
    def user(message, chat_history):
        chat_history.append((message, None))
        return "", chat_history
    def bot(chat_history):
        time.sleep(2)
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history[-1][1] = bot_message
        return chat_history
    msg.submit(user, [msg, chatbot], [msg, chatbot]).then(
        bot, chatbot, chatbot)

# 起動
demo.launch()