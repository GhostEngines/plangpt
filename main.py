from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from llm import todochat

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

@app.get('/{date}/{task}', include_in_schema = False)
def home(date, task):
    return todochat(plan=task, complete_before=date)
