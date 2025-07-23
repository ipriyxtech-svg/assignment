
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

# Load the model
with open("linear_model.pkl", "rb") as f:
    model = pickle.load(f)

# Create router object
router = APIRouter()

# Input schema
class PredictRequest(BaseModel):
    features: list[float]

# Output schema
class PredictResponse(BaseModel):
    prediction: float

# Prediction route
@router.post("/predict", response_model=PredictResponse)
def predict(data: PredictRequest):
    try:
        # Convert input list to numpy array and reshape
        input_data = np.array(data.features).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        return PredictResponse(prediction=prediction)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
