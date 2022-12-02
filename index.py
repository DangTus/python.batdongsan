from fastapi import FastAPI
from module.api import get

#uvicorn index:app --reload

app = FastAPI()


@app.get("/getapi")
def getall(gia_min: int = None, gia_max: int = None, quan_huyen: str = None, tinh_thanh: str = None):
    return get.get_bai_viet(gia_min, gia_max, quan_huyen, tinh_thanh)
