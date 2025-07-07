from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
model = pickle.load(open("model.pkl", "rb"))

class AreaData(BaseModel):
    incidents: int
    last_30_days: int
    police_presence: int

@app.get("/")
def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(data: AreaData):
    input_data = np.array([[data.incidents, data.last_30_days, data.police_presence]])
    result = model.predict_proba(input_data)[0][1]
    return {"risk_score": round(result, 2)}
