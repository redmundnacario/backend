# NOTES on FastAPI

## Installing FastAPI

```
pip install fastapi
```

Install uvicorn for starting an ASGI server for production.
```
pip install uvicorn[standard]
```

## Running your first server

On `./first_server` directory, run the following...
```
uvicorn main:app --reload
```

On the terminal, open the localhost link in the browser.
Adding `/docs` or `/redoc` in the link will go to the automatic interactive API documentation.

##
