let selectedTextContent = '';
let floatingWindow = null;

// Create and style the floating window
function createFloatingWindow() {
  const div = document.createElement('div');
  div.style.cssText = `
    position: absolute;
    max-width: 300px;
    padding: 10px;
    background: white;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    z-index: 10000;
    font-size: 14px;
    line-height: 1.4;
    overflow-wrap: break-word;
    display: none;
  `;
  document.body.appendChild(div);
  return div;
}


function hideFloatingWindow() {
  if (floatingWindow) {
    floatingWindow.style.display = 'none';
  }
}

function showFloatingWindow(text, x, y) {
  if (!floatingWindow) {
    floatingWindow = createFloatingWindow();
  }
  
  floatingWindow.textContent = text;
  floatingWindow.style.display = 'block';
  
  // Position the window next to the selection, slightly offset to avoid overlap
  const windowWidth = floatingWindow.offsetWidth;
  const windowHeight = floatingWindow.offsetHeight;
  const viewportWidth = window.innerWidth;
  const viewportHeight = window.innerHeight;

  // Calculate final position, adjusting to ensure it's near the highlighted text
  let finalX = x + window.scrollX + 10;  // Add some padding to the right of the selection
  let finalY = y + window.scrollY + 10;  // Add some padding below the selection

  // Prevent the floating window from going off the right edge of the viewport
  if (finalX + windowWidth > viewportWidth + window.scrollX) {
    finalX = x + window.scrollX - windowWidth - 10; // Position to the left if it's too wide
  }

  // Prevent the floating window from going off the bottom edge of the viewport
  if (finalY + windowHeight > viewportHeight + window.scrollY) {
    finalY = y + window.scrollY - windowHeight - 10; // Position above if it's too tall
  }

  // Apply final positioning
  floatingWindow.style.left = `${finalX}px`;
  floatingWindow.style.top = `${finalY}px`;
}


// Listen for toolbar icon click message from background
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "triggerApiRequest") {
    getSelectedText();
  }
});

function getSelectedText() {
  try {
    const selection = window.getSelection();
    selectedTextContent = selection.toString().trim();
    
    if (selectedTextContent) {
      console.log('Selected text variable:', selectedTextContent);
      
      // Get the selection coordinates
      const range = selection.getRangeAt(0);
      const rect = range.getBoundingClientRect();
      
      // Show loading message in floating window
      showFloatingWindow("Loading...", rect.right + window.scrollX + 5, rect.top + window.scrollY);
      
      // Send selected text to background script
      chrome.runtime.sendMessage({ action: "logSelectedText", text: selectedTextContent }, function(response) {
        if (chrome.runtime.lastError) {
          console.error(`Error sending message: ${chrome.runtime.lastError.message}`);
        } else {
          console.log(`Message sent to background. Response: ${JSON.stringify(response)}`);

          // Show the API output in the floating window
          if (response.status === "success") {
            showFloatingWindow(response.output, rect.right + window.scrollX + 5, rect.top + window.scrollY);
          } else {
            showFloatingWindow(`Error: ${response.message}`, rect.right + window.scrollX + 5, rect.top + window.scrollY);
          }
        }
      });
    } else {
      hideFloatingWindow();
    }
  } catch (error) {
    console.error(`Error in getSelectedText: ${error.message}`);
  }
}

// // Hide window when clicking outside
// document.addEventListener('mousedown', function(e) {
//   if (floatingWindow && !floatingWindow.contains(e.target)) {
//     hideFloatingWindow();
//   }
// });

// Initial log message
console.log('Content script loaded. Use getSelectedText() to manually trigger text selection logging.');  
