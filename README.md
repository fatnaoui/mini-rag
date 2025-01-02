# mini-rag

## Setup the environment variables

```bash
$ cp .env.example .env
```

set your environment variables in the '.env' file like in the '.env.example' file

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --port 5000 --host 0.0.0.0
```