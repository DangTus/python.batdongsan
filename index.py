from fastapi import FastAPI
from module.api import get

app = FastAPI()

@app.get("/getapi/")
def getall():
    return  get.get()  



