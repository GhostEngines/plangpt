# PlanGPT

PlanGPT is an AI-based application that lets you execute any plan step-by-step. With PlanGPT, you can easily define your goals and deadlines, and the app generates a set of tasks and sub-tasks to help you achieve those goals. PlanGPT is built using GPT-3 and Python Flask, and it includes a browser extension front-end developed by ChatGPT.

With PlanGPT, you can simply answer "What do you want to accomplish?" and "When is the deadline for it?", and the app will generate a task name, description, deadline, risks, and reference links for you to follow.


![Alt Text](https://github.com/GhostEngines/plangpt/blob/main/assets/demo.gif)

## Features
- :rocket: Easy to use: Simply answer two questions to get started
- :computer: GPT-3 powered: Use the power of GPT-3 to generate a customized plan
- :clipboard: Detailed plan: Get a detailed task name, description, deadline, risks, and reference links
- :floppy_disk: Flask backend: Use the Flask backend to communicate with the GPT-3 API
- :globe_with_meridians: All browser support: Run PlanGPT on your favourite browsers

## Installation
To manually install the PlanGPT extension, follow these steps:

1. Clone the GitHub repository:
`git clone https://github.com/GhostEngines/plangpt.git`

2. Open your preferred browser (Chrome, Firefox, or Edge)

3. In the address bar, navigate to `chrome://extensions` (or `edge://extensions` for Microsoft Edge)

4. Turn on "Developer mode" by toggling the switch in the top right corner

5. Click the "Load unpacked" button and select the client folder from the cloned repository

6. Once the extension is loaded, you should see the PlanGPT icon in your browser's toolbar.

## Running the Flask app
To run the Flask app, follow these steps:

1. Navigate to the server directory:

```
cd server
```

2. Create a new virtual environment and activate it:

```
python3 -m virtualenv venv
```

```
source venv/bin/activate
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Rename the `env.example` file to `.env` and add your OpenAI API key to the `OPENAI_API_KEY` field

5. Start the server:

```
python app.py
```

## License
This project is licensed under the Apache 2.0 License.