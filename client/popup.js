// popup.js

const host = 'http://127.0.0.1:8000/generate'

// Define the form elements and their values
const taskInput = document.getElementById('plan');
const dateInput = document.getElementById('complete-before');
const submitButton = document.getElementById('submit-button');
const table = document.getElementById("task-table");
const copyButton = document.getElementById('copyButton');

// Define the event listener for the submit button
submitButton.addEventListener('click', async (event) => {
  event.preventDefault();
  console.log('Pressed');
  // Get the user input values
  const task = taskInput.value;
  const date = dateInput.value;
  
  if (task.trim() === '') {
    alert('Please enter a task name.');
    return;
  }

  // Check if days to complete is a number greater than zero
  if (isNaN(dateInput.value) || Number(dateInput.value) <= 0) {
    alert('Please enter a valid number of days to complete (greater than zero).');
    return;
  }

  table.classList.add("loader");
  copyButton.innerText = 'Loading...';

  var formdata = new FormData();
  formdata.append("complete_before", date);
  formdata.append("plan", task);

  var requestOptions = {
    method: 'POST',
    body: formdata
  };

  // Send the data to the server and get the response
  fetch(host, requestOptions)
  .then((response) => {
    // Log the response for debugging
    console.log(response);
    // Check if the response is valid
    if (!response.ok) {
      throw new Error("Failed to get tasks");
    }
    // Parse the response body as JSON
    return response.json();
  })
  .then((data) => {
    // Update the UI with the new data
    table.classList.remove("loader");
    updateUI(data);
    // Create the "Copy to Clipboard" button
    copyButton.classList.add("button")
    copyButton.innerText = 'Copy to Clipboard';
  })
  .catch((error) => {
    // Log any errors
    console.error(error);
  });

});


// Define the function to update the UI with the response data
function updateUI(tasks) {
    let taskTable = document.getElementById("task-table");
    taskTable.innerHTML = `<thead>
                                <tr>
                                <th>Name</th>
                                <th>Description</th>
                                <th>Deadline</th>
                                <th>Resources</th>
                                <th>Risks</th>
                                <th>Reference</th>
                                </tr>
                            </thead>`;
  
    tasks.forEach((task) => {
      let row = taskTable.insertRow();
      row.innerHTML = `<td>${task.name}</td>
                       <td>${task.description}</td>
                       <td>${new Date(task.deadline * 1000).toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}</td>
                       <td>${task.resources.join(", ")}</td>
                       <td>${task.risks.join(", ")}</td>
                       <td>${task.reference.join(", ")}</td>`;
    });
  }
  
// Add an event listener to the "Copy to Clipboard" button
copyButton.addEventListener('click', () => {
  // Create a textarea element to hold the table contents
  const textarea = document.createElement('textarea');
  textarea.value = table.innerText;
  // Add the textarea element to the document
  document.body.appendChild(textarea);
  // Select the contents of the textarea
  textarea.select();
  // Copy the selected contents to the clipboard
  document.execCommand('copy');
  // Alert
  alert("Sub-Tasks copied to clipboard!");
  // Remove the textarea element from the document
  document.body.removeChild(textarea);
});