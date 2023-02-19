# PYTHON IMAGE
FROM python:3.10-slim-buster

# WORKDIR /code
COPY server/requirements.txt /requirements.txt
COPY server/main.py /main.py

# REQUIREMENTS FILE
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]