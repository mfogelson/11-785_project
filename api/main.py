import logging
from typing import List

from fastapi import FastAPI

from .api_model import KeyGen

app = FastAPI()
model = None  # TODO: initialize some object that will serve as a wrapper for the model


@app.get("/")
def root():
    """Root endpoint for detection by load balancers.
    """
    return {"message": "API running."}


@app.post("/generate")
def generate(keyGen: KeyGen):
    payload = "working"
    status = True
    response = {"success": status, "payload": payload}
    return response
