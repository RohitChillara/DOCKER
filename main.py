from fastapi import FastAPI


app=FastAPI() #creating an instance of the FastAPI class, the basic step to start building an API using FastAPI. This instance will be used to define routes and handle requests.

@app.get("/") #decorator to specify the type of request and the path
def read_root():
    return {"message": "Hello from Rohit using FastAPI"}