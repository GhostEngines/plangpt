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

@app.get('/', include_in_schema= False)
def home():
    return {'status': 'Working'}

@app.get('/{date}/{task}')
def function(date, task):
    return todochat(plan=task, complete_before=date)
