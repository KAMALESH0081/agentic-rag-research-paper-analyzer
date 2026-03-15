import gradio as gr
import requests

API_URL = "http://localhost:8000/analyze"


def analyze(file):

    with open(file.name, "rb") as f:
        response = requests.post(API_URL, files={"file": f})

    return response.json()


interface = gr.Interface(
    fn=analyze,
    inputs=gr.File(label="Upload Research Paper"),
    outputs=gr.JSON(),
    title="Research Paper Analyzer"
)

interface.launch()