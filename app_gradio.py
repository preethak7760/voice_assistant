from model import englishteacher
import gradio as gr


# Function to generate a response using the GPT-2 model
def generate_response(text):
    response = englishteacher(text)
    return response


# Gradio interface
iface = gr.Interface(fn=generate_response, inputs="text", outputs="text", live=True,
                     title="Voice Assistant - English Coach",
                     theme = 'huggingface')
iface.launch()
