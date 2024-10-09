from langflow.load import run_flow_from_json
TWEAKS = {
  "URL-HkBwV": {
    "urls": [
      "https://www.techtarget.com/searchstorage/definition/cache#:~:text=A%20cache%20%2D%2D%20pronounced%20CASH,recently%20or%20frequently%20accessed%20data."
    ]
  },
  "ParseData-FS2Gu": {
    "sep": "\n",
    "template": "{text}"
  },
  "Prompt-OwFNG": {
    "template": "To assist learners in understanding key concepts, please analyze the following content and provide a clear, summarized explanation. Focus on the main ideas, key details, and relevant insights from your own knowledge to enhance comprehension.\nUrl contains data from a whole webpage while data is a section of it. Try to be thorough but brief for both.\n\n\nCheck if url is empty, if yes, use data and viceverca\n{url}",
    "url": ""
  },
  "OllamaModel-tYYlU": {
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
    "verbose": False
  },
  "TextOutput-E68b7": {
    "input_value": ""
  }
}

result = run_flow_from_json(flow="flow/learnmate-URL.json",
                            input_value="message",
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)

# from pprint import pprint
# pprint(result)

summarized_text = result[0].outputs[0].results['text'].text
print(summarized_text)
