"use strict"

function setBadgeText(enabled) {
    const text = enabled ? "ON" : "OFF";
    void chrome.action.setBadgeText({ text: text });
}

function startUp() {
    chrome.storage.sync.get("enabled", (data) => {
        setBadgeText(!!data.enabled);
    });
}

chrome.runtime.onStartup.addListener(startUp);
chrome.runtime.onInstalled.addListener(startUp);

// Handle messages from content script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "storeText") {
        // Get the existing text from storage
        chrome.storage.sync.get("highlightedText", (data) => {
            const currentText = data.highlightedText || [];
            const updatedText = [...currentText, message.text];
            chrome.storage.sync.set({ highlightedText: updatedText }, () => {
                sendResponse({ success: true });
            });
        });
        return true; // Ensures asynchronous response is sent
    }

    if (message.action === "getStoredText") {
        chrome.storage.sync.get("highlightedText", (data) => {
            sendResponse({ data: data.highlightedText || [] });
        });
        return true;
    }

    if (message.action === "clearStoredText") {
        chrome.storage.sync.remove("highlightedText", () => {
            sendResponse({ success: true });
        });
        return true;
    }
});
