from python:3.10

WORKDIR /backend

COPY backend/requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY backend/main.py ./main.py

COPY frontend /frontend

CMD ["fastapi", "run", "/backend/main.py", "--port", "80"]
