// function contentLog(message) {
//     console.log(`[CONTENT ${new Date().toISOString()}]: ${message}`);
//   }
  
//   function getSelectedText() {
//     contentLog('getSelectedText function called');
//     try {
//       const selection = window.getSelection();
//       contentLog(`Selection object: ${selection}`);
//       const selectedText = selection.toString().trim();
//       contentLog(`Raw selected text: "${selectedText}"`);
      
//       if (selectedText) {
//         contentLog(`Selected text (${selectedText.length} characters): ${selectedText}`);
//         chrome.runtime.sendMessage({action: "logSelectedText", text: selectedText}, function(response) {
//           if (chrome.runtime.lastError) {
//             contentLog(`Error sending message: ${chrome.runtime.lastError.message}`);
//           } else {
//             contentLog(`Message sent to background. Response: ${JSON.stringify(response)}`);
//           }
//         });
//       } else {
//         contentLog('No text currently selected');
//       }
//     } catch (error) {
//       contentLog(`Error in getSelectedText: ${error.message}`);
//     }
//   }
  
//   // Automatically log selection changes
//   document.addEventListener('selectionchange', function() {
//     contentLog('Selection changed event fired');
//     getSelectedText();
//   });
  
//   contentLog('Content script loaded. Use getSelectedText() to manually trigger text selection logging.');
  
//   //Inject a button into the page for easy testing
//   const button = document.createElement('button');
//   button.textContent = 'Log Selected Text';
//   button.style.position = 'fixed';
//   button.style.top = '10px';
//   button.style.right = '10px';
//   button.style.zIndex = '9999';
//   button.addEventListener('click', getSelectedText);
//   document.body.appendChild(button);



// function getSelectedText() {
//     try {
//       const selection = window.getSelection();
//       selectedTextContent = selection.toString().trim();
      
//       if (selectedTextContent) {
//         console.log('Selected text variable:', selectedTextContent);
//       }
//     } catch (error) {
//       contentLog(`Error in getSelectedText: ${error.message}`);
//     }
//   }
  
//   // Listen for text selection
//   document.addEventListener('selectionchange', function() {
//     getSelectedText();
//   });


// let selectedTextContent = '';
// let floatingWindow = null;

// // Create and style the floating window
// function createFloatingWindow() {
//   const div = document.createElement('div');
//   div.style.cssText = `
//     position: absolute;
//     max-width: 300px;
//     padding: 10px;
//     background: white;
//     border: 1px solid #ccc;
//     border-radius: 4px;
//     box-shadow: 0 2px 5px rgba(0,0,0,0.2);
//     z-index: 10000;
//     font-size: 14px;
//     line-height: 1.4;
//     overflow-wrap: break-word;
//     display: none;
//   `;
//   document.body.appendChild(div);
//   return div;
// }

// function showFloatingWindow(text, x, y) {
//   if (!floatingWindow) {
//     floatingWindow = createFloatingWindow();
//   }
  
//   floatingWindow.textContent = text;
//   floatingWindow.style.display = 'block';
  
//   // Position the window next to the selection
//   const windowWidth = floatingWindow.offsetWidth;
//   const windowHeight = floatingWindow.offsetHeight;
//   const viewportWidth = window.innerWidth;
//   const viewportHeight = window.innerHeight;
  
//   // Adjust position to keep window within viewport
//   let finalX = x;
//   let finalY = y;
  
//   if (x + windowWidth > viewportWidth) {
//     finalX = x - windowWidth;
//   }
  
//   if (y + windowHeight > viewportHeight) {
//     finalY = y - windowHeight;
//   }
  
//   floatingWindow.style.left = `${finalX}px`;
//   floatingWindow.style.top = `${finalY}px`;
// }

// function hideFloatingWindow() {
//   if (floatingWindow) {
//     floatingWindow.style.display = 'none';
//   }
// }

// function getSelectedText() {
//   try {
//     const selection = window.getSelection();
//     selectedTextContent = selection.toString().trim();
    
//     if (selectedTextContent) {
//       console.log('Selected text variable:', selectedTextContent);
      
//       // Get the selection coordinates
//       const range = selection.getRangeAt(0);
//       const rect = range.getBoundingClientRect();
      
//       // Show floating window at the end of selection
//       showFloatingWindow(
//         selectedTextContent,
//         rect.right + window.scrollX + 5, // 5px offset from selection
//         rect.top + window.scrollY
//       );
//     } else {
//       hideFloatingWindow();
//     }
//   } catch (error) {
//     console.log(`Error in getSelectedText: ${error.message}`);
//   }
// }

// // Listen for text selection
// document.addEventListener('selectionchange', function() {
//   // Small delay to ensure the selection is complete
//   setTimeout(getSelectedText, 10);
// });

// // Hide window when clicking outside
// document.addEventListener('mousedown', function(e) {
//   if (floatingWindow && !floatingWindow.contains(e.target)) {
//     hideFloatingWindow();
//   }
// });

// // Hide window when scrolling
// document.addEventListener('scroll', function() {
//   hideFloatingWindow();
// });

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

function showFloatingWindow(text, x, y) {
  if (!floatingWindow) {
    floatingWindow = createFloatingWindow();
  }
  
  floatingWindow.textContent = text;
  floatingWindow.style.display = 'block';
  
  // Position the window next to the selection
  const windowWidth = floatingWindow.offsetWidth;
  const windowHeight = floatingWindow.offsetHeight;
  const viewportWidth = window.innerWidth;
  const viewportHeight = window.innerHeight;
  
  let finalX = x;
  let finalY = y;
  
  if (x + windowWidth > viewportWidth) {
    finalX = x - windowWidth;
  }
  
  if (y + windowHeight > viewportHeight) {
    finalY = y - windowHeight;
  }
  
  floatingWindow.style.left = `${finalX}px`;
  floatingWindow.style.top = `${finalY}px`;
}

function hideFloatingWindow() {
  if (floatingWindow) {
    floatingWindow.style.display = 'none';
  }
}

function getSelectedText() {
  try {
    const selection = window.getSelection();
    selectedTextContent = selection.toString().trim();
    
    if (selectedTextContent) {
      console.log('Selected text variable:', selectedTextContent);
      
      // Get the selection coordinates
      const range = selection.getRangeAt(0);
      const rect = range.getBoundingClientRect();
      
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

// Listen for text selection
document.addEventListener('selectionchange', function() {
  setTimeout(getSelectedText, 10);
});

// Hide window when clicking outside
document.addEventListener('mousedown', function(e) {
  if (floatingWindow && !floatingWindow.contains(e.target)) {
    hideFloatingWindow();
  }
});

// Hide window when scrolling
document.addEventListener('scroll', function() {
  hideFloatingWindow();
});

// Initial log message
console.log('Content script loaded. Use getSelectedText() to manually trigger text selection logging.');
