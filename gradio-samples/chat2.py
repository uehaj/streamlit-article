import gradio as gr

history: list[str] = []
def yes(message, history):
    history.append(message)
    return message, history

def vote(data: gr.LikeData):
    if data.liked:
        print("You upvoted this response: ", data.value)
    else:
        print("You downvoted this response: ", data.value)

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(placeholder="<strong>Your Personal Yes-Man</strong><br>Ask Me Anything")
#    chatbot.like(vote, None, None)
    chatbot.like(fn=vote, inputs=None, outputs=None)
    gr.ChatInterface(fn=yes, type="messages", chatbot=chatbot, examples=["hello", "hola", "merhaba"])

demo.launch()
