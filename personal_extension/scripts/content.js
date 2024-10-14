document.addEventListener("mouseup", () => {
    const selectedText = window.getSelection().toString().trim();
    if (selectedText.length > 0) {
        // Get the current page's URL and send it to the background script
        const currentPageUrl = window.location.href;
        
        chrome.runtime.sendMessage({ 
            action: 'storeUrl', 
            url: currentPageUrl 
        }, (response) => {
            if (response && response.success) {
                console.log("URL stored:", currentPageUrl);
            }
        });
    }
});
