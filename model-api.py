import argparse
import json
from argparse import RawTextHelpFormatter
import requests
from typing import Optional
import warnings
try:
    from langflow.load import upload_file
except ImportError:
    warnings.warn("Langflow provides a function to help you upload files to the flow. Please install langflow to use it.")
    upload_file = None

BASE_API_URL = "http://127.0.0.1:7860"
FLOW_ID = "7f6d04f0-3bc1-4b74-9031-4da7b210cfc6"
ENDPOINT = "" # You can set a specific endpoint name in the flow settings

# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
TWEAKS = {
  "TextInput-yDnxw": {
    "input_value": "611\n\nsource is a shell command designed for users running on Linux (or any Posix, but whatever, not Windows).\n\nOn Windows, virtualenv creates a .bat/.ps1 file, so you should run venv\\Scripts\\activate instead (per the virtualenv documentation on the activate script).\n\nJust run activate, without an extension, so the right file will get used regardless of whether you're using cmd.exe or PowerShell.\n\nShare\nFollow\nedited Feb 17, 2021 at 6:29\nanswered Jan 19, 2012 at 4:57\nJohn Flatness's user avatar\nJohn Flatness\n33.5k55 gold badges8080 silver badges8181 bronze badges\nThis also helps with virtualenv on both Posix and Windoze systems. virtualenv.pypa.io/en/stable/userguide – \nBlairg23\n CommentedJul 26, 2016 at 21:09\nI don't see this \"venv\" directory after installing Python 2.7 on Windows. Advice? I went to Blairg23's link, but do not see an \"activate\" script in my Python \"Scripts\" directory. – \nryanwebjackson\n CommentedOct 3, 2017 at 2:16\n19\nor just activate – \nMarcin Rapacz\n CommentedApr 27, 2018 at 11:37\n19\ni ran .\\\\venv\\Scripts\\activate.bat but the command just passes on windows 10 without actiavting venv sysmbol (venv) C:\\myApp. what is the problem – \nLutaaya Huzaifah Idris\n CommentedJun 30, 2018 at 8:26 \n8\nI ran . venv\\scripts\\activate On Vscode PowerSh"
  },
  "Prompt-WQFON": {
    "template": "To assist learners in understanding key concepts, please analyze the following content and provide a clear, summarized explanation. Focus on the main ideas, key details, and relevant insights from your own knowledge to enhance comprehension.\n\n{data}",
    "data": ""
  },
  "OllamaModel-2OAvC": {
    "base_url": "http://localhost:11434",
    "format": "",
    "input_value": "",
    "metadata": {},
    "mirostat": "Disabled",
    "mirostat_eta": None,
    "mirostat_tau": None,
    "model_name": "llama3:latest",
    "num_ctx": None,
    "num_gpu": None,
    "num_thread": None,
    "repeat_last_n": None,
    "repeat_penalty": None,
    "stop_tokens": "",
    "stream": False,
    "system": "",
    "system_message": "",
    "tags": "",
    "temperature": 0.2,
    "template": "",
    "tfs_z": None,
    "timeout": None,
    "top_k": None,
    "top_p": None,
    "verbose": True
  },
  "TextOutput-b2p9L": {
    "input_value": ""
  },
  "SequentialTaskComponent-kbDAs": {
    "async_execution": True,
    "expected_output": "",
    "task_description": ""
  },
  "URL-hWZgh": {
    "urls": [
      "https://docs.langflow.org/components-io"
    ]
  },
  "OllamaModel-4f7Ko": {
    "base_url": "http://localhost:11434",
    "format": "",
    "input_value": "",
    "metadata": {},
    "mirostat": "Disabled",
    "mirostat_eta": None,
    "mirostat_tau": None,
    "model_name": "llama3:latest",
    "num_ctx": None,
    "num_gpu": None,
    "num_thread": None,
    "repeat_last_n": None,
    "repeat_penalty": None,
    "stop_tokens": "",
    "stream": False,
    "system": "",
    "system_message": "",
    "tags": "",
    "temperature": 0.2,
    "template": "",
    "tfs_z": None,
    "timeout": None,
    "top_k": None,
    "top_p": None,
    "verbose": True
  },
  "TextOutput-YHJ2r": {
    "input_value": ""
  },
  "ParseData-PuHhe": {
    "sep": "\n",
    "template": "{text}"
  },
  "Prompt-iHmBK": {
    "template": "To assist learners in understanding key concepts, please analyze the following content and provide a clear, summarized explanation. Focus on the main ideas, key details, and relevant insights from your own knowledge to enhance comprehension.\nUrl contains data from a whole webpage while data is a section of it. Try to be thorough but brief for both.\n\n\nCheck if url is empty, if yes, use data and viceverca\n{url}\n\n{data}",
    "data": "",
    "url": ""
  },
  "TextInput-wQuP4": {
    "input_value": "Inputs\nInputs are components used to define where data enters your flow. They can receive data from various sources, such as users, databases, or any other source that can be converted to Text or Data.\n\nChat Input\nThis component collects user input from the chat.\n\nThe difference between Chat Input and other Input components is the output format, the number of configurable fields, and the way they are displayed in the Playground.\n\nChat Input components can output Text or Data. When you want to pass the sender name or sender to the next component, use the Data output. To pass only the message, use the Text output. Passing only the message is useful when saving the message to a database or a memory system like Zep.\n\nParameters\nName\tDisplay Name\tInfo\nSender Type\tSender Type\tSpecifies the sender type (User or Machine). Defaults to User\nSender Name\tSender Name\tSpecifies the name of the sender. Defaults to User\nMessage\tMessage\tSpecifies the message text. Multiline text input\nSession ID\tSession ID\tSpecifies the session ID of the chat history\nnote\nIf \"As Data\" is True and the \"Message\" is a Data, the data will be updated with the Sender, Sender Name, and Session ID.\n\nText Input"
  }
}

def run_flow(message: str,
  endpoint: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  api_key: Optional[str] = None) -> dict:
    """
    
    # Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param endpoint: The ID or the endpoint name of the flow
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/api/v1/run/{endpoint}"
    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if api_key:
        headers = {"x-api-key": api_key}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    parser = argparse.ArgumentParser(description="""Run a flow with a given message and optional tweaks.
Run it like: python <your file>.py "your message here" --endpoint "your_endpoint" --tweaks '{"key": "value"}'""",
        formatter_class=RawTextHelpFormatter)
    parser.add_argument("message", type=str, help="The message to send to the flow")
    parser.add_argument("--endpoint", type=str, default=ENDPOINT or FLOW_ID, help="The ID or the endpoint name of the flow")
    parser.add_argument("--tweaks", type=str, help="JSON string representing the tweaks to customize the flow", default=json.dumps(TWEAKS))
    parser.add_argument("--api_key", type=str, help="API key for authentication", default=None)
    parser.add_argument("--output_type", type=str, default="chat", help="The output type")
    parser.add_argument("--input_type", type=str, default="chat", help="The input type")
    parser.add_argument("--upload_file", type=str, help="Path to the file to upload", default=None)
    parser.add_argument("--components", type=str, help="Components to upload the file to", default=None)

    args = parser.parse_args()
    try:
      tweaks = json.loads(args.tweaks)
    except json.JSONDecodeError:
      raise ValueError("Invalid tweaks JSON string")

    if args.upload_file:
        if not upload_file:
            raise ImportError("Langflow is not installed. Please install it to use the upload_file function.")
        elif not args.components:
            raise ValueError("You need to provide the components to upload the file to.")
        tweaks = upload_file(file_path=args.upload_file, host=BASE_API_URL, flow_id=args.endpoint, components=[args.components], tweaks=tweaks)

    response = run_flow(
        message=args.message,
        endpoint=args.endpoint,
        output_type=args.output_type,
        input_type=args.input_type,
        tweaks=tweaks,
        api_key=args.api_key
    )

    print(json.dumps(response, indent=2))

if __name__ == "__main__":
    main()
