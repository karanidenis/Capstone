document.addEventListener("mouseup", () => {
    const selectedText = window.getSelection().toString().trim();
    if (selectedText.length > 0) {
        chrome.runtime.sendMessage({ action: 'storeText', text: selectedText }, (response) => {
            if (response && response.success) {
                console.log("Highlighted text stored:", selectedText);
            }
        });
    }
});
