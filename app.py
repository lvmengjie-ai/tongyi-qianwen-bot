import gradio as gr
from langchain_community.chat_models import ChatTongyi

def chat(message, history):
    llm = ChatTongyi(
        model_name="qwen-turbo",
        dashscope_api_key="sk-"
    )
    response = llm.invoke(message)
    return response.content

demo = gr.ChatInterface(
    fn=chat,
    title="通义千问基础对话机器人",
    description="纯API调用，稳定无警告"
)

if __name__ == "__main__":
    demo.launch()
