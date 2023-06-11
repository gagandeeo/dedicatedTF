from typing import Union
from test_model import prepare_image, load_model, predict
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import ssl
import uvicorn

# Handle SSL certification for googleAPIs.
ssl._create_default_https_context = ssl._create_unverified_context

app = FastAPI()

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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)