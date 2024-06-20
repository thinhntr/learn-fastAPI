from python:3.10

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY main.py .

COPY views .

CMD ["fastapi", "run", "main.py", "--port", "80"]
