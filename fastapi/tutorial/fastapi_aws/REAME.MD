
## Create Folder
`mkdir serverless-fastapi`
`cd serverless-fastapi`


## VirtualEnv
`pip install virtualenv`
`virtualenv -p python3.7 env`
`source ./env/bin/activate`


## Install fastapi and Uvicorn
`pip install fastapi[all]`
`pip install uvicorn`

##  Create main.py
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```
## Run FastAI
`uvicorn main:app --reload`

## FastAPI API Documentation
`http://127.0.0.1:8000/docs`


## Add new route in main.py
```python
@app.get("/users")
async def get_users():
    return {"message": "Get Users!"}
```

## Restructuring files

From this
```
.
├── env
├── main.py
```

To This
```
.
└── app
    ├── __init__.py
    ├── main.py
    └── api
        ├── __init__.py
        └── api_v1
            ├── __init__.py
            ├── api.py
            └── endpoints
                ├── __init__.py
```

## Restarting uvicorn in port 8000
sudo lsof -i:8000
kill -9 95275
uvicorn main:app --reload

#
cd env/lib/python3.7/site-packages
zip -r9 /Users/redmundnacario/Documents/backend/fastapi/tutorial/fastapi_aws/serverless-fastapi/function.zip .
zip -g ./function.zip -r app