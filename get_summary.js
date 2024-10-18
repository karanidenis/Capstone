texts = "Data structures are the fundamental building blocks of computer programming. They define how data is organized, stored, and manipulated within a program. Understanding data structures is very important for developing efficient and effective algorithms. In this tutorial, we will explore the most commonly used data structures, including arrays, linked lists, stacks, queues, trees, and graphs."

class LangflowClient {
    constructor(baseURL, apiKey) {
        this.baseURL = baseURL;
        this.apiKey = apiKey;
        // this.apiKey = process.env.langflow_API_KEY;
    }
  
    async post(endpoint, body, headers = {"Content-Type": "application/json"}) {
      if (this.apiKey) {
            headers["Authorization"] = `Bearer ${this.apiKey}`;
        }
        const url = `${this.baseURL}${endpoint}`;
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify(body)
            });
  
            const responseMessage = await response.json();
            if (!response.ok) {
                throw new Error(`${response.status} ${response.statusText} - ${JSON.stringify(responseMessage)}`);
            }
            return responseMessage;
        } catch (error) {
            console.error(`Error during POST request: ${error.message}`);
            throw error;
        }
    }
  
    async initiateSession(flowId, inputValue, inputType = 'chat', outputType = 'chat', stream = false, tweaks = {}) {
        const endpoint = `/api/v1/run/${flowId}?stream=${stream}`;
        return this.post(endpoint, { input_value: inputValue, input_type: inputType, output_type: outputType, tweaks: tweaks });
    }
  
    handleStream(streamUrl, onUpdate, onClose, onError) {
        const eventSource = new EventSource(streamUrl);
  
        eventSource.onmessage = event => {
            const data = JSON.parse(event.data);
            onUpdate(data);
        };
  
        eventSource.onerror = event => {
            console.error('Stream Error:', event);
            onError(event);
            eventSource.close();
        };
  
        eventSource.addEventListener("close", () => {
            onClose('Stream closed');
            eventSource.close();
        });
  
        return eventSource;
    }
  
    async runFlow(flowIdOrName, inputValue, inputType = 'chat', outputType = 'chat', tweaks, stream = false, onUpdate, onClose, onError) {
        try {
            const initResponse = await this.initiateSession(flowIdOrName, inputValue, inputType, outputType, stream, tweaks);
            if (stream && initResponse?.outputs?.[0]?.outputs?.[0]?.artifacts?.stream_url) {
                const streamUrl = initResponse.outputs[0].outputs[0].artifacts.stream_url;
                console.log(`Streaming from: ${streamUrl}`);
                this.handleStream(streamUrl, onUpdate, onClose, onError);
            }
            return initResponse;
        } catch (error) {
          onError('Error initiating session');
        }
    }
  }
  
  async function main(inputValue, inputType = 'chat', outputType = 'chat', stream = false, onUpdate, onClose, onError) {
    const flowIdOrName = '7f6d04f0-3bc1-4b74-9031-4da7b210cfc6';
    const langflowClient = new LangflowClient('http://127.0.0.1:7860',
          process.env.langflow_API_KEY);
    const tweaks = {
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
    "mirostat_eta": null,
    "mirostat_tau": null,
    "model_name": "llama3:latest",
    "num_ctx": null,
    "num_gpu": null,
    "num_thread": null,
    "repeat_last_n": null,
    "repeat_penalty": null,
    "stop_tokens": "",
    "stream": false,
    "system": "",
    "system_message": "",
    "tags": "",
    "temperature": 0.2,
    "template": "",
    "tfs_z": null,
    "timeout": null,
    "top_k": null,
    "top_p": null,
    "verbose": true
  },
  "TextOutput-b2p9L": {
    "input_value": ""
  }
};
  
    try {
        const response = await langflowClient.runFlow(
            flowIdOrName,
            texts,
            inputType,
            outputType,
            tweaks,
            // stream,
            false,
            (data) => console.log("Received:", data.chunk), // onUpdate
            (message) => console.log("Stream Closed:", message), // onClose
            (error) => console.error("Stream Error:", error) // onError
        );
  
        if (!stream && response) {
            // const flowOutputs = response.outputs;
            // const firstComponentOutputs = flowOutputs.outputs[0];
            // const output = firstComponentOutputs.outputs.message;
            // const output = firstComponentOutputs.outputs[0];
  
            // console.log("Final Output:", output.message.text);
            // console.log("Final Output:", response.outputs.outputs);
            // console.log("Final Output:", output[0]);
            console.log("Response:", JSON.stringify(response, null, 2));
        }
    } catch (error) {
        console.error('Main Error:', error.message);
    }
  }
  
//   const args = process.argv.slice(2);
//   main(
//     args[0], // inputValue
//     args[1], // inputType
//     args[2], // outputType
//     args[3] === 'true' // stream
//   );
  
// Run the test
main().catch(console.error);
