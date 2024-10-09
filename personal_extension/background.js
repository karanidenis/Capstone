let storedText = [];

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "storeText") {
        storedText.push(message.data);
        sendResponse({ status: "Text stored successfully" });
    }
    if (message.action === "getStoredText") {
        sendResponse({ data: storedText });
    }
    if (message.action === "clearStoredText") {
        storedText = []; // Clear the stored text
        sendResponse({ status: "Text cleared successfully" });
    }
});
