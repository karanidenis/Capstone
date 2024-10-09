from langflow.load import run_flow_from_json
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

result = run_flow_from_json(flow="flow/webpage-summarries.json",
                            input_value="message",
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)

# from pprint import pprint
# pprint(result)
summarized_text = result[0].outputs[0].results['text'].text
print(summarized_text)
