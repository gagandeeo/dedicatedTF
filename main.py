from typing import Union
from test_model import prepare_image, load_model, predict
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import start_http_server, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import Counter, Gauge, Summary
from prometheus_client import REGISTRY, CollectorRegistry
from starlette.responses import Response
import ssl
import time

# Handle SSL certification for googleAPIs.
ssl._create_default_https_context = ssl._create_unverified_context

app = FastAPI()

# Create custom metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_count', 'Total number of requests')
IN_PROGRESS = Gauge('in_progress_requests', 'Number of requests in progress')

@app.middleware("http")
async def add_metrics(request: Request, call_next):
    IN_PROGRESS.inc()
    start_time = time.time()
    
    response = await call_next(request)
    
    REQUEST_TIME.observe(time.time() - start_time)
    REQUEST_COUNT.inc()
    IN_PROGRESS.dec()
    
    return response

# Load model
model = load_model("./mobilenetV2")

# CORS handlers
origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)

# About
@app.get("/about")
def hello_world():
    return {"result": "Model Serving API"}

# Upload image and predict
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    content = await file.read()
    preprocess_img = prepare_image(content)
    res = predict(preprocess_img, model)
    res = res[0][:,1:]
    return {"result": res}

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
