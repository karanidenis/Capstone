from langflow.load import run_flow_from_json
TWEAKS = {
  "URL-HkBwV": {
    "urls": [
      "https://www.nationalgeographic.com/science/article/ai-predict-earthquakes-seismology"
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
    "verbose": True
  },
  "TextOutput-E68b7": {
    "input_value": ""
  },
  "OpenAIModel-B3cI4": {
    "api_key": "",
    "input_value": "",
    "json_mode": False,
    "max_tokens": None,
    "model_kwargs": {},
    "model_name": "gpt-4o-mini",
    "openai_api_base": "",
    "output_schema": {},
    "seed": 1,
    "stream": False,
    "system_message": "",
    "temperature": 0.1
  }
}

result = run_flow_from_json(flow="./flow/learnmate-URL.json",
                            input_value="message",
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)
