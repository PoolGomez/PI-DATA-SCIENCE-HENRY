from fastapi import FastAPI
from pandas import pd
from numpy import np

app = FastAPI()
    
#http://127.0.0.1:8000
@app.get("/")
def index():
    return {"mensaje":"Hola,pythones"}
