# Simple recommendation API

This is based on [fastapi-ml-template](https://github.com/yagays/fastapi-ml-template)

## Run Web API
### Local
```sh
$ poetry install 
$ poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 9000
```

### Docker
```sh
$ docker build -f Dockerfile -t fastapi-ml .
$ docker run -p 9000:9000 --rm --name fastapi-ml -t -i fastapi-ml
```

### Docker Compose

```sh
$ docker compose up --build
```

## Request Commands

```sh 
$ curl --request POST --url http://127.0.0.1:9000/api/v1/predict --header 'Content-Type: application/json' --data '{"item_id": "item3"}'
```

```sh
$ http POST http://127.0.0.1:9000/api/v1/predict item_id=item3
```

## Run Tests and Linter
### Using tox
```
$ poetry run tox
```

### Individual test
```
poetry run flake8 app tests
poetry run python -m pytest -vv .
```


## Reference

- [tiangolo/full\-stack\-fastapi\-postgresql: Full stack, modern web application generator\. Using FastAPI, PostgreSQL as database, Docker, automatic HTTPS and more\.](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [eightBEC/fastapi\-ml\-skeleton: FastAPI Skeleton App to serve machine learning models production\-ready\.](https://github.com/eightBEC/fastapi-ml-skeleton)