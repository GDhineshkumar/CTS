from fastapi import FastAPI
from .database import Base, engine
from .models import User
from .routes import auth_routes, predict_routes, fuel_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fuel Prediction API",
    description="ML Backend for Fuel Blend Predictions",
    version="1.0.0"
)

# Include all routers
app.include_router(auth_routes.router)
app.include_router(predict_routes.router)
app.include_router(fuel_routes.router)

@app.get("/")
def root():
    return {
        "message": "Fuel Prediction API",
        "endpoints": {
            "auth": "/auth/token",
            "fuel_prediction": "/fuel/predict",
            "csv_upload": "/fuel/predict-csv",
            "template": "/fuel/input-template"
        },
        "docs": "/docs"
    }