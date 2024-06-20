help:
	@echo [USAGE]:
	@echo "  make build: build Docker image"
	@echo "  make run: run container"

build:
	docker build -t learnbackend:latest .

run:
	docker run --rm -it -p 80:80 learnbackend:latest

dev:
	fastapi dev main.py
