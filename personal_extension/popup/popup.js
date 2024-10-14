// document.addEventListener('DOMContentLoaded', function () {
//     const highlightedTextDiv = document.getElementById('highlightedText');
//     const clearTextBtn = document.getElementById('clearTextBtn');

//     // Request the stored highlighted text from the background script
//     chrome.runtime.sendMessage({ action: 'getStoredText' }, (response) => {
//         const storedText = response.data || [];
//         highlightedTextDiv.textContent = storedText.length > 0 ? storedText.join('\n\n') : "No text highlighted yet.";
//     });

//     // Clear the stored text when the user clicks the "Clear Text" button
//     clearTextBtn.addEventListener('click', function () {
//         chrome.runtime.sendMessage({ action: 'clearStoredText' }, () => {
//             highlightedTextDiv.textContent = "No text highlighted yet.";
//         });
//     });
// });

document.addEventListener('DOMContentLoaded', function () {
    const highlightedTextDiv = document.getElementById('highlightedText');
    const clearTextBtn = document.getElementById('clearTextBtn');

    // Request the stored highlighted text from the background script
    chrome.runtime.sendMessage({ action: 'getStoredText' }, (response) => {
        const storedText = response.data || [];
        highlightedTextDiv.textContent = storedText.length > 0 ? storedText.join('\n\n') : "No text highlighted yet.";
    });

    // Clear the stored text when the user clicks the "Clear Text" button
    clearTextBtn.addEventListener('click', function () {
        chrome.runtime.sendMessage({ action: 'clearStoredText' }, () => {
            highlightedTextDiv.textContent = "No text highlighted yet.";
        });
    });
});
