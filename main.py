from fastapi import FastAPI
from pandas import pandas
#from numpy import numpy

app = FastAPI()
    
#http://127.0.0.1:8000
@app.get("/")
def index():
    return {"mensaje":"Hello word"}
