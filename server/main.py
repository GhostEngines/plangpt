from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Response
from langchain import OpenAI
from llm import get_current_datetime
from os import environ, getenv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if 'OPENAI_API_KEY' in environ:
    openai_api_key = environ['OPENAI_API_KEY']
else:
    from dotenv import load_dotenv
    load_dotenv()
    openai_api_key = getenv('OPENAI_API_KEY')

# Initialize OpenAI language model
llm = OpenAI(model_name="text-davinci-003", best_of=1,  max_tokens=2000, openai_api_key=openai_api_key)


@app.get('/')
async def check():
    return {'status': 'OK'}

@app.post("/generate")
async def generate_tasks(plan: str, complete_before: int):
    prompt = '''Please generate a JSON of subtasks and their deadlines for the task %s. The subtasks should be reasonable and not take more than a day to complete. I want to complete all the subtasks in %s days. Current Timestamp: %s
    The JSON output should be in the following format: [{"name": Subtask 1, "description": Description of subtask 1, "deadline": deadline for subtask 2 in unix timestamp, "resources" : [resources needed to accomplish subtask 1], "risks": [risks associated with subtask 1 includes potential roadblocks, obstacles, and challenges that may arise], "reference": reference links that are useful for subtask 1}, {"name": Subtask 2, "description": Description of subtask 2, , "deadline": deadline for subtask 2 in unix timestamp, "resources": [resources needed to accomplish subtask 2], "risks": [risks associated with subtask 2 includes potential roadblocks, obstacles, and challenges that may arise, "reference": reference links that are useful for subtask 2]}].'''%(plan, complete_before, get_current_datetime())
    response = llm(prompt)
    headers = {
        "x-content-type-options": "nosniff"
    }
    print(response)
    return Response(content=response, media_type='application/json', headers=headers)
