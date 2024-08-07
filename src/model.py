import os
import pickle

MODEL_FOLDER = os.path.relpath("models", "simple-mlops-api")

def load_model(model_path: str = "model.pkl"):
    model_path = os.path.join(MODEL_FOLDER, model_path)
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    return model

def load_encode(encoder_path: str = "ohe.pkl"):
    encoder_path