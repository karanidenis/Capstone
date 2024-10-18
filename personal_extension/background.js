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
      sendResponse({status: "logged"});
    }
    return true; // Indicates we will send a response asynchronously
  });
  
  debugLog('Background script loaded');