start:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 9000

init-docker: ## initialize docker image
	docker build -f Dockerfile -t fastapi-ml .

init-docker-no-cache: ## initialize docker image without cachhe
	docker build --no-cache -t fastapi-ml -f Dockerfile .

start-container: ## create docker container
	docker run -p 9000:9000 --rm --name fastapi-ml -t -i fastapi-ml

clean-container: ## remove Docker container
	docker rm fastapi-ml

clean-image: ## remove Docker image
	docker image rm fastapi-ml

flake8:
	poetry run flake8 app tests

pytest:
	poetry run python -m pytest -vv .

