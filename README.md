# Gradio Code Generation Interface

This repository contains a Python script that creates a Gradio interface for generating code using a language model hosted on a local server. The interface allows users to enter a prompt, which is then sent to the server for code generation. The generated code is displayed in the Gradio interface.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- requests
- gradio
- Ollama

You can install the required packages using pip: `pip install requests gradio`

`https://github.com/ollama/ollama`

## Usage

1. Make sure you have a language model server running locally at `http://localhost:11434/api/generate`. This script is configured to send requests to this URL.

2. Run the Python script:
`python main.py`


3. The Gradio interface will open in your default web browser. You can enter your prompt in the text box and click the "Submit" button to generate code based on your prompt.

4. The generated code will be displayed in the output area of the Gradio interface.

## Code Explanation

Here's a brief explanation of the code:

1. The script imports the necessary libraries: `requests` for making HTTP requests, `json` for working with JSON data, and `gradio` for creating the user interface.

2. The `url` and `headers` variables are defined for making requests to the language model server.

3. The `history` list is used to keep track of the prompts entered by the user.

4. The `generate_code` function takes a `prompt` as input, appends it to the `history` list, and constructs the final prompt by joining the prompts in the `history` list with newline characters.

5. The function then creates a JSON payload with the model name, final prompt, and a flag indicating whether to stream the response.

6. The function sends a POST request to the server with the JSON payload and processes the response. If the response is successful (status code 200), it extracts the generated code from the response and returns it. Otherwise, it prints an error message.

7. The `gr.Interface` is created, passing the `generate_code` function as the function to be called, and specifying the input as a multi-line text box and the output as text.

8. Finally, the `interface.launch(share=True)` line starts the Gradio interface and makes it shareable with others.

Note: This script assumes that you have a language model server running locally at `http://localhost:11434/api/generate` and that the server expects a JSON payload with the specified format. You may need to modify the code to match the requirements of your language model server.


