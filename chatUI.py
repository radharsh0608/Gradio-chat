import gradio as gr
import API as chat
def echo(message, history, model, prompt,temperature,maxTokens,topP,repetitionPenalty):
    systemMessage=chat.responseFromModel(model,prompt,message,temperature,maxTokens,topP,repetitionPenalty)
    return systemMessage

demo = gr.ChatInterface(fn=echo, additional_inputs=[
    gr.Dropdown(
        ["chatNBX - mixtral-8x7b-inst-v0-1-32k",
         "chatNBX - openhermes-2-5-m7b-4k",
         "chatNBX - Qwen1-5-7B-Chat",
         "chatNBX - gemma-7b-it",
         "chatNBX - nous-hermes-13b-4k",
         "chatNBX - Qwen1-5-14B-Chat",
         "OpenRouter - nousresearch/nous-capybara-7b:free",
         "OpenRouter - mistralai/mistral-7b-instruct:free",
         "OpenRouter - gryphe/mythomist-7b:free",
         "OpenRouter - undi95/toppy-m-7b:free",
         "OpenRouter - openrouter/cinematika-7b:free",
         "OpenRouter - google/gemma-7b-it:free",
         "OpenRouter - rwkv/rwkv-5-world-3b",
         "OpenRouter - recursal/rwkv-5-3b-ai-town",
         "OpenRouter - recursal/eagle-7b",
         "OpenRouter - huggingfaceh4/zephyr-7b-beta:free",
         "OpenRouter - openchat/openchat-7b:free"],label="Select the model"),
    gr.Textbox(label="Enter your prompt:"),
    gr.Slider(0, 1, value=0.5, label="Temperature"),
    gr.Slider(1, 1000, value=200, label="Max Tokens"),
    gr.Slider(0, 1, value=1, label="Top P"),
    gr.Slider(0,2 , value=1.15, label="Repetition Penalty"),
], title="Elle",retry_btn=None,undo_btn=None)
demo.launch()