FROM python:3.10-slim

WORKDIR /app

COPY hello_world.py .
COPY requirements.txt .
COPY test_hello_world.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4049

CMD ["python", "hello_world.py"]