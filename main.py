
import requests
import json
import gradio as gr 

url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type":"application/json"
}

history = []
def generate_code(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model":"CodeSarathi",
        "prompt":final_prompt,
        "stream":False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        print("Error:", response.text)

interface = gr.Interface(
    fn = generate_code,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt"),
    outputs="text"
)

interface.launch(share=True)