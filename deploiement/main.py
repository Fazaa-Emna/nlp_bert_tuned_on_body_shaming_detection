from fastapi import FastAPI, Form
from root.workspace.prediction import BinaryBodyShaming
from typing import Optional
from pydantic import BaseModel
class Prediction(BaseModel):
    label: str
    value: Optional[float] = None
    model: Optional[str] = None

class SimplePrediction(Prediction):
    error : str = None

# start FasAPI
app = FastAPI()


# Initialize models
predictor = BinaryBodyShaming()


@app.post('/predict', response_model = SimplePrediction)
async def predict(text: str = Form(...)):

    try :
        label, proba = predictor.predict(text)
        result = {'label':label,'value':proba,'model':'binary body shaming fr'}
    except Exception as e:
        result = {'label':'','model':'binary body shaming fr','error':str(e)}
    return result