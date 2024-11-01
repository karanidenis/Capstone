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
      
//       // Send selected text to background script
//       chrome.runtime.sendMessage({ action: "logSelectedText", text: selectedTextContent }, function(response) {
//         if (chrome.runtime.lastError) {
//           console.error(`Error sending message: ${chrome.runtime.lastError.message}`);
//         } else {
//           console.log(`Message sent to background. Response: ${JSON.stringify(response)}`);

//           // Show the API output in the floating window
//           if (response.status === "success") {
//             showFloatingWindow(response.output, rect.right + window.scrollX + 5, rect.top + window.scrollY);
//           } else {
//             showFloatingWindow(`Error: ${response.message}`, rect.right + window.scrollX + 5, rect.top + window.scrollY);
//           }
//         }
//       });
//     } else {
//       hideFloatingWindow();
//     }
//   } catch (error) {
//     console.error(`Error in getSelectedText: ${error.message}`);
//   }
// }

// // Listen for text selection
// document.addEventListener('selectionchange', function() {
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

// // Initial log message
// console.log('Content script loaded. Use getSelectedText() to manually trigger text selection logging.');


let selectedTextContent = '';
let floatingWindow = null;
let triggerIcon = null;

// Create and style the floating window with loader
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
  div.innerHTML = `<p>Thank you for using LearnMate, your response is loading...</p><div class="loader"></div>`;
  document.body.appendChild(div);
  return div;
}

// Create loader animation
const style = document.createElement('style');
style.innerHTML = `
  .loader {
    border: 4px solid #f3f3f3;
    border-top: 4px solid #3498db;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    animation: spin 1s linear infinite;
    margin-top: 5px;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
`;
document.head.appendChild(style);

function showFloatingWindow(text, x, y) {
  if (!floatingWindow) {
    floatingWindow = createFloatingWindow();
  }
  floatingWindow.innerHTML = text;
  floatingWindow.style.display = 'block';

  // Position and display window logic...
}

function createTriggerIcon(x, y) {
  if (!triggerIcon) {
    triggerIcon = document.createElement('button');
    triggerIcon.style.cssText = `
      position: absolute;
      width: 24px;
      height: 24px;
      background: url('your-icon.png') no-repeat center center;
      background-size: cover;
      border: none;
      cursor: pointer;
      z-index: 10000;
    `;
    triggerIcon.title = "Click to load response";
    document.body.appendChild(triggerIcon);
  }
  triggerIcon.style.left = `${x}px`;
  triggerIcon.style.top = `${y}px`;
  triggerIcon.style.display = 'block';
}

function getSelectedText() {
  try {
    const selection = window.getSelection();
    selectedTextContent = selection.toString().trim();
    if (selectedTextContent) {
      const range = selection.getRangeAt(0);
      const rect = range.getBoundingClientRect();
      createTriggerIcon(rect.right + window.scrollX + 5, rect.top + window.scrollY);
      
      // Trigger API call on icon click
      triggerIcon.onclick = () => {
        showFloatingWindow("Thank you for using LearnMate, your response is loading...", rect.right + window.scrollX + 5, rect.top + window.scrollY);
        triggerIcon.style.display = 'none'; // Hide the icon after clicking

        chrome.runtime.sendMessage({ action: "logSelectedText", text: selectedTextContent }, function(response) {
          if (chrome.runtime.lastError) {
            showFloatingWindow(`Error: ${chrome.runtime.lastError.message}`, rect.right + window.scrollX + 5, rect.top + window.scrollY);
          } else {
            if (response.status === "success") {
              showFloatingWindow(response.output, rect.right + window.scrollX + 5, rect.top + window.scrollY);
            } else {
              showFloatingWindow(`Error: ${response.message}`, rect.right + window.scrollX + 5, rect.top + window.scrollY);
            }
          }
        });
      };
    } else {
      hideFloatingWindow();
      if (triggerIcon) triggerIcon.style.display = 'none';
    }
  } catch (error) {
    console.error(`Error in getSelectedText: ${error.message}`);
  }
}

// Event listeners for text selection
document.addEventListener('selectionchange', function() {
  setTimeout(getSelectedText, 10);
});

document.addEventListener('mousedown', function(e) {
  if (floatingWindow && !floatingWindow.contains(e.target) && !triggerIcon.contains(e.target)) {
    hideFloatingWindow();
    if (triggerIcon) triggerIcon.style.display = 'none';
  }
});

document.addEventListener('scroll', hideFloatingWindow);

// Hide the floating window
function hideFloatingWindow() {
  if (floatingWindow) floatingWindow.style.display = 'none';
  if (triggerIcon) triggerIcon.style.display = 'none';
}
