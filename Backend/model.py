import joblib
from preprocess import preprocess_input
from schema import StudentData

# Load all models at startup
models = {
    "model_a": joblib.load("models/model_a.pkl"),
    "model_b": joblib.load("models/model_b.pkl"),
    "model_c": joblib.load("models/model_c.pkl")
}

def predict(data: StudentData):
    model = models[data.model_choice.value]
    processed = preprocess_input(data)
    pred = model.predict([processed])[0]
    
    try:
        conf = max(model.predict_proba([processed])[0])
    except:
        conf = None  # not all models have predict_proba
    
    return {"prediction": str(pred), "confidence": conf}
