from fastapi import FastAPI, HTTPException, Depends, Body
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import Annotated
from .person_data import Person
import pandas as pd
from .model import load_model, load_encoder

app = FastAPI()

bearer = HTTPBearer()

ml_models = {}

@app.on_event("startup")
async def startup_event():
    """
    Startup event to load the models
    """
    ml_models["ohe"] = load_encoder()
    ml_models["models"] = load_model()

def get_username_from_token(token):
    if token == "abc123":
        return "renatex333"
    return ""

async def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer)):
    """
    Function to validate the token
    """
    token = credentials.credentials

    username = get_username_from_token(token)
    if username == "":
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    return {"username": username}

@app.get("/")
async def root():
    """
    Route to check that API is alive!
    """
    return "Model API is alive!"


@app.post("/predict")
async def predict(
    person: Annotated[
        Person,
        Body(
            examples=[
                {
                    "age": 42,
                    "job": "entrepreneur",
                    "marital": "married",
                    "education": "primary",
                    "balance": 558,
                    "housing": "yes",
                    "duration": 186,
                    "campaign": 2,
                }
            ],
        ),
    ],
    user=Depends(validate_token),
):
    """
    Route to make predictions!
    """
    # Load the models
    ohe = ml_models["ohe"]
    model = ml_models["models"]

    df_person = pd.DataFrame([person.dict()])

    person_t = ohe.transform(df_person)
    pred = model.predict(person_t)[0]

    return {
        "prediction": str(pred),
        "username": user["username"]
        }
