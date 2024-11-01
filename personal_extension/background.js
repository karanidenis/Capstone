// function debugLog(message) {
//     console.log(`[BACKGROUND ${new Date().toISOString()}]: ${message}`);
//   }
  
//   chrome.runtime.onInstalled.addListener(() => {
//     debugLog('Extension installed/updated');
//   });
  
//   chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
//     debugLog(`Received message: ${JSON.stringify(request)}`);
//     if (request.action === "logSelectedText") {
//       debugLog(`Selected text from content script: ${request.text}`);
//       sendResponse({status: "logged"});
//     }
//     return true; // Indicates we will send a response asynchronously
//   });
  
//   debugLog('Background script loaded');


function debugLog(message) {
  console.log(`[BACKGROUND ${new Date().toISOString()}]: ${message}`);
}

chrome.runtime.onInstalled.addListener(() => {
  debugLog('Extension installed/updated');
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  debugLog(`Received message: ${JSON.stringify(request)}`);
  
  if (request.action === "logSelectedText") {
    debugLog(`Selected text from content script: ${request.text}`);

    // Call the API with the selected text
    fetch('http://127.0.0.1:7860/api/v1/run/7f6d04f0-3bc1-4b74-9031-4da7b210cfc6?stream=false', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ "tweaks": {
        "TextInput-yDnxw": {
          "input_value": request.text
        }
      }}), // Use the selected text
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    // .then(data => {
    //   debugLog(`API response: ${JSON.stringify(data)}`);
    //   sendResponse({ status: "success", output: data.output }); // Send output back
    // })
    .then(data => {
      debugLog(`API response: ${JSON.stringify(data)}`);

      // Extract nested output text as per required format
      const output_text = data?.outputs?.[0]?.outputs?.[0]?.results?.text?.text || "";
      debugLog(`Extracted output_text: ${output_text}`);
      
      sendResponse({ status: "success", output: output_text }); // Send extracted output back
    })
    .catch(error => {
      debugLog(`Error calling API: ${error.message}`);
      sendResponse({ status: "error", message: error.message });
    });

    return true; // Indicates we will send a response asynchronously
  }
});

debugLog('Background script loaded');
