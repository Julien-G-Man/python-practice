from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI()

base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'my_model.joblib')

model = joblib.load(model_path)

class ModelInput(BaseModel):
    feature1: float
    feature2: float


@app.post("/predict")
def predict(data: ModelInput):
    prediction = model.predict([[
        data.feature1, data.feature2
    ]])
    return {"prediction": prediction[0]}