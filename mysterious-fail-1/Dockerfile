FROM python:3.8-slim

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python3", "reverse_figlet.py"]
