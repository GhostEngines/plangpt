from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain import OpenAI
from os import environ, getenv
import json

app = Flask(__name__)

CORS(app)

# GET CURRENT DATETIME

def get_current_datetime():
    from datetime import datetime
    import time
    current_timestamp = datetime.now()
    current_timestamp = int(time.mktime(current_timestamp.timetuple()))
    return current_timestamp


if 'OPENAI_API_KEY' in environ:
    openai_api_key = environ['OPENAI_API_KEY']
else:
    from dotenv import load_dotenv
    load_dotenv()
    openai_api_key = getenv('OPENAI_API_KEY')

# Initialize OpenAI language model
llm = OpenAI(model_name="text-davinci-003", best_of=1,  max_tokens=2000, openai_api_key=openai_api_key)


@app.route('/')
def check():
    return {'status': 'OK'}

@app.route('/generate', methods=['POST'])
def generate_tasks():
    plan = request.form['plan']
    complete_before = request.form['complete_before']    
    prompt = '''Please generate a JSON of subtasks and their deadlines for the task %s. The subtasks should be reasonable and not take more than a day to complete. I want to complete all the subtasks in %s days. Current Timestamp: %s
    The JSON output should be in the following format: [{"name": Subtask 1, "description": Description of subtask 1, "deadline": deadline for subtask 2 in unix timestamp, "resources" : [resources needed to accomplish subtask 1], "risks": [risks associated with subtask 1 includes potential roadblocks, obstacles, and challenges that may arise], "reference": reference links that are useful for subtask 1}, {"name": Subtask 2, "description": Description of subtask 2, , "deadline": deadline for subtask 2 in unix timestamp, "resources": [resources needed to accomplish subtask 2], "risks": [risks associated with subtask 2 includes potential roadblocks, obstacles, and challenges that may arise, "reference": reference links that are useful for subtask 2]}].'''%(plan, complete_before, get_current_datetime())
    response = llm(prompt)
    print(response)
    return json.loads(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)