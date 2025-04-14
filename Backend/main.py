from fastapi import FastAPI
from schema import StudentData, PredictionResponse
from model import predict

app = FastAPI()

@app.post("/predict", response_model=PredictionResponse)
def get_prediction(data: StudentData):
    result = predict(data)
    return result
