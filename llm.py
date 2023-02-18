# GET CURRENT DATETIME

def get_current_datetime():
    from datetime import datetime
    import time
    current_timestamp = datetime.now()
    current_timestamp = int(time.mktime(current_timestamp.timetuple()))
    return current_timestamp

# UPDATED WORKING

def todochat(plan, complete_before):

    from langchain.llms import OpenAI

    llm = OpenAI(model_name="text-davinci-003", best_of=1,  max_tokens=2000)

    prompt = '''Please generate a JSON of subtasks and their deadlines for the task %s. The subtasks should be reasonable and not take more than a day to complete. I want to complete all the subtasks before %s. Current Timestamp: %s
    The JSON output should be in the following format: [{"name": Subtask 1, "description": Description of subtask 1, "deadline": deadline for subtask 2 in timestamp, "resources" : [resources needed to accomplish subtask 1], "risks": [risks associated with subtask 1 includes potential roadblocks, obstacles, and challenges that may arise]}, {"name": Subtask 2, "description": Description of subtask 2, , "deadline": deadline for subtask 2 in timestamp, "resources": [resources needed to accomplish subtask 2], "risks": [risks associated with subtask 2 includes potential roadblocks, obstacles, and challenges that may arise]}].'''%(plan, complete_before, get_current_datetime())

    return llm(prompt)