# import argparse
# import json
# from argparse import RawTextHelpFormatter
# import requests
# from typing import Optional
# import warnings
# from flask import Flask, request, jsonify
# from flask_cors import CORS

# try:
#     from langflow.load import upload_file
# except ImportError:
#     warnings.warn("Langflow provides a function to help you upload files to the flow. Please install langflow to use it.")
#     upload_file = None

# BASE_API_URL = "http://127.0.0.1:7860"
# FLOW_ID = "7f6d04f0-3bc1-4b74-9031-4da7b210cfc6"
# ENDPOINT = "" # You can set a specific endpoint name in the flow settings
# input_value = ""

# # You can tweak the flow by adding a tweaks dictionary
# # e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
# TWEAKS = {
#   "TextInput-yDnxw": {
#     "input_value": input_value
#   },
#   "Prompt-WQFON": {
#     "template": "To assist learners in understanding key concepts, please analyze the following content and provide a clear, summarized explanation. Focus on the main ideas, key details, and relevant insights from your own knowledge to enhance comprehension.\n\n{data}",
#     "data": ""
#   },
#   "OllamaModel-2OAvC": {
#     "base_url": "http://localhost:11434",
#     "format": "",
#     "input_value": "",
#     "metadata": {},
#     "mirostat": "Disabled",
#     "mirostat_eta": None,
#     "mirostat_tau": None,
#     "model_name": "llama3:latest",
#     "num_ctx": None,
#     "num_gpu": None,
#     "num_thread": None,
#     "repeat_last_n": None,
#     "repeat_penalty": None,
#     "stop_tokens": "",
#     "stream": False,
#     "system": "",
#     "system_message": "",
#     "tags": "",
#     "temperature": 0.2,
#     "template": "",
#     "tfs_z": None,
#     "timeout": None,
#     "top_k": None,
#     "top_p": None,
#     "verbose": True
#   },
#   "TextOutput-b2p9L": {
#     "input_value": ""
#   },
#   "SequentialTaskComponent-kbDAs": {
#     "async_execution": True,
#     "expected_output": "",
#     "task_description": ""
#   },
#   "URL-hWZgh": {
#     "urls": [
#       "https://docs.langflow.org/components-io"
#     ]
#   },
#   "OllamaModel-4f7Ko": {
#     "base_url": "http://localhost:11434",
#     "format": "",
#     "input_value": "",
#     "metadata": {},
#     "mirostat": "Disabled",
#     "mirostat_eta": None,
#     "mirostat_tau": None,
#     "model_name": "llama3:latest",
#     "num_ctx": None,
#     "num_gpu": None,
#     "num_thread": None,
#     "repeat_last_n": None,
#     "repeat_penalty": None,
#     "stop_tokens": "",
#     "stream": False,
#     "system": "",
#     "system_message": "",
#     "tags": "",
#     "temperature": 0.2,
#     "template": "",
#     "tfs_z": None,
#     "timeout": None,
#     "top_k": None,
#     "top_p": None,
#     "verbose": True
#   },
#   "TextOutput-YHJ2r": {
#     "input_value": ""
#   },
#   "ParseData-PuHhe": {
#     "sep": "\n",
#     "template": "{text}"
#   },
#   "Prompt-iHmBK": {
#     "template": "To assist learners in understanding key concepts, please analyze the following content and provide a clear, summarized explanation. Focus on the main ideas, key details, and relevant insights from your own knowledge to enhance comprehension.\nUrl contains data from a whole webpage while data is a section of it. Try to be thorough but brief for both.\n\n\nCheck if url is empty, if yes, use data and viceverca\n{url}\n\n{data}",
#     "data": "",
#     "url": ""
#   },
#   "TextInput-wQuP4": {
#     "input_value": "Inputs\nInputs are components used to define where data enters your flow. They can receive data from various sources, such as users, databases, or any other source that can be converted to Text or Data.\n\nChat Input\nThis component collects user input from the chat.\n\nThe difference between Chat Input and other Input components is the output format, the number of configurable fields, and the way they are displayed in the Playground.\n\nChat Input components can output Text or Data. When you want to pass the sender name or sender to the next component, use the Data output. To pass only the message, use the Text output. Passing only the message is useful when saving the message to a database or a memory system like Zep.\n\nParameters\nName\tDisplay Name\tInfo\nSender Type\tSender Type\tSpecifies the sender type (User or Machine). Defaults to User\nSender Name\tSender Name\tSpecifies the name of the sender. Defaults to User\nMessage\tMessage\tSpecifies the message text. Multiline text input\nSession ID\tSession ID\tSpecifies the session ID of the chat history\nnote\nIf \"As Data\" is True and the \"Message\" is a Data, the data will be updated with the Sender, Sender Name, and Session ID.\n\nText Input"
#   }
# }

# def run_flow(message: str,
#   endpoint: str,
#   output_type: str = "chat",
#   input_type: str = "chat",
#   tweaks: Optional[dict] = None,
#   api_key: Optional[str] = None) -> dict:
#     """
    
#     # Run a flow with a given message and optional tweaks.

#     :param message: The message to send to the flow
#     :param endpoint: The ID or the endpoint name of the flow
#     :param tweaks: Optional tweaks to customize the flow
#     :return: The JSON response from the flow
#     """
#     api_url = f"{BASE_API_URL}/api/v1/run/{endpoint}"
#     payload = {
#         "input_value": message,
#         "output_type": output_type,
#         "input_type": input_type,
#     }
#     headers = None
#     if tweaks:
#         payload["tweaks"] = tweaks
#     if api_key:
#         headers = {"x-api-key": api_key}
#     response = requests.post(api_url, json=payload, headers=headers)
#     return response.json()
  
# def execute_flow(message: str, endpoint: str, tweaks: Optional[dict] = None, 
#                  api_key: Optional[str] = None, output_type: str = "chat", 
#                  input_type: str = "chat") -> dict:
#     """
#     A helper function to run the flow and return the response.
#     This can be called directly from the Flask endpoint.
#     """
#     response = run_flow(
#         message=message,
#         endpoint=endpoint,
#         output_type=output_type,
#         input_type=input_type,
#         tweaks=tweaks,
#         api_key=api_key
#     )
#     # output = response['outputs'][0]['outputs'][0]['results']['text']['text']
#     # print(output)   
#     # return output
#     return response

# # def main():
# #     parser = argparse.ArgumentParser(description="""Run a flow with a given message and optional tweaks.
# # Run it like: python <your file>.py "your message here" --endpoint "your_endpoint" --tweaks '{"key": "value"}'""",
# #         formatter_class=RawTextHelpFormatter)
# #     # parser.add_argument("message", type=str, help="The message to send to the flow")
# #     parser.add_argument("--endpoint", type=str, default=ENDPOINT or FLOW_ID, help="The ID or the endpoint name of the flow")
# #     parser.add_argument("--tweaks", type=str, help="JSON string representing the tweaks to customize the flow", default=json.dumps(TWEAKS))
# #     parser.add_argument("--api_key", type=str, help="API key for authentication", default=None)
# #     parser.add_argument("--output_type", type=str, default="chat", help="The output type")
# #     parser.add_argument("--input_type", type=str, default="chat", help="The input type")
# #     parser.add_argument("--upload_file", type=str, help="Path to the file to upload", default=None)
# #     parser.add_argument("--components", type=str, help="Components to upload the file to", default=None)

# #     args = parser.parse_args()
# #     try:
# #       tweaks = json.loads(args.tweaks)
# #     except json.JSONDecodeError:
# #       raise ValueError("Invalid tweaks JSON string")

# #     if args.upload_file:
# #         if not upload_file:
# #             raise ImportError("Langflow is not installed. Please install it to use the upload_file function.")
# #         elif not args.components:
# #             raise ValueError("You need to provide the components to upload the file to.")
# #         tweaks = upload_file(file_path=args.upload_file, host=BASE_API_URL, flow_id=args.endpoint, components=[args.components], tweaks=tweaks)

# #     response = execute_flow(
# #         message=args.message,
# #         endpoint=args.endpoint,
# #         output_type=args.output_type,
# #         input_type=args.input_type,
# #         tweaks=tweaks,
# #         api_key=args.api_key
# #     )

# #     output = response['outputs'][0]['outputs'][0]['results']['text']['text']
# #     print(output)   
# #     return output     
   
# app = Flask(__name__)
# CORS(app) 
    
# @app.route('/run_flow', methods=['POST'])
# def api_run_flow():
#     """
#     API endpoint to run the flow.
#     Expects JSON payload with keys: 'message', 'endpoint', 'tweaks', 'api_key'.
#     """
#     data = request.json
#     message = data.get('message')
#     endpoint = data.get('endpoint', ENDPOINT or FLOW_ID)  # Use default if not provided
#     tweaks = data.get('tweaks', json.dumps(TWEAKS))  # Default tweaks
#     api_key = data.get('api_key', None)  # API key from request
    
#     # Update input_value in TWEAKS with the provided message
#     tweaks_dict = json.loads(tweaks)
#     if 'TextInput-wQuP4' in tweaks_dict:
#         tweaks_dict['TextInput-wQuP4']['input_value'] = message

#     # Call execute_flow to run the flow
#     response = execute_flow(
#         message=message,
#         endpoint=endpoint,
#         tweaks=json.loads(tweaks),
#         api_key=api_key
#     )
    
#     # Extract the output text from the response
#     output_text = response.get('outputs', [{}])[0].get('outputs', [{}])[0].get('results', {}).get('text', {}).get('text', "")
    
#     return jsonify({"output": output_text})

# if __name__ == "__main__":
#     app.run(debug=True)  # Set debug=True for development only



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
    "input_value": "Data labeling is the process of identifying and tagging data samples commonly used in the context of training machine learning (ML) models. The process can be manual, but it's usually performed or assisted by software. Data labeling helps machine learning models make accurate predictions. It's also useful in processes such as computer vision, natural language processing (NLP) and speech recognition.\n\nThe process starts with raw data, such as images or text data, that's collected, and then one or more identifying labels are applied to each segment of data to specify the data's context in the ML model. The labels used to identify data features must be informative, specific and independent to produce a quality model.\n\nWhat is data labeling used for?\nData labeling is an important part of data preprocessing for ML, particularly for supervised learning. In supervised learning, a machine learning program is trained on a labeled data set. Models are trained until they can detect the underlying relationship between the input data and the output labels. In this setting, data labeling helps the model process and understand the input data.\n\nFor example, a model trained to identify images of animals is provided with multiple images of various types of animals from which it learns the common features of each. This enables the model to correctly identify the animals in unlabeled data.\n\nThis article is part of\n\nWhat is machine learning? Guide, definition and examples\nWhich also includes:\nThe different types of machine learning explained\nHow to build a machine learning model in 7 steps\nCNN vs. RNN: How are they different?\nData labeling is also used when constructing machine learning algorithms for autonomous vehicles, such as self-driving cars. They need to be able to tell the difference between objects that might get in their way. This information lets these vehicles process the external world and drive safely. Data labeling enables the car's artificial intelligence (AI) to tell the differences between a person and another car or between the street and the sky. Key features of those objects or data points get labeled and similarities between them are identified."
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
  }
}

def run_flow(message: str,
  endpoint: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  api_key: Optional[str] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks.

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
